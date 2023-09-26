import random

# List of words for the game
word_list = ["apple", "banana", "cherry", "dog", "elephant", "flamingo", "giraffe", "hamburger", "icecream", "jacket"]

def choose_random_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def display_hangman(incorrect_guesses):
    hangman_art = [
        """
         _____
        |     |
              |
              |
              |
              |
        """,
        """
         _____
        |     |
        O     |
              |
              |
              |
        """,
        """
         _____
        |     |
        O     |
        |     |
              |
              |
        """,
        """
         _____
        |     |
        O     |
       /|     |
              |
              |
        """,
        """
         _____
        |     |
        O     |
       /|\    |
              |
              |
        """,
        """
         _____
        |     |
        O     |
       /|\    |
       /      |
              |
        """,
        """
         _____
        |     |
        O     |
       /|\    |
       / \    |
              |
        """
    ]
    return hangman_art[incorrect_guesses]

def hangman():
    word_to_guess = choose_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = len(word_to_guess) + 3  # You can adjust this as needed

    print("Welcome to Hangman!")

    while True:
        print(display_hangman(incorrect_guesses))
        print(display_word(word_to_guess, guessed_letters))

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You've won!")
            break

        if incorrect_guesses >= max_attempts:
            print("Sorry, you've run out of attempts. The word was:", word_to_guess)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            incorrect_guesses += 1

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()

hangman()

