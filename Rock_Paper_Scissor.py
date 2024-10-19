import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", page_icon="✊✋✌️", layout="centered")

# Initialize session state for tracking score
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'computer_score' not in st.session_state:
    st.session_state.computer_score = 0

# Custom CSS for vibrant, fun interface
st.markdown("""
    <style>
    body {
        background-color: #e0f7fa;
    }
    .title {
        font-size: 40px;
        color: #00796b;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .big-font {
        font-size: 30px !important;
        color: #0288d1;
        font-weight: bold;
    }
    .score-font {
        font-size: 24px !important;
        font-weight: bold;
        color: #ff9800;
        text-align: center;
    }
    .button {
        background-color: #4caf50;
        color: white;
        font-size: 22px;
        padding: 10px;
        border-radius: 12px;
        width: 100%;
        margin: 5px;
        transition: 0.3s;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
    }
    .button:hover {
        transform: scale(1.1);
        background-color: #388e3c;
    }
    .result-font {
        font-size: 28px !important;
        color: #d32f2f;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .footer {
        text-align: center;
        font-size: 18px;
        color: #808080;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and instructions
st.markdown("<div class='title'>🎉 Rock Paper Scissors Game 🎉</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Choose your move and challenge the computer! Best of luck!</p>", unsafe_allow_html=True)

# User choices
choices = ['Rock', 'Paper', 'Scissors']
emojis = {'Rock': '✊', 'Paper': '✋', 'Scissors': '✌️'}

# Score display
st.markdown(f"<p class='score-font'>Your Score: {st.session_state.user_score} | Computer Score: {st.session_state.computer_score}</p>", unsafe_allow_html=True)

# Display fun buttons for choices
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('✊ Rock'):
        user_choice = 'Rock'
with col2:
    if st.button('✋ Paper'):
        user_choice = 'Paper'
with col3:
    if st.button('✌️ Scissors'):
        user_choice = 'Scissors'

# Game logic
if 'user_choice' in locals():
    st.markdown(f"<p class='big-font'>You chose: {emojis[user_choice]}</p>", unsafe_allow_html=True)
    computer_choice = random.choice(choices)
    st.markdown(f"<p class='big-font'>Computer chose: {emojis[computer_choice]}</p>", unsafe_allow_html=True)

    # Determine the result and update score
    if user_choice == computer_choice:
        result = "It's a Tie! 🤝"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You Win! 🎉"
        st.session_state.user_score += 1
    else:
        result = "You Lose! 😔"
        st.session_state.computer_score += 1

    st.markdown(f"<p class='result-font'>{result}</p>", unsafe_allow_html=True)

# Footer message
st.markdown("<div class='footer'>Can you reach 5 points before the computer does? 🔥</div>", unsafe_allow_html=True)

# Reset score button
if st.button('Reset Scores'):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
