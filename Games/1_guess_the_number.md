# Guess the Number Game

## Objective

To create a simple, interactive game where the user attempts to guess a randomly generated number within a certain range.

## Game Mechanics

- The game generates a random number between 1 and 100 at the start.
- The user is prompted to enter a guess for the number.
- The program provides feedback on each guess:
  - If the guess is lower than the target number, display "Too low, try again."
  - If the guess is higher than the target number, display "Too high, try again."
  - If the guess is correct, display a congratulatory message along with the number of attempts it took.

## Features

1. **Random Number Generation**: Utilize Python's `random` library to generate a random number between 1 and 100.
2. **User Input and Validation**: Capture user input and ensure it's a valid integer. If not, prompt the user again.
3. **Control Flow**: Implement a loop that continues until the user guesses the correct number.
4. **User Feedback**: Provide real-time feedback to the user after each guess.
5. **Count Attempts**: Keep track of the number of attempts the user makes before successfully guessing the number.
6. **Error Handling**: Handle any errors or exceptions, such as non-integer inputs.

## User Interface

- Console-based: The user interacts with the game via standard input (keyboard) and output (console).
- Game should be runnable either by running a single python file or a single jupyter notebook cell.

## Extension Possibilities

- Add difficulty levels (e.g. change the range of numbers).
- Limit the number of attempts.
- Implement a scoring system based on the number of attempts.
