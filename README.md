# brain-buster
This project is a simple console-based memory game written in Python. The game challenges players to test their memory by uncovering hidden pairs of integers on a grid. The main features include:

Interactive: Players guess cell pairs to uncover hidden numbers and match them to score points.

Scalable Grid Sizes: Supports 2x2, 4x4, and 6x6 grids for varying levels of difficulty.

Dynamic Scoring System: Scores players based on the efficiency of their guesses relative to the minimum required. If players want to cheat and reveal single cells, that is considered as well.

Error Handling: Ensures robust input validation for grid size, menu options, and cell selections.


There are 2 files:
game.py handles user interface, menu navigation and game logic
grid.py handles the grid structure and the methods for the game mechanics

The project only relies on Python Libraries


Usage:
To play the game, run this command in your terminal by replacing <grid_size> with 2, 4 or 6:

python3 game.py <grid_size>
