# 🕹️ Python Retro Game Launcher & Archive by davinciXVII

Welcome to my retro game collection! This project features a custom **Tkinter-based Dashboard Launcher** that allows seamless execution of 9 different Python games. The architecture runs each game as an independent sub-process using the native `subprocess` module, ensuring strict separation of concerns, stable window management, and zero execution conflicts.

## 🚀 Features

- **Centralized Dashboard**: A clean, responsive GUI built with Tkinter to browse and launch games with a single click.
- **Robust Subprocess Architecture**: Games run in their own environments, preventing thread blocks and graphic-engine (`turtle` / `tkinter`) crashes.
- **Cross-Platform Path Handling**: Leverages Python's `os` and `sys` modules to ensure correct absolute directory resolution.
- **Automated Console Spawning**: Seamlessly triggers standard Windows CMD terminal wrapper execution for text-based logic games.

---

## 🎮 The Game Archive

The collection consists of a diverse mix of graphical (GUI) and console-based (CLI) applications developed over my 2-year coding journey:

| Game Title | Engine / UI | Type | Description |
| :--- | :--- | :--- | :--- |
| **Snake** | Turtle Graphics | GUI | Classic arcade snake game with responsive vector movement. |
| **Colors (Stroop Effect)** | Tkinter | GUI | High-speed cognitive training game where you type the color of the text, not the word. |
| **Dice Sim** | Console (CMD) | CLI | A tactical dice betting simulator with dynamic point scaling and x4 multiplier payouts. |
| **Quest** | Console (CMD) | CLI | A text-based choice-driven adventure game with branch-logic paths. |
| **Tic Tac Toe** | Console (CMD) | CLI | Features a smart Artificial Intelligence (AI) logic engine that dynamically blocks player wins. |
| **Battleship** | Tkinter | GUI | Scale-ready 10x10 grid combat with automated map generation, validation arrays, and adaptive AI shooting logs. |
| **Wheel of Fortune** | Console (CMD) | CLI | Word-guessing game featuring dynamic character masking, list management, and input validators. |
| **Arrangement (15-Puzzle)** | Tkinter | GUI | Dynamic board-sizing engine (3x3, 4x4, etc.) featuring tile-shifting index collision tracking and complex victory state validation. |
| **Guess Number** | Tkinter | GUI | Numeric hot/cold guessing interface utilizing conditional loop guidance states. |

---

## 🛠️ Tech Stack & Concepts Applied

- **Language**: Python 3.12+
- **GUI Frameworks**: Tkinter, Turtle Graphics
- **Core Modules**: `subprocess`, `random`, `sys`, `os`, `sys.modules` cache handling
- **Architecture**: Process isolation, Object-Oriented Programming (OOP) via customized Class data representations, conditional branch structures, state mutation validation logic.

---

## 💻 How To Run

1. Clone this repository to your machine.
2. Make sure all game folders are located in the same directory as the main dashboard script.
3. Run the main launcher:
```bash
python main_menu.py
```


