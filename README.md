# Crossing-game
This is a classic arcade-style game built with Python's `turtle` module, inspired by Frogger. The player controls a turtle trying to cross a busy street full of moving cars. With each successful crossing, the game gets harder. Reach the top, dodge traffic, and survive as long as you can!

## 🎮 How to Play

- Press **Up Arrow** to move the turtle forward.
- Cars are generated at random y-positions and drive from right to left.
- Reach the top of the screen to level up. Each level increases the speed of the cars.
- Colliding with a car ends the game with a **"GAME OVER"** screen.

---

## 🛠️ Features

- Smooth car movement and spawning
- Progressive difficulty with each level (up to Level 5)
- Game over detection with clean screen message
- Modular design using OOP: `Player`, `CarManager`, `Scoreboard`

---

## 🗂️ File Structure

- `main.py` - Sets up the game loop, input, and collision logic.
- `player.py` - Manages turtle movement and finish-line detection.
- `car_manager.py` - Generates and moves cars, handles difficulty.
- `scoreboard.py` - Displays and updates the current level, and handles game over state.
- 'images' - contains a bunch of image to show the template


## 🚀 Requirements

- Python 3.7+
- No external dependencies (pure `turtle` module)

> You can run the game by simply executing:
python main.py
📚 Learning Objectives
This project demonstrates:

Object-Oriented Programming in Python

Event-driven programming using onkey and Screen.listen()

Randomized sprite generation

Basic game design principles using Python’s built-in libraries

📌 Author
Created with Like-Supreme
