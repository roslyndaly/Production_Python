
# Tic-Tac-Toe

## Objective

To create a two-player Tic-Tac-Toe game in Python, where players take turns to mark spaces in a 3x3 grid, attempting to place three of their marks in a horizontal, vertical, or diagonal row.

## Game Mechanics

- The game board is a 3x3 grid, typically represented using a two-dimensional array.
- Two players participate in the game, usually one being 'X' and the other 'O'.
- Players take turns to place their mark ('X' or 'O') in an empty cell of the grid.
- The game checks after every turn if there is a winner.
- The game ends when one player aligns three of their marks in a horizontal, vertical, or diagonal row or if all cells are filled (resulting in a tie).

## Features

1. **Game Board Representation**: Implement a 3x3 grid using a two-dimensional list.
2. **Player Turns**: Alternate turns between players, allowing them to place their mark on the board.
3. **Input Validation**: Ensure the players' input corresponds to an empty cell in the grid.
4. **Win Condition Check**: After each turn, check for a win condition or a tie.
5. **Game Loop**: Implement the main game loop, which continues until the game ends.
6. **Displaying the Board**: Visually represent the current state of the game board after each turn.
7. **Error Handling**: Handle scenarios like invalid inputs or out-of-bound moves.

## User Interface

- Console-based: Interaction with the game is through the command line, with the grid displayed in the console.

## Extension Possibilities

- Implement an AI opponent using basic algorithms.
- Add a graphical user interface (GUI) using libraries like Tkinter or Pygame.
- Include options to choose symbols and restart the game.
- Implement a score tracking system.
