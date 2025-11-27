import streamlit as st
import time
import random
from streamlit_webrtc import webrtc_streamer, RTCConfiguration

# --- Import our custom modules ---
from video_processor import RpsTransformer
from game_logic import play_round, reset_game

# --- VIBRANT STYLING SYSTEM ---
st.markdown("""
<style>
    /* ========== COLOR PALETTE & THEME ========== */
    :root {
        --primary-bg: #0E1117;
        --secondary-bg: #1E2530;
        --accent-cyan: #00D9FF;
        --accent-magenta: #FF006E;
        --success-green: #00FF88;
        --text-white: #FFFFFF;
    }
    
    /* Main background */
    .stApp {
        background-color: var(--primary-bg);
        color: var(--text-white);
    }
    
    /* Secondary backgrounds */
    .stMarkdown, .stButton, .stHeader {
        color: var(--text-white);
    }
    
    /* ========== BUTTON STYLING ========== */
    .stButton > button {
        background: linear-gradient(135deg, var(--accent-cyan) 0%, var(--accent-magenta) 100%);
        color: var(--text-white);
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(0, 217, 255, 0.3);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        transform: scale(1.05) translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 217, 255, 0.5), 
                    0 4px 15px rgba(255, 0, 110, 0.3);
        filter: brightness(1.2);
    }
    
    .stButton > button:active {
        transform: scale(0.98);
    }
    
    /* ========== CARD CONTAINERS ========== */
    .custom-card {
        background: linear-gradient(145deg, #1E2530 0%, #262D3D 100%);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4),
                    0 0 20px rgba(0, 217, 255, 0.1);
        border: 1px solid rgba(0, 217, 255, 0.2);
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .custom-card:hover {
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5),
                    0 0 30px rgba(0, 217, 255, 0.2);
        transform: translateY(-4px);
    }
    
    /* ========== SCORE DISPLAY ========== */
    .score-header {
        background: linear-gradient(90deg, var(--accent-cyan), var(--accent-magenta));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5rem;
        font-weight: 800;
        text-align: center;
        margin: 1.5rem 0;
        text-shadow: 0 0 30px rgba(0, 217, 255, 0.5);
    }
    
    /* ========== RESULT DISPLAY ========== */
    .result-box {
        background: rgba(0, 217, 255, 0.1);
        border-left: 4px solid var(--accent-cyan);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    .win-text {
        color: var(--success-green);
        font-weight: 700;
        font-size: 1.3rem;
        text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
    }
    
    .lose-text {
        color: var(--accent-magenta);
        font-weight: 700;
        font-size: 1.3rem;
        text-shadow: 0 0 10px rgba(255, 0, 110, 0.5);
    }
    
    /* ========== HEADERS ========== */
    h1 {
        background: linear-gradient(135deg, var(--accent-cyan), var(--accent-magenta));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 900;
        text-align: center;
        font-size: 3rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    h2 {
        color: var(--accent-cyan);
        font-weight: 700;
        text-shadow: 0 0 20px rgba(0, 217, 255, 0.3);
    }
    
    h3 {
        color: var(--text-white);
        font-weight: 600;
    }
    
    /* ========== DIVIDERS ========== */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, 
            transparent, 
            var(--accent-cyan), 
            var(--accent-magenta), 
            transparent);
        margin: 2rem 0;
    }
    
    /* ========== WARNING/SUCCESS MESSAGES ========== */
    .stAlert {
        border-radius: 12px;
        border-left: 4px solid var(--accent-cyan);
    }
    
    /* ========== GLOW EFFECT ========== */
    .glow {
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from {
            text-shadow: 0 0 5px var(--accent-cyan), 
                         0 0 10px var(--accent-cyan);
        }
        to {
            text-shadow: 0 0 10px var(--accent-cyan), 
                         0 0 20px var(--accent-cyan),
                         0 0 30px var(--accent-magenta);
        }
    }
</style>
""", unsafe_allow_html=True)

# --- App Title and Credits ---
st.markdown("<h1>🎮 Human Pose Estimation for RPS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1rem; color: #888;'>By: Nicolei Faith Abot and Adlei Jed Tan</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Initialize session state for game logic ---
# This ensures variables persist between button clicks
if 'user_score' not in st.session_state:
    reset_game() # Use the function from our module

# --- Initialize timer and round state ---
if 'timer_active' not in st.session_state:
    st.session_state.timer_active = False
if 'end_time' not in st.session_state:
    st.session_state.end_time = 0.0
if 'countdown_result' not in st.session_state:
    st.session_state.countdown_result = "Waiting..."
if 'captured_user_move' not in st.session_state:
    st.session_state.captured_user_move = "N/A"
if 'captured_ai_move' not in st.session_state:
    st.session_state.captured_ai_move = "N/A"

# ========== HEADS-UP DISPLAY (HUD) - ALWAYS AT TOP ==========
st.markdown("<h2 style='text-align: center; margin-bottom: 1rem; margin-top: 0;'>🎯 Game Status HUD</h2>", unsafe_allow_html=True)
hud_col1, hud_col2, hud_col3 = st.columns(3)

with hud_col1:
    # Calculate time remaining
    if st.session_state.timer_active:
        time_remaining = max(0, st.session_state.end_time - time.time())
        timer_display = f"{time_remaining:.1f}s"
        timer_delta = "⏱️ Counting..."
    else:
        timer_display = "Ready"
        timer_delta = "⏸️ Standby"
    
    st.metric(
        label="⏰ Time Remaining",
        value=timer_display,
        delta=timer_delta
    )

with hud_col2:
    st.metric(
        label="📊 Round Result",
        value=st.session_state.countdown_result,
        delta=st.session_state.last_result if st.session_state.last_result != "N/A" else None
    )

with hud_col3:
    # Display current score
    st.metric(
        label="🏆 Score",
        value=f"{st.session_state.user_score} - {st.session_state.computer_score}",
        delta=f"First to 3 wins!"
    )
RTC_CONFIGURATION = RTCConfiguration({
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]},
        {"urls": ["stun:stun1.l.google.com:19302"]},
        {"urls": ["stun:stun2.l.google.com:19302"]},
    ]
})


st.markdown("---")

# --- Webcam Feed Card ---
st.markdown("<h2>📹 Live Camera Feed</h2>", unsafe_allow_html=True)
st.markdown('<div class="custom-card">', unsafe_allow_html=True)
ctx = webrtc_streamer(
    key="rps-game",
    video_transformer_factory=RpsTransformer,
    rtc_configuration=RTC_CONFIGURATION,  # Add this line
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)


st.markdown('</div>', unsafe_allow_html=True)

# --- Game Control Buttons ---
st.markdown("<h2>🎮 Game Controls</h2>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    # Start Round button with countdown timer
    start_disabled = st.session_state.timer_active or st.session_state.game_over
    if st.button("🚀 Start Round (5s)", disabled=start_disabled, use_container_width=True):
        if ctx.video_transformer:
            # Activate the countdown timer
            st.session_state.timer_active = True
            st.session_state.end_time = time.time() + 5.0
            st.session_state.countdown_result = "Get Ready! 🎮"
            st.session_state.captured_user_move = "N/A"
            st.session_state.captured_ai_move = "N/A"
            st.rerun()
        else:
            st.error("❌ Webcam is not ready.")

with col2:
    if st.button("🔄 New Game", use_container_width=True):
        reset_game() # Call game logic
        st.session_state.timer_active = False
        st.session_state.countdown_result = "Waiting..."
        st.session_state.captured_user_move = "N/A"
        st.session_state.captured_ai_move = "N/A"
        # Reset AI move display on video
        if ctx.video_transformer:
            ctx.video_transformer.ai_move = "Waiting..."
        st.rerun()

# ========== TIMER LOGIC - COUNTDOWN & AUTO-PLAY ==========
if st.session_state.timer_active:
    time_remaining = st.session_state.end_time - time.time()
    
    if time_remaining > 0:
        # Timer is still running - force rerun to update display
        st.rerun()
    else:
        # Timer expired - execute the round
        st.session_state.timer_active = False
        
        if ctx.video_transformer:
            user_move = ctx.video_transformer.user_move
            
            if user_move != "None":
                # Play the round using game logic
                play_round(user_move)
                
                # Update the video transformer's AI move display
                ctx.video_transformer.ai_move = st.session_state.computer_move_display
                
                # Update countdown result
                st.session_state.countdown_result = st.session_state.last_result
            else:
                st.session_state.countdown_result = "No hand detected! ⚠️"
                st.session_state.last_result = "N/A"
        
        st.rerun()

# --- Score Display Card ---
st.markdown(f"""
<div class="custom-card">
    <div class="score-header">
        🏆 Score: You ({st.session_state.user_score}) - AI ({st.session_state.computer_score})
    </div>
    <p style='text-align: center; font-size: 1.2rem; color: #00D9FF;'>⚡ First to 3 wins! ⚡</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Round Result Display Card ---
st.markdown("<h2>📊 Round Results</h2>", unsafe_allow_html=True)

# Determine result color and emoji
result_class = ""
result_emoji = ""
if st.session_state.last_result == "You Win":
    result_class = "win-text"
    result_emoji = "🎉"
elif st.session_state.last_result == "AI Wins":
    result_class = "lose-text"
    result_emoji = "💀"
elif st.session_state.last_result == "Draw":
    result_emoji = "🤝"
else:
    result_emoji = "⏳"

# Map moves to emojis
move_emojis = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️", "N/A": "❓"}

st.markdown(f"""
<div class="custom-card result-box">
    <h3 style='text-align: center;'>
        <span class='{result_class}'>{result_emoji} {st.session_state.last_result}</span>
    </h3>
    <div style='display: flex; justify-content: space-around; margin-top: 1.5rem;'>
        <div style='text-align: center;'>
            <p style='font-size: 1.1rem; color: #888;'>You Played</p>
            <p style='font-size: 2rem;'>{move_emojis.get(st.session_state.user_move_display, "❓")}</p>
            <p style='font-size: 1.3rem; font-weight: 600; color: #00D9FF;'>{st.session_state.user_move_display}</p>
        </div>
        <div style='text-align: center; align-self: center;'>
            <p style='font-size: 2.5rem;'>⚔️</p>
        </div>
        <div style='text-align: center;'>
            <p style='font-size: 1.1rem; color: #888;'>AI Played</p>
            <p style='font-size: 2rem;'>{move_emojis.get(st.session_state.computer_move_display, "❓")}</p>
            <p style='font-size: 1.3rem; font-weight: 600; color: #FF006E;'>{st.session_state.computer_move_display}</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Game Over Message ---
if st.session_state.game_over:
     winner = "You" if st.session_state.user_score == 3 else "The AI"
     winner_emoji = "🏆🎊" if st.session_state.user_score == 3 else "🤖💪"
     st.markdown(f"""
     <div class="custom-card" style='background: linear-gradient(135deg, #00FF88 0%, #00D9FF 100%); border: none;'>
         <h2 style='text-align: center; color: #0E1117; font-size: 2.5rem;'>
             {winner_emoji} Game Over! {winner} won! {winner_emoji}
         </h2>
         <p style='text-align: center; color: #0E1117; font-size: 1.2rem; margin-top: 1rem;'>
             Click "🔄 New Game" to play again!
         </p>
     </div>
     """, unsafe_allow_html=True)