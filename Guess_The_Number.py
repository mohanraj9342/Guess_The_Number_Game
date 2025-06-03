import random

def play_game():
    while True:
        secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 10
        score = max_attempts * 10  # Max possible score = 100
        hint_used = False

        print("\n🎯 Welcome to the Guess the Number game!")
        print("I'm thinking of a number between 1 and 100.")
        print(f"You have {max_attempts} attempts to guess it.")

        while attempts < max_attempts:
            try:
                guess = int(input("\nEnter your guess: "))
                if guess < 1 or guess > 100:
                    print("🚫 Please enter a number between 1 and 100.")
                    continue
            except (ValueError, EOFError):
                print("🚫 Invalid input! Please enter a valid number.")
                continue

            attempts += 1
            remaining_attempts = max_attempts - attempts

            if guess < secret_number:
                print("📉 Too low!")
            elif guess > secret_number:
                print("📈 Too high!")
            else:
                print(f"\n🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                score = (max_attempts - attempts) * 10
                if hint_used:
                    score -= 5  # Correct score after hint deduction
                print(f"🏆 Your score: {max(score, 0)}")
                break

            # ✅ HINT SYSTEM after 5th attempt
            if attempts == 5 and not hint_used:
                print("\n⚠️ WARNING: If you use a hint, your score will be reduced by 5 points.")
                give_hint = input("💡 You've had 5 tries. Do you want a hint? (y/n): ").strip().lower()
                if give_hint == 'y':
                    hint_used = True
                    score -= 5  # Deduct 5 points for using a hint
                    print("⚠️ Hint used! -5 points.")

                    # ✅ Hint 1: Even or Odd
                    if secret_number % 2 == 0:
                        print("🤔 Hint 1: The number is EVEN.")
                    else:
                        print("🤔 Hint 1: The number is ODD.")

                    # ✅ Hint 2: Range hint
                    lower_bound = (secret_number // 10) * 10
                    upper_bound = min(lower_bound + 10, 100)
                    print(f"📏 Hint 2: The number is between {lower_bound} and {upper_bound}.")

                    # ✅ Hint 3: Divisibility or Multiple Hint
                    if secret_number % 5 == 0:
                        print("➗ Hint 3: The number is divisible by 5.")
                    elif secret_number % 10 == 0:
                        print("➗ Hint 3: The number is divisible by 10.")
                    else:
                        multiples = [n for n in [3, 4, 7] if secret_number % n == 0]
                        if multiples:
                            print(f"➗ Hint 3: The number is a multiple of {', '.join(map(str, multiples))}.")
                        else:
                            print("➗ Hint 3: The number is NOT a multiple of 3, 4, or 7.")

            if remaining_attempts > 0:
                print(f"🔄 Attempts left: {remaining_attempts}")
            else:
                print(f"\n❌ Game Over! The correct number was {secret_number}.")
                print("😢 Better luck next time!")

        play_again = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\n👋 Thanks for playing! Goodbye!")
            break

# ✅ Start the game
if __name__ == "__main__":
    play_game()
