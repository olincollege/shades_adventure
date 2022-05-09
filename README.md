# Shades' Adventure: The Game

This is the repository for the game *Shades' Adventure*, created by Evan Lockwood and Mateo Macias.

## Installation and Setup

The main installation required for this project is conda python (3.8). You can install it using this link: 

Pygame is also required to run the game. You can install this library by typing into your terminal:
```
pip install pygame
```

## File Structure

The file structure for this project consists of the following .py files:
- `game.py` contains the method `main` that runs the game. Run this file to play the game.
- `fighter.py` contains the class `Fighter` that gives each character their attributes.
- `game_view.py` contains the class `GameView`, which is used for anything that is displayed in the game.
- `button_controls.py` contains the class `Button`. This is used to track where the mouse is on the screen as well as what area it clicks.
- `test_game.py` is used to test all testable methods used in our code.

The repository also contains a `/img` folder that contains all visuals used in the project.

## Run the Game

To run the game, either run the file `game.py` or type into your terminal:
```
python game.py
```

## Website

Visit our website [here](https://olincollege.github.io/shades_adventure/).