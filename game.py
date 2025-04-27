import streamlit as st
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return 'You win!'
    else:
        return 'You lose!'

st.title('Rock Paper Scissors Game')


user_choice = st.radio('Choose your move:', ['Rock', 'Paper', 'Scissors'])

if st.button('Play'):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    result = determine_winner(user_choice, computer_choice)

    st.write(f'Your choice: {user_choice}')
    st.write(f'Computer\'s choice: {computer_choice}')
    st.write(result)
