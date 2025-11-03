
# Battleships

## Objective

To create a digital version of the classic [Battleship]((https://en.wikipedia.org/wiki/Battleship_(game))) game, where players place a set of ships on a grid and take turns guessing the locations of the opponent's ships. The first player to sink all of the opponent's ships wins.

## Game Mechanics

- The game is played on two grids per player: one for their own ships and one for recording guesses against the opponent.
- Each player has a set of ships of varying lengths to place on their grid horizontally or vertically.
- Players take turns to guess coordinates on the opponent's grid in an attempt to "hit" their ships.
- A hit is marked on the guess grid, and the player is informed. A miss is also marked.
- The game continues until one player sinks all the opponent's ships.

## Features

1. **Grid Representation**: Implement two grids per player using two-dimensional lists.
2. **Ship Placement**: Allow players to place their ships on their grid in random or user-defined locations.
3. **Turn-Based Gameplay**: Players take turns guessing the location of the opponent's ships.
4. **Hit and Miss Tracking**: Track and display hits and misses on the guess grid.
5. **Win Condition Check**: Determine when all ships of a player have been sunk.
6. **Game Loop**: Create a main game loop that continues until the game ends.
7. **Displaying the Grids**: Visually represent both the player's ship grid and the guess grid after each turn.
8. **Error Handling**: Manage invalid inputs, such as repeating guesses or placing ships out of bounds.

## User Interface

- Console-based: Interaction with the game is through the command line, with grids displayed in the console.

## Extension Possibilities

- Implement an AI opponent for single-player mode.
- Create a graphical user interface (GUI) using Python libraries like Tkinter or Pygame.
- Enable different ship sizes and customizable layouts.
- Hiding moves between players
  - Either a handover screen could be shown between player turns to avoid either player seeing the opponent's grid.
  - Or, the past turns should be cleared in the terminal window to avoid an opponent scrolling up.
