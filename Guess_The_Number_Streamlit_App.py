import streamlit as st
import random

st.set_page_config(page_title="Guess The Number Game", page_icon="🎯")

# Initialize session state variables
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "max_attempts" not in st.session_state:
    st.session_state.max_attempts = 10
if "score" not in st.session_state:
    st.session_state.score = st.session_state.max_attempts * 10
if "hint_used" not in st.session_state:
    st.session_state.hint_used = False
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "message" not in st.session_state:
    st.session_state.message = ""
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False

st.title("🎯 Guess The Number Game")
st.write("I'm thinking of a number between 1 and 100.")
st.write(f"You have {st.session_state.max_attempts} attempts to guess it.")

if st.session_state.game_over:
    st.success(st.session_state.message)
    if st.button("Play Again"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.score = st.session_state.max_attempts * 10
        st.session_state.hint_used = False
        st.session_state.game_over = False
        st.session_state.message = ""
        st.session_state.show_hint = False
    st.stop()

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, key="guess_input")
guess_button = st.button("Submit Guess")

if guess_button and not st.session_state.game_over:
    st.session_state.attempts += 1
    remaining_attempts = st.session_state.max_attempts - st.session_state.attempts

    if guess < st.session_state.secret_number:
        st.info("📉 Too low!")
    elif guess > st.session_state.secret_number:
        st.info("📈 Too high!")
    else:
        st.session_state.score = (st.session_state.max_attempts - st.session_state.attempts) * 10
        if st.session_state.hint_used:
            st.session_state.score -= 5
        st.session_state.message = f"🎉 Congratulations! You guessed the number {st.session_state.secret_number} in {st.session_state.attempts} attempts.\n🏆 Your score: {max(st.session_state.score, 0)}"
        st.session_state.game_over = True
        st.stop()

    # Hint system after 5th attempt
    if st.session_state.attempts == 5 and not st.session_state.hint_used:
        st.session_state.show_hint = True

    if remaining_attempts > 0 and not st.session_state.game_over:
        st.write(f"🔄 Attempts left: {remaining_attempts}")
    elif not st.session_state.game_over:
        st.session_state.message = f"❌ Game Over! The correct number was {st.session_state.secret_number}.\n😢 Better luck next time!"
        st.session_state.game_over = True
        st.stop()

# Show hint if eligible
if st.session_state.show_hint and not st.session_state.hint_used and not st.session_state.game_over:
    st.warning("⚠️ If you use a hint, your score will be reduced by 5 points.")
    if st.button("💡 Use Hint"):
        st.session_state.hint_used = True
        st.session_state.score -= 5
        st.info("⚠️ Hint used! -5 points.")

        # Hint 1: Even or Odd
        if st.session_state.secret_number % 2 == 0:
            st.info("🤔 Hint 1: The number is EVEN.")
        else:
            st.info("🤔 Hint 1: The number is ODD.")

        # Hint 2: Range hint
        lower_bound = (st.session_state.secret_number // 10) * 10
        upper_bound = min(lower_bound + 10, 100)
        st.info(f"📏 Hint 2: The number is between {lower_bound} and {upper_bound}.")

        # Hint 3: Divisibility or Multiple Hint
        if st.session_state.secret_number % 5 == 0:
            st.info("➗ Hint 3: The number is divisible by 5.")
        elif st.session_state.secret_number % 10 == 0:
            st.info("➗ Hint 3: The number is divisible by 10.")
        else:
            multiples = [n for n in [3, 4, 7] if st.session_state.secret_number % n == 0]
            if multiples:
                st.info(f"➗ Hint 3: The number is a multiple of {', '.join(map(str, multiples))}.")
            else:
                st.info("➗ Hint 3: The number is NOT a multiple of 3, 4, or 7.")

        st.session_state.show_hint = False

st.sidebar.title("About")
st.sidebar.markdown("""
- 🎯 **Guess The Number Game**: Try to guess the secret number between 1 and 100.
- 🕹️ You have 10 attempts.
- 💡 Use hints (with a score penalty) after 5 attempts.
- 🏆 Score is based on attempts and hint usage.

**Author:** Mohanraj Velayutham  
[GitHub](https://github.com/mohanraj9342)
""")