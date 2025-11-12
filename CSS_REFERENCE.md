# 🎨 Complete CSS Reference - Quick Copy-Paste Guide

## Full CSS Implementation

This is the complete CSS code injected into your `app.py`. You can copy sections for use in other Streamlit projects:

```python
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
```

---

## Key CSS Features Explained

### 1. **CSS Variables (`:root`)**
Makes it easy to change colors globally - just update one value!

### 2. **Gradient Backgrounds**
```css
background: linear-gradient(135deg, #00D9FF 0%, #FF006E 100%);
```
Creates smooth color transitions from cyan to magenta at 135° angle.

### 3. **Text Gradients**
```css
background: linear-gradient(...);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
```
Makes text itself display the gradient.

### 4. **Box Shadows for Depth**
```css
box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4),
            0 0 20px rgba(0, 217, 255, 0.1);
```
First shadow = depth, second shadow = glow effect.

### 5. **Hover Transforms**
```css
transform: scale(1.05) translateY(-2px);
```
Makes element 5% bigger and lifts it 2px up.

### 6. **Smooth Transitions**
```css
transition: all 0.3s ease;
```
Animates all property changes over 0.3 seconds.

---

## Individual Component Snippets

### Just the Button Styling
```python
st.markdown("""
<style>
.stButton > button {
    background: linear-gradient(135deg, #00D9FF 0%, #FF006E 100%);
    color: #FFFFFF;
    border: none;
    border-radius: 12px;
    padding: 0.75rem 2rem;
    font-weight: 600;
    font-size: 1.1rem;
    box-shadow: 0 4px 15px rgba(0, 217, 255, 0.3);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.05) translateY(-2px);
    box-shadow: 0 8px 25px rgba(0, 217, 255, 0.5);
    filter: brightness(1.2);
}
</style>
""", unsafe_allow_html=True)
```

### Just the Card Styling
```python
st.markdown("""
<style>
.custom-card {
    background: linear-gradient(145deg, #1E2530 0%, #262D3D 100%);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(0, 217, 255, 0.2);
    margin: 1rem 0;
    transition: all 0.3s ease;
}

.custom-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5);
}
</style>
""", unsafe_allow_html=True)
```

### Just the Gradient Headers
```python
st.markdown("""
<style>
h1 {
    background: linear-gradient(135deg, #00D9FF, #FF006E);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 900;
    text-align: center;
}

h2 {
    color: #00D9FF;
    font-weight: 700;
    text-shadow: 0 0 20px rgba(0, 217, 255, 0.3);
}
</style>
""", unsafe_allow_html=True)
```

---

## Color Palette Variations

### Ocean Theme
```css
:root {
    --primary-bg: #001F3F;      /* Navy */
    --accent-1: #0074D9;        /* Blue */
    --accent-2: #39CCCC;        /* Teal */
    --success: #2ECC40;         /* Green */
}
```

### Sunset Theme
```css
:root {
    --primary-bg: #2C1B47;      /* Deep purple */
    --accent-1: #FF6B6B;        /* Coral */
    --accent-2: #FFD93D;        /* Gold */
    --success: #6BCB77;         /* Green */
}
```

### Matrix Theme
```css
:root {
    --primary-bg: #0D0D0D;      /* Almost black */
    --accent-1: #00FF41;        /* Matrix green */
    --accent-2: #00D9FF;        /* Cyan */
    --success: #39FF14;         /* Neon green */
}
```

---

## Performance Tips

1. **Use CSS variables** - faster than inline styles
2. **Limit animations** - only on hover/active states
3. **Use `transform` instead of `top/left`** - GPU accelerated
4. **Avoid excessive shadows** - max 2-3 per element
5. **Use `will-change` for complex animations**:
   ```css
   .custom-card {
       will-change: transform;
   }
   ```

---

## Browser Compatibility

All CSS features used are compatible with:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

Note: `-webkit-` prefixes are included for better Safari support.

---

## Troubleshooting

### Issue: Styles not applying
**Solution:** Ensure `unsafe_allow_html=True` is set

### Issue: Text not visible
**Solution:** Check contrast ratios, use lighter colors on dark backgrounds

### Issue: Hover effects choppy
**Solution:** Add `transition: all 0.3s ease;` to base element

### Issue: Cards not aligning
**Solution:** Use `st.columns()` or add `display: flex;` to parent

---

**Ready to build more amazing interfaces! 🚀**
