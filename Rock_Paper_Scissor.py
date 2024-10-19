import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors Game", page_icon="✊✋✌️", layout="centered")

# Define the styles for a vibrant interface
st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #1e90ff;
    }
    .button {
        background-color: #1e90ff;
        color: white;
        font-size: 20px;
        padding: 10px;
        border-radius: 10px;
        width: 200px;
        margin: 5px;
    }
    .result-font {
        font-size: 24px !important;
        color: #ff6347;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎮 Rock Paper Scissors Game!")
st.subheader("Make your choice:")

# User choices
choices = ['Rock', 'Paper', 'Scissors']

# Display vibrant buttons for choices
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('✊ Rock', key="rock"):
        user_choice = 'Rock'
with col2:
    if st.button('✋ Paper', key="paper"):
        user_choice = 'Paper'
with col3:
    if st.button('✌️ Scissors', key="scissors"):
        user_choice = 'Scissors'

if 'user_choice' in locals():
    st.markdown(f"<p class='big-font'>You chose: {user_choice}</p>", unsafe_allow_html=True)
    computer_choice = random.choice(choices)
    st.markdown(f"<p class='big-font'>Computer chose: {computer_choice}</p>", unsafe_allow_html=True)

    # Determine the result
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You Win! 🎉"
    else:
        result = "You Lose! 😔"

    st.markdown(f"<p class='result-font'>{result}</p>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 50px;'>
    <p style='font-size: 18px; color: #808080;'>Enjoyed the game? Play again!</p>
    </div>
    """, unsafe_allow_html=True)
