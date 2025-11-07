import streamlit as st
from streamlit_webrtc import webrtc_streamer

# --- Import our custom modules ---
from video_processor import RpsTransformer
from game_logic import play_round, reset_game

# --- App Title and Credits ---
st.title("Human Pose Estimation for RPS")
st.write("By: Nicolei Faith Abot and Adlei Jed Tan") # 
st.write("---")

# --- Initialize session state for game logic ---
# This ensures variables persist between button clicks
if 'user_score' not in st.session_state:
    reset_game() # Use the function from our module

# --- Webcam Feed ---
ctx = webrtc_streamer(
    key="rps",
    video_transformer_factory=RpsTransformer,
    media_stream_constraints={"video": True, "audio": False},
)

# --- Game Control Buttons ---
col1, col2 = st.columns(2)
with col1:
    if st.button("Play Round"):
        if not st.session_state.game_over:
            if ctx.video_transformer:
                user_move = ctx.video_transformer.user_move
                if user_move != "None":
                    play_round(user_move) # Call game logic
                else:
                    st.warning("Show your hand clearly in the camera!")
            else:
                st.error("Webcam is not ready.")
        else:
            st.warning("Game is over. Please start a New Game.")

with col2:
    if st.button("New Game"):
        reset_game() # Call game logic
        st.rerun()

# --- Score and Result Display ---
st.header(f"Score: You ({st.session_state.user_score}) - AI ({st.session_state.computer_score})")
st.write(f"**First to 3 wins!**") # 
st.write("---")
st.subheader(f"Round Result: {st.session_state.last_result}")
st.write(f"You Played: **{st.session_state.user_move_display}**")
st.write(f"AI Played: **{st.session_state.computer_move_display}**")

# --- Game Over Message ---
if st.session_state.game_over:
     winner = "You" if st.session_state.user_score == 3 else "The AI"
     st.success(f"**Game Over! {winner} won the best-of-five!**") #