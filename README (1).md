# Hangman Game

A simple Hangman game built in two versions:
- `index.html` — browser-based version with a visual keyboard and gallows
- `hangman.py` — Python terminal version

## How to Play

**Browser version:**
1. Open `index.html` in any web browser
2. Click letters or type on your keyboard to guess
3. You have 6 incorrect guesses before game over

**Python version:**
1. Make sure Python 3 is installed
2. Run: `python hangman.py`
3. Type one letter at a time and press Enter

## Words Included

| Word     | Hint                        |
|----------|-----------------------------|
| python   | a programming language 🐍   |
| guitar   | a stringed instrument 🎸    |
| planet   | orbits a star 🪐             |
| jungle   | a dense tropical forest 🌿  |
| wizard   | casts spells ✨              |

## Key Concepts Used

- `random` — picks a word at random each round
- `while loop` — keeps the game going until win or loss
- `if-else` — checks guesses, win/lose conditions
- `strings` — splits and compares word characters
- `lists/sets` — tracks guessed letters
