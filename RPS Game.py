import random

# Function to determine the winner for a single round
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Initialize user and computer scores
user_score = 0
computer_score = 0

while True:
    print("Rock, Paper, Scissors Game")
    print("Choose your move: rock, paper, or scissors (or type 'quit' to exit)")
    user_choice = input("Your choice: ").lower()

    if user_choice == "quit":
        break

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Generate computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")
    print()

# Display final scores
print("Final Scores:")
print(f"Your score: {user_score}")
print(f"Computer score: {computer_score}")
print("Thanks for playing!")