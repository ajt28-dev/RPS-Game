"""
🎯 HUD DEMO - Standalone Heads-Up Display Example
==================================================
This is a minimal, runnable example demonstrating the HUD system
with a countdown timer and game state management.

Run with: streamlit run hud_demo.py
"""

import streamlit as st
import time
import random

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="HUD Demo",
    page_icon="🎯",
    layout="wide"
)

# ========== STYLING ==========
st.markdown("""
<style>
    :root {
        --primary-bg: #0E1117;
        --secondary-bg: #1E2530;
        --accent-cyan: #00D9FF;
        --accent-magenta: #FF006E;
        --success-green: #00FF88;
        --text-white: #FFFFFF;
    }
    
    .stApp {
        background-color: var(--primary-bg);
        color: var(--text-white);
    }
    
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
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 25px rgba(0, 217, 255, 0.5);
    }
    
    h1 {
        background: linear-gradient(135deg, var(--accent-cyan), var(--accent-magenta));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 900;
        text-align: center;
    }
    
    h2 {
        color: var(--accent-cyan);
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ========== SESSION STATE INITIALIZATION ==========
def init_session_state():
    """Initialize all session state variables"""
    if 'timer_active' not in st.session_state:
        st.session_state.timer_active = False
    if 'end_time' not in st.session_state:
        st.session_state.end_time = 0.0
    if 'last_result' not in st.session_state:
        st.session_state.last_result = "Waiting..."
    if 'player_score' not in st.session_state:
        st.session_state.player_score = 0
    if 'ai_score' not in st.session_state:
        st.session_state.ai_score = 0
    if 'round_count' not in st.session_state:
        st.session_state.round_count = 0

# ========== HELPER FUNCTIONS ==========
def get_ai_result():
    """Simulates AI making a choice"""
    return random.choice(["Rock", "Paper", "Scissors"])

def simulate_game_result():
    """Simulates a game round and returns result"""
    outcomes = ["You Win! 🎉", "AI Wins 🤖", "Draw 🤝"]
    result = random.choice(outcomes)
    
    # Update scores
    if "You Win" in result:
        st.session_state.player_score += 1
    elif "AI Wins" in result:
        st.session_state.ai_score += 1
    
    st.session_state.round_count += 1
    return result

def reset_game():
    """Reset all game state"""
    st.session_state.player_score = 0
    st.session_state.ai_score = 0
    st.session_state.round_count = 0
    st.session_state.last_result = "Waiting..."
    st.session_state.timer_active = False

# ========== INITIALIZE ==========
init_session_state()

# ========== APP TITLE ==========
st.markdown("<h1>🎯 HUD Demo Application</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Demonstrating Persistent Heads-Up Display with Real-Time Timer</p>", unsafe_allow_html=True)
st.markdown("---")

# ========== HEADS-UP DISPLAY (HUD) ==========
# This section MUST be at the top to ensure visibility without scrolling
st.markdown("<h2>🎯 Game Status HUD</h2>", unsafe_allow_html=True)

hud_col1, hud_col2, hud_col3 = st.columns(3)

with hud_col1:
    # Timer Display
    if st.session_state.timer_active:
        time_remaining = max(0, st.session_state.end_time - time.time())
        timer_display = f"{time_remaining:.1f}s"
        timer_delta = "⏱️ Counting Down..."
    else:
        timer_display = "Ready"
        timer_delta = "⏸️ Standby Mode"
    
    st.metric(
        label="⏰ Time Remaining",
        value=timer_display,
        delta=timer_delta
    )

with hud_col2:
    # Result Display
    st.metric(
        label="📊 Round Result",
        value=st.session_state.last_result,
        delta=f"Round #{st.session_state.round_count}"
    )

with hud_col3:
    # Score Display
    st.metric(
        label="🏆 Score",
        value=f"{st.session_state.player_score} - {st.session_state.ai_score}",
        delta="Player - AI"
    )

st.markdown("---")

# ========== CONTROL PANEL ==========
st.markdown("<h2>🎮 Control Panel</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    # Start Round Button (Disabled while timer is active)
    start_disabled = st.session_state.timer_active
    if st.button("🚀 Start Round (5s)", disabled=start_disabled, use_container_width=True):
        # Activate timer
        st.session_state.timer_active = True
        st.session_state.end_time = time.time() + 5.0
        st.session_state.last_result = "Get Ready! 🎮"
        st.rerun()

with col2:
    # Manual Play (Instant, no timer)
    if st.button("⚡ Instant Play", use_container_width=True):
        st.session_state.last_result = simulate_game_result()
        st.rerun()

with col3:
    # Reset Game
    if st.button("🔄 Reset Game", use_container_width=True):
        reset_game()
        st.rerun()

st.markdown("---")

# ========== TIMER LOGIC ==========
# This is the core of the countdown system
if st.session_state.timer_active:
    time_remaining = st.session_state.end_time - time.time()
    
    if time_remaining > 0:
        # Timer still running - force rerun to update display
        st.rerun()
    else:
        # Timer expired - execute the action
        st.session_state.timer_active = False
        st.session_state.last_result = simulate_game_result()
        st.rerun()

# ========== INFORMATION PANEL ==========
st.markdown("<h2>ℹ️ How It Works</h2>", unsafe_allow_html=True)

info_col1, info_col2 = st.columns(2)

with info_col1:
    st.markdown("""
    ### 🎯 HUD Features
    - **Always Visible:** HUD stays at the top
    - **Real-Time Updates:** Timer counts down live
    - **State Persistence:** Data survives page reruns
    - **Visual Feedback:** Instant UI response
    
    ### ⏱️ Timer Mechanism
    1. Click "Start Round (5s)"
    2. Timer counts from 5.0 to 0.0
    3. Auto-executes when timer expires
    4. Updates HUD in real-time
    """)

with info_col2:
    st.markdown("""
    ### 🔧 Technical Details
    - **Session State:** Manages timer and game data
    - **st.rerun():** Forces immediate UI updates
    - **Unix Timestamps:** Reliable time tracking
    - **Disabled Buttons:** Prevents multiple timers
    
    ### 🎮 Try These Actions
    - Start a round and watch the countdown
    - Click "Instant Play" for immediate results
    - Reset the game to clear everything
    - Start multiple rounds to see scoring
    """)

st.markdown("---")

# ========== STATS PANEL ==========
st.markdown("<h2>📊 Session Statistics</h2>", unsafe_allow_html=True)

stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

with stats_col1:
    st.metric("Total Rounds", st.session_state.round_count)

with stats_col2:
    win_rate = (st.session_state.player_score / max(1, st.session_state.round_count)) * 100
    st.metric("Win Rate", f"{win_rate:.1f}%")

with stats_col3:
    st.metric("Player Wins", st.session_state.player_score)

with stats_col4:
    st.metric("AI Wins", st.session_state.ai_score)

# ========== CODE REFERENCE ==========
with st.expander("📝 View Implementation Code"):
    st.code("""
# SESSION STATE INITIALIZATION
if 'timer_active' not in st.session_state:
    st.session_state.timer_active = False
if 'end_time' not in st.session_state:
    st.session_state.end_time = 0.0
if 'last_result' not in st.session_state:
    st.session_state.last_result = "Waiting..."

# HUD DISPLAY
hud_col1, hud_col2, hud_col3 = st.columns(3)

with hud_col1:
    if st.session_state.timer_active:
        time_remaining = max(0, st.session_state.end_time - time.time())
        timer_display = f"{time_remaining:.1f}s"
    else:
        timer_display = "Ready"
    st.metric(label="⏰ Time Remaining", value=timer_display)

# BUTTON HANDLER
if st.button("🚀 Start Round (5s)", disabled=st.session_state.timer_active):
    st.session_state.timer_active = True
    st.session_state.end_time = time.time() + 5.0
    st.rerun()

# TIMER MAIN LOOP
if st.session_state.timer_active:
    time_remaining = st.session_state.end_time - time.time()
    
    if time_remaining > 0:
        st.rerun()  # Keep updating
    else:
        st.session_state.timer_active = False
        # Execute your action here
        st.rerun()
    """, language="python")

# ========== FOOTER ==========
st.markdown("---")
st.markdown("""
<p style='text-align: center; color: #888;'>
    🎯 HUD Demo v2.0 | Built with Streamlit | 
    <a href='https://github.com/ajt28-dev/RPS-Game' style='color: #00D9FF;'>View on GitHub</a>
</p>
""", unsafe_allow_html=True)
