# Hangman Word Guessing Game

## Overview
This is a Python-based Hangman-style word guessing game. The game randomly selects a word from a file (`wordbank.txt`), and the player must guess the word within a limited number of attempts.

## How It Works
1. The game reads words from `wordbank.txt` and picks one randomly.
2. The player is given 10 attempts to guess the word, letter by letter.
3. If a guessed letter is correct, it is revealed in the word.
4. If a guessed letter is incorrect, an attempt is deducted.
5. The game ends when the player either guesses the entire word (win) or runs out of attempts (lose).

## Features
- Reads words from an external file (`wordbank.txt`).
- Prevents duplicate guesses.
- Displays the current state of the word after each guess.
- Shows wrong guesses separately.
- Simple text-based interface.

## Prerequisites
- Python 3.x installed on your system.
- A `wordbank.txt` file containing a list of words (one per line).

## How to Run the Game
1. Ensure Python is installed on your system.
2. Save the script as `hangman.py`.
3. Place `wordbank.txt` in the same directory as the script.
4. Open a terminal or command prompt and run:
   ```sh
   python hangman.py
   ```

## Example of `wordbank.txt`
```
python
java
javascript
ruby
csharp
swift
kotlin
php
html
css
C++
SQL
bash
perl
go
rust
haskell
typescript
```

## Future Enhancements
- Implement difficulty levels (easy, medium, hard).
- Add a graphical interface using Tkinter.
- Allow multi-word phrases as guesses.

## License
This project is open-source and available for modification and redistribution.

Enjoy the game! 🎉

