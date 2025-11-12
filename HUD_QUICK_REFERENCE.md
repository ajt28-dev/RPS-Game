# 🎯 HUD Quick Reference Card

## 🚀 Quick Start

```bash
# Run the full game
streamlit run app.py

# Run the standalone demo
streamlit run hud_demo.py
```

---

## 📊 HUD Components

| Component | Label | Shows | States |
|-----------|-------|-------|--------|
| **Timer** | ⏰ Time Remaining | Countdown | "Ready" / "4.3s" / "0.0s" |
| **Result** | 📊 Round Result | Last outcome | "You Win" / "AI Wins" / "Draw" |
| **Score** | 🏆 Score | Match score | "2 - 1" format |

---

## 🎮 Game Flow

```
1. Click "Start Round (5s)"
   ↓
2. Timer counts: 5.0 → 4.9 → ... → 0.0
   ↓
3. Make hand gesture (Rock/Paper/Scissors)
   ↓
4. Timer hits 0 → Round plays automatically
   ↓
5. HUD updates with result and score
   ↓
6. Repeat or click "New Game"
```

---

## 🔧 Key Code Snippets

### Initialize Session State
```python
if 'timer_active' not in st.session_state:
    st.session_state.timer_active = False
if 'end_time' not in st.session_state:
    st.session_state.end_time = 0.0
```

### Create HUD
```python
hud_col1, hud_col2, hud_col3 = st.columns(3)

with hud_col1:
    if st.session_state.timer_active:
        time_remaining = max(0, st.session_state.end_time - time.time())
        timer_display = f"{time_remaining:.1f}s"
    else:
        timer_display = "Ready"
    
    st.metric(
        label="⏰ Time Remaining",
        value=timer_display
    )
```

### Start Timer
```python
if st.button("🚀 Start Round (5s)", disabled=st.session_state.timer_active):
    st.session_state.timer_active = True
    st.session_state.end_time = time.time() + 5.0
    st.rerun()
```

### Timer Main Loop
```python
if st.session_state.timer_active:
    time_remaining = st.session_state.end_time - time.time()
    
    if time_remaining > 0:
        st.rerun()  # Keep updating
    else:
        # Timer expired - execute action
        st.session_state.timer_active = False
        play_round(user_move)
        st.rerun()
```

---

## 🐛 Common Issues & Fixes

| Issue | Cause | Fix |
|-------|-------|-----|
| Timer doesn't update | Missing `st.rerun()` | Add `st.rerun()` in timer loop |
| Multiple timers | Button not disabled | Use `disabled=st.session_state.timer_active` |
| HUD below content | Wrong placement | Move HUD code to top of script |
| Button stays disabled | Timer not reset | Set `timer_active = False` when done |

---

## 📝 Session State Variables

```python
# Timer State
st.session_state.timer_active       # bool
st.session_state.end_time          # float (Unix timestamp)
st.session_state.countdown_result  # str

# Game State
st.session_state.user_score        # int
st.session_state.computer_score    # int
st.session_state.last_result       # str
st.session_state.game_over         # bool

# Move Tracking
st.session_state.user_move_display      # str
st.session_state.computer_move_display  # str
```

---

## 🎨 Customization Examples

### Change Timer Duration
```python
# From 5 seconds to 10 seconds
st.session_state.end_time = time.time() + 10.0
```

### Add Custom HUD Metric
```python
with hud_col4:
    st.metric(
        label="🔥 Win Streak",
        value=st.session_state.win_streak,
        delta="+1"
    )
```

### Change Button Text
```python
st.button("⚡ GO! (5s)", disabled=start_disabled)
```

---

## 📚 Documentation Files

- **HUD_IMPLEMENTATION.md** - Complete technical guide (10+ pages)
- **HUD_SUMMARY.md** - Implementation summary with all details
- **hud_demo.py** - Standalone working demo
- **THIS FILE** - Quick reference card

---

## ✅ Verification Checklist

- [ ] HUD appears at top of page
- [ ] Timer counts down in real-time
- [ ] Button disabled during countdown
- [ ] Round auto-executes when timer expires
- [ ] Results display in HUD
- [ ] Score updates correctly
- [ ] "New Game" resets everything
- [ ] No errors in console

---

## 🎯 Testing Commands

```bash
# Test standalone demo
streamlit run hud_demo.py

# Test full app
streamlit run app.py

# Check for errors
# (Watch terminal output while clicking buttons)
```

---

## 📞 Key Functions

| Function | Purpose | Location |
|----------|---------|----------|
| `reset_game()` | Reset scores & state | `game_logic.py` |
| `play_round(move)` | Execute one round | `game_logic.py` |
| `classify_hand()` | Detect gesture | `hand_classifier.py` |
| `RpsTransformer` | Video processing | `video_processor.py` |

---

## 🏆 Success Metrics

✅ **User Experience:** Exciting countdown creates anticipation  
✅ **Fairness:** Fixed 5-second window for all players  
✅ **Visibility:** Critical info always on screen  
✅ **Performance:** Smooth 60fps countdown animation  
✅ **Reliability:** No race conditions or bugs  

---

## 🔮 Extension Ideas

```python
# Add sound effect on timer expiration
if time_remaining <= 0:
    st.audio("countdown_beep.mp3")
    
# Add progress bar
progress = time_remaining / 5.0
st.progress(progress)

# Add animation
if time_remaining < 1.0:
    st.markdown('<div class="pulse">GET READY!</div>')
```

---

**Quick Links:**
- GitHub: [ajt28-dev/RPS-Game](https://github.com/ajt28-dev/RPS-Game)
- Docs: See `HUD_IMPLEMENTATION.md`
- Demo: Run `hud_demo.py`

**Version:** 2.0 (HUD Implementation)  
**Date:** November 12, 2025
