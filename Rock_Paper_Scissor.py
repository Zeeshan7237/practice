import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors Game", page_icon="✊✋✌️", layout="centered")

# Add custom CSS for fun animations and colorful interface
st.markdown("""
    <style>
    body {
        background-color: #fffbe7;
    }
    .big-font {
        font-size: 30px !important;
        font-weight: bold;
        color: #1f7a8c;
    }
    .button {
        background-color: #ffcccb;
        color: white;
        font-size: 20px;
        padding: 10px;
        border-radius: 10px;
        width: 200px;
        margin: 5px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        transition: 0.3s;
    }
    .button:hover {
        transform: scale(1.1);
        background-color: #ff6347;
    }
    .result-font {
        font-size: 28px !important;
        color: #d35400;
        font-weight: bold;
        animation: pulse 1s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 18px;
        color: #808080;
        animation: bounce 2s infinite;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎉 Let's Play Rock Paper Scissors! 🎮")
st.subheader("Choose wisely and let's see who wins!")

# User choices
choices = ['Rock', 'Paper', 'Scissors']

# Display animated buttons for choices
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

    # Determine the result with animations for fun
    if user_choice == computer_choice:
        result = "It's a Tie! 🤝"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You Win! 🎉"
    else:
        result = "You Lose! 😔"

    st.markdown(f"<p class='result-font'>{result}</p>", unsafe_allow_html=True)

# Footer with bouncing animation
st.markdown("""
    <div class="footer">
    <p>Had fun? Click a button to play again! 🎮</p>
    </div>
    """, unsafe_allow_html=True)
