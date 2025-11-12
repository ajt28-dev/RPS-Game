# 🎯 Heads-Up Display (HUD) Implementation Guide

## Overview
This document explains the persistent HUD system implemented in the RPS Game application. The HUD provides real-time game status information that remains visible at the top of the screen, above all other content.

---

## 📋 Table of Contents
1. [Architecture](#architecture)
2. [Session State Management](#session-state-management)
3. [HUD Components](#hud-components)
4. [Timer Logic](#timer-logic)
5. [Usage Guide](#usage-guide)

---

## 🏗️ Architecture

### Layout Hierarchy
```
┌─────────────────────────────────────────┐
│  🎯 HEADS-UP DISPLAY (HUD)              │
│  ┌──────────┬──────────┬──────────┐    │
│  │ Timer    │ Result   │ Score    │    │
│  └──────────┴──────────┴──────────┘    │
├─────────────────────────────────────────┤
│  📹 Live Camera Feed                    │
├─────────────────────────────────────────┤
│  🎮 Game Controls                       │
├─────────────────────────────────────────┤
│  📊 Detailed Round Results              │
└─────────────────────────────────────────┘
```

### Key Principle
**The HUD is rendered FIRST** in the script, ensuring it always appears at the top of the page, regardless of page scroll position.

---

## 💾 Session State Management

### Required State Variables

```python
# Timer Management
st.session_state.timer_active    # bool: Is countdown running?
st.session_state.end_time        # float: Unix timestamp when timer ends
st.session_state.countdown_result # str: Current round status message

# Game State (from game_logic.py)
st.session_state.user_score      # int: Player's score
st.session_state.computer_score  # int: AI's score
st.session_state.last_result     # str: "You Win" | "AI Wins" | "Draw" | "N/A"
st.session_state.game_over       # bool: Has someone won 3 rounds?

# Move Tracking
st.session_state.user_move_display      # str: Last user move
st.session_state.computer_move_display  # str: Last AI move
st.session_state.captured_user_move     # str: Move captured at timer end
st.session_state.captured_ai_move       # str: AI move at timer end
```

### Initialization Pattern

```python
# Always check before initializing
if 'timer_active' not in st.session_state:
    st.session_state.timer_active = False

if 'end_time' not in st.session_state:
    st.session_state.end_time = 0.0

if 'countdown_result' not in st.session_state:
    st.session_state.countdown_result = "Waiting..."
```

---

## 🎮 HUD Components

### Component 1: Timer Display

**Purpose:** Shows real-time countdown during active rounds.

```python
with hud_col1:
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
```

**States:**
- **Active:** Shows countdown in seconds (e.g., "3.2s")
- **Inactive:** Shows "Ready" with standby indicator

---

### Component 2: Round Result Display

**Purpose:** Shows the outcome of the last completed round.

```python
with hud_col2:
    st.metric(
        label="📊 Round Result",
        value=st.session_state.countdown_result,
        delta=st.session_state.last_result if st.session_state.last_result != "N/A" else None
    )
```

**Possible Values:**
- `"Waiting..."` - No round started yet
- `"Get Ready! 🎮"` - Countdown started
- `"You Win"` - Player won the round
- `"AI Wins"` - AI won the round
- `"Draw"` - Tie game
- `"No hand detected! ⚠️"` - Timer expired but no gesture detected

---

### Component 3: Score Display

**Purpose:** Shows the current match score.

```python
with hud_col3:
    st.metric(
        label="🏆 Score",
        value=f"{st.session_state.user_score} - {st.session_state.computer_score}",
        delta=f"First to 3 wins!"
    )
```

**Format:** `"Player Score - AI Score"` (e.g., "2 - 1")

---

## ⏱️ Timer Logic

### How the Countdown Works

The timer system uses a combination of:
1. **Session State** - Persists timer data across reruns
2. **`st.rerun()`** - Forces immediate UI updates for live countdown
3. **Unix Timestamps** - Reliable time tracking

### Timer Lifecycle

```
┌─────────────────┐
│ User clicks     │
│ "Start Round"   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Set:            │
│ timer_active=T  │
│ end_time=now+5  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Main Loop:      │
│ Check time      │
│ Update display  │
│ Call rerun()    │
└────────┬────────┘
         │
         ▼
    Time > 0?
         │
    ┌────┴────┐
   YES       NO
    │         │
    │         ▼
    │    ┌────────────┐
    │    │ Capture    │
    │    │ moves      │
    │    │ Play round │
    │    │ Set active │
    │    │ = False    │
    │    └────────────┘
    │
    └──────> Rerun to update display
```

### Implementation Code

```python
# TIMER ACTIVATION (Button Click)
if st.button("🚀 Start Round (5s)", disabled=start_disabled):
    if ctx.video_transformer:
        st.session_state.timer_active = True
        st.session_state.end_time = time.time() + 5.0
        st.session_state.countdown_result = "Get Ready! 🎮"
        st.rerun()

# TIMER MAIN LOOP (Placed after button definitions)
if st.session_state.timer_active:
    time_remaining = st.session_state.end_time - time.time()
    
    if time_remaining > 0:
        # Still counting - force UI update
        st.rerun()
    else:
        # Timer expired - execute game logic
        st.session_state.timer_active = False
        
        if ctx.video_transformer:
            user_move = ctx.video_transformer.user_move
            
            if user_move != "None":
                # Play the round
                play_round(user_move)
                st.session_state.countdown_result = st.session_state.last_result
            else:
                st.session_state.countdown_result = "No hand detected! ⚠️"
        
        st.rerun()
```

---

## 📖 Usage Guide

### For Players

1. **Start a Round**
   - Click "🚀 Start Round (5s)" button
   - Watch the HUD timer count down from 5.0 to 0.0
   - Make your hand gesture (Rock, Paper, or Scissors) before time runs out

2. **During Countdown**
   - The timer display updates in real-time
   - "Start Round" button is disabled (preventing multiple timers)
   - Result shows "Get Ready! 🎮"

3. **After Round Completes**
   - Timer stops at "Ready"
   - Result shows "You Win", "AI Wins", or "Draw"
   - Score updates automatically
   - You can start another round

4. **Starting a New Game**
   - Click "🔄 New Game" at any time
   - Resets scores to 0-0
   - Clears all round results
   - Stops any active timer

### For Developers

#### Adding a New HUD Metric

```python
with hud_col4:  # Add a 4th column
    st.metric(
        label="🎯 Your Label",
        value=st.session_state.your_variable,
        delta="Optional delta text"
    )
```

#### Modifying Timer Duration

Change the `5.0` in the button click handler:

```python
st.session_state.end_time = time.time() + 10.0  # 10 second timer
```

#### Adding Timer Events

Insert logic in the timer expiration block:

```python
else:
    # Timer expired
    st.session_state.timer_active = False
    
    # YOUR CUSTOM LOGIC HERE
    send_notification()
    log_event("round_completed")
    
    # ... existing game logic ...
```

---

## 🎨 Visual Design

The HUD uses the app's vibrant color palette:

- **Primary Accent:** `#00D9FF` (Electric Cyan)
- **Secondary Accent:** `#FF006E` (Vibrant Magenta)
- **Background:** `#1E2530` (Dark Slate)

The `st.metric` widgets automatically style themselves with:
- Gradient text effects
- Hover animations
- Card-like elevation
- Responsive layout

---

## 🔧 Troubleshooting

### Timer Doesn't Update
**Problem:** Timer shows same value and doesn't count down.
**Solution:** Ensure `st.rerun()` is called in the timer loop.

### Button Stays Disabled
**Problem:** Can't click "Start Round" after a round ends.
**Solution:** Check that `st.session_state.timer_active` is set to `False` when timer expires.

### HUD Not at Top
**Problem:** HUD appears below other content.
**Solution:** Move the HUD code block to be the FIRST UI element after session state initialization.

### Multiple Timers Running
**Problem:** Starting multiple rounds creates overlapping timers.
**Solution:** Use `disabled=st.session_state.timer_active` on the Start Round button.

---

## 📈 Performance Notes

- **Rerun Frequency:** While timer is active, the app reruns ~60 times per second
- **Impact:** Minimal - Streamlit is optimized for rapid reruns
- **Optimization:** Timer only reruns when `timer_active` is `True`

---

## 🚀 Future Enhancements

Possible additions to the HUD system:

1. **Streak Counter** - Show consecutive wins
2. **Win Rate** - Display percentage of rounds won
3. **Animation** - Add pulse effect on timer expiration
4. **Sound Effects** - Play audio cues at key moments
5. **Countdown Voice** - "3... 2... 1... Go!"
6. **Progress Bar** - Visual timer bar alongside numeric display

---

## 📝 Code Reference

**Full Implementation Location:** `app.py`

**Related Files:**
- `game_logic.py` - Round execution and scoring
- `video_processor.py` - Hand gesture detection
- `hand_classifier.py` - Move classification logic

**Key Dependencies:**
- `streamlit` - UI framework
- `time` - Timer calculations
- `random` - AI move generation

---

## ✅ Success Criteria Checklist

- [x] HUD positioned at top of page
- [x] Timer displays live countdown
- [x] Round results update in real-time
- [x] Score always visible without scrolling
- [x] Button states managed correctly
- [x] Timer auto-executes round on expiration
- [x] All state persists across reruns
- [x] No race conditions or state conflicts

---

**Last Updated:** November 12, 2025  
**Version:** 2.0 (HUD Implementation)  
**Authors:** Nicolei Faith Abot & Adlei Jed Tan
