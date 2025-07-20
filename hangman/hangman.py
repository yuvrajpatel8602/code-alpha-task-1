import random

# Predefined words
words = ['apple', 'mango', 'banana', 'guava', 'orange']
word = random.choice(words)
guesses = ''
turns = 6

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_', end=' ')
            failed += 1
    if failed == 0:
        print("\nYou Won!")
        break
    guess = input("\nGuess a letter: ").lower()
    guesses += guess
    if guess not in word:
        turns -= 1
        print(f"\nWrong! Turns left: {turns}")
    if turns == 0:
        print(f"\nYou Lost! The word was: {word}")