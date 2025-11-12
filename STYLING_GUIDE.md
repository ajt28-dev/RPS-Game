# 🎨 Vibrant Styling Guide for RPS Game

## Color Palette: "Neon Gaming Dark Mode"

```css
--primary-bg: #0E1117        /* Deep dark blue-black */
--secondary-bg: #1E2530      /* Slate gray */
--accent-cyan: #00D9FF       /* Electric cyan */
--accent-magenta: #FF006E    /* Vibrant magenta */
--success-green: #00FF88     /* Neon green */
--text-white: #FFFFFF        /* Pure white */
```

---

## 📦 Component Usage Examples

### 1. Custom Card Container

Use this for grouping related content with visual depth:

```python
st.markdown('<div class="custom-card">', unsafe_allow_html=True)
st.write("Your content here")
st.metric("Score", "100", "+10")
st.markdown('</div>', unsafe_allow_html=True)
```

**Features:**
- ✨ Subtle gradient background
- 🌟 Glowing border on hover
- 📦 Automatic elevation on hover (lifts 4px)
- 🎨 Rounded corners (20px radius)

---

### 2. Gradient Headers

Already implemented in the main app:

```python
# H1 - Main Title (Auto-styled)
st.markdown("<h1>🎮 Your Title Here</h1>", unsafe_allow_html=True)

# H2 - Section Headers (Auto-styled with cyan)
st.markdown("<h2>📊 Section Title</h2>", unsafe_allow_html=True)
```

---

### 3. Stylized Buttons

Buttons are automatically styled, but you can enhance them with emojis:

```python
# Recommended emojis for different actions:
st.button("🎲 Play Round")      # Game action
st.button("🔄 New Game")        # Reset/Refresh
st.button("⚙️ Settings")        # Configuration
st.button("📊 Stats")           # Statistics
st.button("💾 Save")            # Save action
st.button("❌ Cancel")          # Cancel/Close
st.button("✅ Confirm")         # Confirm action
st.button("🏆 Leaderboard")     # Rankings
```

**Button Effects:**
- 🌈 Gradient background (cyan to magenta)
- ✨ Glow effect on hover
- 📈 Scales to 105% and lifts on hover
- 💫 Smooth transitions (0.3s)

---

### 4. Score Display with Gradient Text

```python
st.markdown(f"""
<div class="score-header">
    🏆 Score: Player ({score_1}) - AI ({score_2})
</div>
""", unsafe_allow_html=True)
```

---

### 5. Result Box with Color Coding

```python
# Win result
st.markdown(f"""
<div class="custom-card result-box">
    <h3 style='text-align: center;'>
        <span class='win-text'>🎉 You Win!</span>
    </h3>
</div>
""", unsafe_allow_html=True)

# Lose result
st.markdown(f"""
<div class="custom-card result-box">
    <h3 style='text-align: center;'>
        <span class='lose-text'>💀 AI Wins!</span>
    </h3>
</div>
""", unsafe_allow_html=True)
```

---

### 6. Custom Dividers

Horizontal rules are auto-styled with gradients:

```python
st.markdown("---")  # Creates a gradient divider
```

---

## 🎯 Recommended Emojis by Category

### Game Actions
- 🎲 Play/Action
- 🔄 Restart/Reset
- ⏸️ Pause
- ⏹️ Stop
- ▶️ Start/Resume

### Results
- 🏆 Victory/Win
- 💀 Defeat/Loss
- 🤝 Draw/Tie
- ⚔️ Battle/Versus
- 🎯 Target/Goal

### Hand Gestures
- ✊ Rock
- ✋ Paper
- ✌️ Scissors
- 👋 Wave/Hello
- 👍 Good/Approve

### Status Indicators
- ✅ Success
- ❌ Error/Cancel
- ⚠️ Warning
- ℹ️ Info
- 🔴 Live/Active
- 🟢 Ready/Online
- 🟡 Waiting/Pending

### Navigation & Controls
- 📹 Camera/Video
- 📊 Statistics/Charts
- ⚙️ Settings
- 📱 Device/Screen
- 🎮 Gaming/Controls

### Celebration
- 🎉 Party/Celebrate
- 🎊 Confetti
- ✨ Sparkle/Magic
- 💫 Stars
- 🌟 Shine/Highlight

---

## 🔧 Advanced Customizations

### Creating a New Card Variant

```python
# Add this to your st.markdown <style> section:
"""
.info-card {
    background: linear-gradient(145deg, #1E2530 0%, #2A3F5F 100%);
    border-left: 4px solid var(--accent-cyan);
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1rem 0;
}
"""

# Usage:
st.markdown('<div class="info-card">', unsafe_allow_html=True)
st.write("ℹ️ **Tip:** This is an informational card!")
st.markdown('</div>', unsafe_allow_html=True)
```

### Adding Glow Animation to Text

```python
st.markdown("""
<h2 class="glow">✨ This text glows!</h2>
""", unsafe_allow_html=True)
```

### Custom Color Text

```python
st.markdown("""
<p style='color: #00D9FF; font-weight: 600;'>Cyan text</p>
<p style='color: #FF006E; font-weight: 600;'>Magenta text</p>
<p style='color: #00FF88; font-weight: 600;'>Green text</p>
""", unsafe_allow_html=True)
```

---

## 📱 Responsive Design Tips

All components are designed to be responsive. For best results:

1. **Use Streamlit columns** for side-by-side layouts
2. **Keep card content concise** to avoid overflow
3. **Test on different screen sizes**
4. **Use emojis sparingly** - 2-3 per section maximum

---

## 🎨 Alternative Color Schemes

If you want to try different themes, here are two alternatives:

### "Sunny & Clean" Theme
```css
--primary-bg: #FFFFFF        /* Pure white */
--secondary-bg: #F5F7FA      /* Light gray */
--accent-orange: #FF6B35     /* Bright orange */
--accent-yellow: #FFD23F     /* Sunny yellow */
--text-dark: #2C3E50         /* Dark blue-gray */
```

### "Purple Dream" Theme
```css
--primary-bg: #1A0B2E        /* Deep purple */
--secondary-bg: #2D1B4E      /* Rich purple */
--accent-purple: #A061FF     /* Bright purple */
--accent-pink: #FF61D8       /* Hot pink */
--success-teal: #00E5CC      /* Teal */
```

To change themes, simply replace the color variables in the `:root` section of the CSS.

---

## ✅ Best Practices

1. **Consistency:** Use the same emojis for the same actions throughout your app
2. **Contrast:** Ensure text is always readable against backgrounds
3. **Performance:** Don't nest too many custom cards (max 2-3 levels)
4. **Accessibility:** Emojis should complement text, not replace it
5. **Spacing:** Use margins between cards for visual breathing room

---

## 🚀 Quick Start Checklist

- [x] Color palette defined
- [x] Button hover effects implemented
- [x] Card containers styled
- [x] Headers with gradient text
- [x] Emojis added to key elements
- [x] Result displays color-coded
- [x] Game over screen enhanced
- [x] All interactive elements have visual feedback

---

**Enjoy your vibrant, modern RPS game! 🎮✨**
