# 2048 Game – Python (Tkinter)

## Overview

This is a simple implementation of the classic **2048 game** built using **Python** and the **Tkinter GUI framework**. The game follows the traditional 2048 rules: combine tiles with the same value by moving them in one of four directions (up, down, left, right) to reach the **2048** tile.

The game supports:
- A 4x4 grid with dynamic tile generation
- Tile merging with animation updates
- Win and lose conditions
- Intuitive keyboard controls

---

## How to Play

- Use the arrow keys (**↑ ↓ ← →**) to move the tiles.
- When two tiles with the same number touch, they merge into one.
- The goal is to reach the **2048 tile**.
- The game ends when there are no valid moves left.

---

## File Structure

- `main.py` – Contains core game logic including tile movement and game state checks.
- `Constants.py` – Stores all constants used for styling, colors, fonts, grid size, and key mappings.
- `game.py` – Main GUI implementation using `tkinter`. It handles rendering the grid, capturing keyboard input, and updating tile visuals.
- `README.md` – Game instructions and setup guide.

---

## Requirements

- Python 3.x

No external libraries are required apart from the built-in `tkinter` module.

---

## Running the Game

1. Ensure all files (`game.py`, `main.py`, `Constants.py`) are in the same directory.
2. Run the following command in your terminal:

```bash
python game.py
```

---

## Features

- **Smooth UI** with dynamically colored tiles
- **Grid initialization** with two random tiles
- **Mutual tile movement and merging** logic
- **Win/Lose messages** displayed in the grid
- **Separation of concerns** between UI (`game.py`) and logic (`main.py`)

---

## Customization

we can modify the constants in `Constants.py` to:
- Change the grid size (e.g., 5x5 instead of 4x4)
- Adjust colors and fonts
- Modify key mappings

---

## Example Gameplay

```
2048
⬆️  ⬇️  ⬅️  ➡️

2  2  0  0
4  4  2  0
0  2  4  2
0  0  2  2
```

After pressing the Left arrow:
```
4  0  0  0
8  2  0  0
2  4  2  0
4  0  0  0
```

---

## License

This project is open-source and free to use for learning and development purposes.

