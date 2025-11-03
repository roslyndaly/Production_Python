# Dots and Boxes Game

## Objective

To create a two-player [Dots and Boxes](https://en.wikipedia.org/wiki/Dots_and_boxes) game where players take turns drawing lines between dots on a grid, aiming to complete the fourth side of a 1×1 box. Each completed box earns a point, and the player with the most points at the end wins.

## Game Mechanics

- The game board consists of a grid of dots (e.g., 5x5 dots).
- Two players take turns to draw a single horizontal or vertical line between two unjoined adjacent dots.
- A player scores a point and takes another turn if they complete the fourth side of a 1×1 box.
- The game continues until all boxes are created (i.e., no more lines can be drawn).
- The winner is the player with the most boxes completed.

## Features

1. **Game Board Representation**: Implement a grid of dots and track the lines drawn and boxes completed.
2. **Player Turns**: Alternate turns between players, allowing them to draw lines.
3. **Input Validation**: Ensure the players' input corresponds to a valid and unoccupied line position.
4. **Scoring System**: Implement a scoring system that awards points for box completion.
5. **Game Loop**: Maintain the main game loop, continuing until all possible lines are drawn.
6. **Displaying the Board**: Display the current state of the game board, including drawn lines and completed boxes, after each turn.
7. **Error Handling**: Handle invalid inputs and ensure that lines are drawn correctly.

## User Interface

- Console-based: Interaction with the game is through the command line, with the board displayed in the console.

## Extension Possibilities

- Implement an AI opponent with basic strategy.
- Create a graphical user interface (GUI) using libraries like Tkinter or Pygame.
- Offer different grid sizes for varied gameplay.
- Implement a "hint" feature that suggests possible moves.
