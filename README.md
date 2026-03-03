# 🚀 Fighter Jet Master (Terminal Edition)

A fully interactive **Terminal-Based Fighter Jet Shooting Game** built using Python and `curses`.

This game runs entirely inside the terminal and features a dynamic obstacle system, power-ups, health management, and an interactive menu system.

---

## 🎮 Features

* 🛩 Realistic ASCII Fighter Jet
* 🎯 Smooth Arrow Key Movement
* 🔫 Shooting Mechanism (Single & Double Gun Mode)
* 💥 Multiple Obstacle Types
* 🎁 Supply Drops (Power-ups)
* ❤️ Health System with Visual Health Bar
* 📊 Score Tracking
* 🏠 Main Menu (Start / Help / Exit)
* 📘 Help Screen with Controls Guide
* 🎨 Colored Terminal Graphics
* 🔄 Returns to Menu after Game Over

---

## 🕹 Controls

### 🚀 In Game

| Key         | Action     |
| ----------- | ---------- |
| ⬅️ ➡️ ⬆️ ⬇️ | Move Jet   |
| Space       | Shoot      |
| Q           | Quit Game  |
| Ctrl + Z    | Force Exit |

### 🏠 Menu

| Key | Action     |
| --- | ---------- |
| S   | Start Game |
| H   | Help       |
| E   | Exit       |

### 📘 Help Screen

| Key | Action         |
| --- | -------------- |
| B   | Return to Menu |

---

## 🧱 Obstacle Types

| Type      | Color     | Effect                       |
| --------- | --------- | ---------------------------- |
| `[###]`   | 🔴 Red    | Normal Stone (-10 HP)        |
| `[#####]` | 🟡 Yellow | Big Stone (-15 HP)           |
| `[SUP]`   | 🟢 Green  | Double Gun Mode (10 seconds) |

---

## 🛠 Requirements

* Python **3.12 recommended**
* Windows: `windows-curses`
* Linux/macOS: Built-in `curses`

---

## 📦 Installation

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/RISHNULAL/Fighter_Jet_Master.git
cd Fighter_Jet_Master
```

---

### 🔹 2. Install Dependencies (Windows Only)

```bash
py -3.12 -m pip install windows-curses
```

(Linux/macOS users do not need this step.)

---

### 🔹 3. Run the Game

```bash
py -3.12 fighter_menu_game.py
```

Or:

```bash
python fighter_menu_game.py
```

---

## 🧠 Game Logic Overview

* Uses `curses` for terminal rendering
* Real-time non-blocking input
* Dynamic obstacle spawning
* Collision detection system
* Timed power-up activation
* Structured modular functions:

  * Menu System
  * Help Screen
  * Game Loop
  * Color Initialization

---

## 🎯 Future Improvements

* ⭐ Level System
* 👾 Boss Fight Mode
* 💾 High Score Saving
* 🌌 Animated Star Background
* 💣 Explosion Animation
* 🛡 Shield Power-up

---

## 👨‍💻 Author

**Rishnu Lal N**
GitHub: https://github.com/RISHNULAL

---



⭐ If you like this project, consider starring the repository!
