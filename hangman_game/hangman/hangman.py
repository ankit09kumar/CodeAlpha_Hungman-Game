import random

WORDS = [
    {"word": "python", "hint": "a programming language"},
    {"word": "guitar", "hint": "a stringed instrument"},
    {"word": "planet", "hint": "orbits a star"},
    {"word": "jungle", "hint": "a dense tropical forest"},
    {"word": "wizard", "hint": "casts spells"},
]

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]

MAX_WRONG = 6


def display_word(word, guessed):
    return " ".join(ch if ch in guessed else "_" for ch in word)


def play():
    choice = random.choice(WORDS)
    word = choice["word"]
    hint = choice["hint"]

    guessed = set()
    wrong_count = 0

    print("\n" + "=" * 40)
    print("       W E L C O M E  T O  H A N G M A N")
    print("=" * 40)

    while wrong_count < MAX_WRONG:
        print(HANGMAN_STAGES[wrong_count])
        print(f"\nHint: {hint}")
        print(f"\nWord: {display_word(word, guessed)}")

        wrong_letters = sorted(ch for ch in guessed if ch not in word)
        if wrong_letters:
            print(f"Wrong guesses: {', '.join(wrong_letters)}")

        remaining = MAX_WRONG - wrong_count
        print(f"Incorrect guesses remaining: {remaining}")

        # Check win
        if all(ch in guessed for ch in word):
            print(f"\n🎉 You won! The word was: {word}")
            return

        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print(f"✅ '{guess}' is in the word!")
        else:
            wrong_count += 1
            print(f"❌ '{guess}' is not in the word.")

    # Game over
    print(HANGMAN_STAGES[MAX_WRONG])
    print(f"\n💀 Game over! The word was: {word}")


def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
