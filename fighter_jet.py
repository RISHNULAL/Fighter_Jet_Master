import curses
import random
import time
import sys

JET_DESIGN = [
    "    /^\\    ",
    "   /___\\   ",
    "==/_______\\==",
    "     /_|_\\     "
]

MAX_HEALTH = 100
GAME_SPEED = 0.05
STONE_SPEED = 0.25


# ------------------ COLORS ------------------
def init_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)


# ------------------ MENU ------------------
def show_menu(stdscr):
    stdscr.nodelay(False)   # WAIT for input
    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        title = "FIGHTER JET TERMINAL GAME"
        stdscr.addstr(h//2 - 4, w//2 - len(title)//2, title, curses.A_BOLD)

        stdscr.addstr(h//2 - 1, w//2 - 10, "[S] Start Game")
        stdscr.addstr(h//2, w//2 - 10, "[H] Help")
        stdscr.addstr(h//2 + 1, w//2 - 10, "[E] Exit")

        stdscr.refresh()

        key = stdscr.getch()

        if key in [ord('s'), ord('S')]:
            return "start"
        elif key in [ord('h'), ord('H')]:
            return "help"
        elif key in [ord('e'), ord('E')]:
            return "exit"


# ------------------ HELP SCREEN ------------------
def show_help(stdscr):
    stdscr.clear()
    stdscr.nodelay(False)  # WAIT here too
    h, w = stdscr.getmaxyx()

    help_text = [
        "========== HELP ==========",
        "",
        "Arrow Keys  -> Move Jet",
        "Space       -> Shoot",
        "Q           -> Quit Game",
        "Ctrl + Z    -> Force Stop",
        "",
        "OBSTACLES:",
        "[###]   Red     -> Normal Stone (-10 HP)",
        "[#####] Yellow  -> Big Stone (-15 HP)",
        "[SUP]    Green  -> Supply (Double Gun 10 sec)",
        "",
        "Press B to return to MENU"
    ]

    for i, line in enumerate(help_text):
        stdscr.addstr(h//2 - len(help_text)//2 + i,
                      w//2 - len(line)//2, line)

    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key in [ord('b'), ord('B')]:
            break


# ------------------ DRAW JET ------------------
def draw_jet(stdscr, y, x):
    for i, line in enumerate(JET_DESIGN):
        stdscr.addstr(y + i, x, line, curses.color_pair(5))


# ------------------ GAME ------------------
def start_game(stdscr):
    stdscr.nodelay(True)
    stdscr.keypad(True)

    height, width = stdscr.getmaxyx()

    jet_height = len(JET_DESIGN)
    jet_width = len(JET_DESIGN[0])

    jet_x = width // 2 - jet_width // 2
    jet_y = height - jet_height - 2

    bullets = []
    stones = []
    score = 0
    health = MAX_HEALTH
    double_gun = False
    double_timer = 0

    last_stone_time = time.time()

    while True:
        stdscr.clear()
        key = stdscr.getch()

        # Ctrl + Z handling
        if key == 26:   # ASCII for Ctrl+Z
            stdscr.nodelay(False)
            stdscr.addstr(height//2, width//2 - 10,
                          "CTRL+Z Pressed. Exiting...")
            stdscr.refresh()
            time.sleep(2)
            sys.exit()

        # Movement
        if key == curses.KEY_LEFT and jet_x > 1:
            jet_x -= 2
        elif key == curses.KEY_RIGHT and jet_x < width - jet_width - 1:
            jet_x += 2
        elif key == curses.KEY_UP and jet_y > 1:
            jet_y -= 1
        elif key == curses.KEY_DOWN and jet_y < height - jet_height - 1:
            jet_y += 1
        elif key == ord(' '):
            if double_gun:
                bullets.append([jet_y - 1, jet_x + 2])
                bullets.append([jet_y - 1, jet_x + jet_width - 3])
            else:
                bullets.append([jet_y - 1, jet_x + jet_width // 2])
        elif key == ord('q'):
            break

        # Spawn stones
        if time.time() - last_stone_time > STONE_SPEED:
            stone_type = random.choice(["normal", "big", "supply"])
            x_pos = random.randint(2, width - 10)
            stones.append([0, x_pos, stone_type])
            last_stone_time = time.time()

        for stone in stones:
            stone[0] += 1

        for bullet in bullets:
            bullet[0] -= 1

        stones = [s for s in stones if s[0] < height - 1]
        bullets = [b for b in bullets if b[0] > 0]

        # Bullet collision
        for bullet in bullets[:]:
            for stone in stones[:]:
                if bullet[0] == stone[0] and stone[1] <= bullet[1] <= stone[1] + 4:
                    if stone[2] == "supply":
                        double_gun = True
                        double_timer = time.time()
                    score += 2 if stone[2] == "big" else 1
                    bullets.remove(bullet)
                    stones.remove(stone)
                    break

        if double_gun and time.time() - double_timer > 10:
            double_gun = False

        # Jet collision
        for stone in stones[:]:
            if (jet_y <= stone[0] <= jet_y + jet_height and
                jet_x <= stone[1] <= jet_x + jet_width):
                health -= 15 if stone[2] == "big" else 10
                stones.remove(stone)

        draw_jet(stdscr, jet_y, jet_x)

        for stone in stones:
            if stone[2] == "normal":
                stdscr.addstr(stone[0], stone[1], "[###]", curses.color_pair(1))
            elif stone[2] == "big":
                stdscr.addstr(stone[0], stone[1], "[#####]", curses.color_pair(2))
            elif stone[2] == "supply":
                stdscr.addstr(stone[0], stone[1], "[SUP]", curses.color_pair(3))

        for bullet in bullets:
            stdscr.addstr(bullet[0], bullet[1], "|", curses.color_pair(4))

        health_bar = "█" * (health // 5)
        stdscr.addstr(0, 2, f"Health: [{health_bar:<20}] {health}")
        stdscr.addstr(1, 2, f"Score: {score}")
        stdscr.addstr(2, 2, f"Double Gun: {'ON' if double_gun else 'OFF'}")

        if health <= 0:
            stdscr.nodelay(False)
            stdscr.addstr(height//2, width//2 - 5, "GAME OVER")
            stdscr.addstr(height//2 + 1, width//2 - 8,
                          f"Final Score: {score}")
            stdscr.addstr(height//2 + 3, width//2 - 12,
                          "Press any key to return to MENU")
            stdscr.refresh()
            stdscr.getch()
            break

        stdscr.refresh()
        time.sleep(GAME_SPEED)


# ------------------ MAIN ------------------
def main(stdscr):
    curses.curs_set(0)
    init_colors()

    while True:
        choice = show_menu(stdscr)

        if choice == "start":
            start_game(stdscr)
        elif choice == "help":
            show_help(stdscr)
        elif choice == "exit":
            break


if __name__ == "__main__":
    curses.wrapper(main)