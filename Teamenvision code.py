"""
Number Guessing Game
--------------------
The computer randomly chooses a number between 1 and 100.
Your task is to guess the number in as few attempts as possible.
After each guess, you'll get hints ("Too High" / "Too Low").
The game ends when you guess correctly.
You can play multiple rounds, and your best score (fewest attempts) is tracked.

How to Play:
1. Run the program.
2. Enter your guesses when prompted.
3. Type 'exit' anytime to quit the game.
"""

import random

def get_valid_guess():
    """Prompt the user for a valid guess and handle errors."""
    while True:
        user_input = input("Enter your guess (1-100) or type 'exit' to quit: ").strip()
        if user_input.lower() == "exit":
            return "exit"
        if user_input.isdigit():
            guess = int(user_input)
            if 1 <= guess <= 100:
                return guess
        print("❌ Invalid input! Please enter a number between 1 and 100 or 'exit'.")

def play_game():
    """Play one round of the Number Guessing Game."""
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("\n🎯 I have chosen a number between 1 and 100. Try to guess it!")

    while True:
        guess = get_valid_guess()
        if guess == "exit":
            print("👋 Exiting game...")
            return None  # player quit

        attempts += 1

        if guess < number_to_guess:
            print("⬇️ Too Low! Try again.")
        elif guess > number_to_guess:
            print("⬆️ Too High! Try again.")
        else:
            print(f"✅ Correct! You guessed it in {attempts} attempts.")
            return attempts

def main():
    """Main function to run the game with replay and high score tracking."""
    print("===== Welcome to the Number Guessing Game =====")
    high_score = None

    while True:
        attempts = play_game()
        if attempts is None:  # player chose to exit
            break

        # Track high score
        if high_score is None or attempts < high_score:
            high_score = attempts
            print(f"🏆 New High Score: {high_score} attempts!")

        # Ask if player wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("👋 Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
