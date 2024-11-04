import streamlit as st
import random
st.title("Guessing Game")
st.title("Guess the Secret Number!")
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
user_guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)
if st.button("Guess"):
    st.session_state.attempts += 1
    if user_guess < st.session_state.number:
        st.write("Your guess is too low. Try again!")
    elif user_guess > st.session_state.number:
        st.write("Your guess is too high. Try again!")
    else:
        st.write(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
        # Reset the game
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.write("A new number has been generated. Start guessing!")