# Classic Snake Game

## Description

This project is a Python-based implementation of the classic Snake Game. The game uses the Python `turtle` module for the UI. The snake is controlled by the arrow keys, and the goal is to eat as much food as possible without colliding with the game border or with the snake's own body. The game keeps track of the current score and the high score, storing the latter between sessions.

## Features

- Classic snake mechanics, with the snake increasing in length each time it eats food.
- The food appears randomly in the game area.
- Collision detection with the game border and the snake's own body.
- Score keeping, with each piece of food increasing the score by one.
- High score tracking between game sessions, stored in a file `snakedata.txt`.

## Structure

The game is divided into four Python files, each representing a different aspect of the game:

- `main.py`: The main game loop. Sets up the game screen and manages the game logic.
- `snake.py`: Defines the `Snake` class. The snake is made up of segments, which are `turtle` objects. Contains methods to control the snake's movement and handle the snake's growth and collisions.
- `food.py`: Defines the `Food` class, which is also a `turtle` object. Each `Food` object appears in a random location within the game area.
- `scoreboard.py`: Defines the `Scoreboard` class, which displays the current score and high score.

## Dependencies

The application uses the following Python libraries:

- [turtle](https://docs.python.org/3/library/turtle.html): For creating the game UI and handling user input.
- [random](https://docs.python.org/3/library/random.html): For positioning food randomly in the game area.
- [time](https://docs.python.org/3/library/time.html): To control the game's refresh rate.

## Usage

To play the game, simply run `main.py`. Use the arrow keys to control the snake. The game ends when the snake collides with the border or with itself. The score resets to zero when the game ends, but the high score is preserved between games.

## Future Enhancements

Some possible improvements to the game might include adding different levels of difficulty, introducing different types of food with varying point values, or adding obstacles in the game area.

## Disclaimer

This project is meant for personal, non-commercial use. The developer is not responsible for any misuse of this game or any violation of terms. Always ensure that your usage of these services complies with their terms of service.
