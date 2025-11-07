import streamlit as st
import random

def play_round(user_move):
    """
    Executes one round of the game, updates scores, and checks for a winner.
    This implements the "Human vs Al Bot" setup .
    """
    
    # The "Al Bot" generates its move computationally 
    computer_move = random.choice(["Rock", "Paper", "Scissors"])
    
    result = "Draw"
    
    # Implement the decision matrix 
    if user_move == computer_move:
        result = "Draw" # 
    elif (user_move == "Rock" and computer_move == "Scissors") or \
         (user_move == "Scissors" and computer_move == "Paper") or \
         (user_move == "Paper" and computer_move == "Rock"):
        result = "You Win" # 
        st.session_state.user_score += 1 # 
    else:
        result = "AI Wins" # 
        st.session_state.computer_score += 1 # 
        
    # Update state
    st.session_state.last_result = result
    st.session_state.user_move_display = user_move
    st.session_state.computer_move_display = computer_move
    
    # Check for winning condition: "The first player to reach three wins" 
    if st.session_state.user_score == 3 or st.session_state.computer_score == 3:
        st.session_state.game_over = True

def reset_game():
    """
    Resets all session state variables for a new game.
    """
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.game_over = False
    st.session_state.last_result = "N/A"
    st.session_state.user_move_display = "N/A"
    st.session_state.computer_move_display = "N/A"