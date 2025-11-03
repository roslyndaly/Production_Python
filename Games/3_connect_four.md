# Connect Four Game

## Objective

To create a two-player game of Connect Four, where players take turns dropping colored discs into a vertically suspended grid. The first player to form a horizontal, vertical, or diagonal line of four of their own discs wins the game.

## Requirements

1. **Language**: Python
2. **External Libraries**: None (only Python's standard libraries)

## Game Mechanics

- The game is played on a vertical grid of 6 rows and 7 columns.
- Two players compete, each with a set of colored discs (commonly red and yellow).
- Players alternate turns, dropping one disc into one of the columns on each turn.
- A disc falls to the lowest available space within the selected column.
- The game checks after every turn if a player has achieved four discs in a row - horizontally, vertically, or diagonally.
- The game ends when one player forms a line of four discs or if the board is completely filled (resulting in a draw).

## Features

1. **Game Board Representation**: Implement the board using a two-dimensional list.
2. **Player Turns**: Allow players to choose columns to drop their discs.
3. **Input Validation**: Ensure the selected column is within range and not full.
4. **Win Condition Check**: After each move, check for a winning line of four discs.
5. **Game Loop**: Implement a loop that continues until the game ends either with a win or a draw.
6. **Displaying the Board**: Visually represent the current state of the game board after each move.
7. **Error Handling**: Handle invalid inputs and full column selections.

## User Interface

- Console-based: Interaction with the game is through the command line, with the grid displayed in the console.

## Extension Possibilities

- Implement an AI opponent with varying difficulty levels.
- Create a graphical user interface using Python libraries like Tkinter or Pygame.
- Include features like undo move, replay last game, and save game progress.
