import random

def hangman():
    words = ['python', 'apple', 'hello', 'world', 'code']
    word = random.choice(words)
    guessed = ['_'] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    while attempts > 0 and '_' in guessed:
        print("\nWord:", ' '.join(guessed))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")

    if '_' not in guessed:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

if __name__ == "__main__":
    hangman()