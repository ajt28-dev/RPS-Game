# 🎮 Rock Paper Scissors - Computer Vision Game

A real-time Rock Paper Scissors game powered by computer vision and AI. Play against the computer using hand gestures detected through your webcam!

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.40+-red.svg)
![MediaPipe](https://img.shields.io/badge/mediapipe-0.10+-green.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

## 🌟 Features

- **Real-Time Hand Gesture Recognition** - Uses MediaPipe for accurate hand tracking
- **Computer Vision AI** - Analyzes finger angles to classify Rock, Paper, or Scissors
- **Live Video Feed** - WebRTC-powered camera stream with hand landmark visualization
- **5-Second Countdown Timer** - Build anticipation before each round
- **Interactive HUD** - Real-time display of game state, scores, and results
- **Modern UI** - Vibrant neon-themed interface with smooth animations
- **First to 3 Wins** - Classic competitive format

## 🎯 How It Works

1. **Hand Detection**: MediaPipe Hands detects 21 landmarks on your hand
2. **Angle Calculation**: The system calculates finger extension angles using vector mathematics
3. **Gesture Classification**: 
   - **Rock**: 0-1 fingers extended (fist)
   - **Scissors**: 2 fingers extended (index + middle)
   - **Paper**: 4-5 fingers extended (open hand)
4. **Game Logic**: Your move is captured after the countdown and compared against the AI's random choice

## 🚀 Quick Start

### Prerequisites

- Python 3.11
- Webcam
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ajt28-dev/RPS-Game.git
   cd RPS-Game
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Run Locally

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📦 Project Structure

```
RPS-Game/
│
├── app.py                    # Main Streamlit application
├── video_processor.py        # WebRTC video processing with MediaPipe
├── hand_classifier.py        # Hand gesture recognition logic
├── game_logic.py            # Game rules and state management
│
├── requirements.txt         # Python dependencies
├── runtime.txt             # Python version for deployment
├── packages.txt            # System-level dependencies
├── .gitignore              # Git ignore rules
│
└── docs/                   # Documentation files
    ├── HUD_ARCHITECTURE.md
    ├── STYLING_GUIDE.md
    └── ...
```

## 🎮 How to Play

1. **Allow Camera Access**: Grant permission when prompted
2. **Show Your Hand**: Position your hand clearly in the camera frame
3. **Click "Start Round"**: A 5-second countdown begins
4. **Make Your Move**: Form Rock, Paper, or Scissors before time runs out
5. **See Results**: Your move is captured and compared against the AI
6. **Win 3 Rounds**: First player to 3 wins takes the game!

## 🧠 Technical Details

### Hand Gesture Recognition Algorithm

The hand classifier uses angle-based detection:

```python
# Calculate finger extension angle
angle = arccos(dot(vec1, vec2) / (||vec1|| * ||vec2||))

# Classification rules
if extended_fingers >= 4:    return "Paper"
elif extended_fingers == 2:  return "Scissors"
elif extended_fingers <= 1:  return "Rock"
```

### Key Technologies

- **Streamlit**: Web framework and UI
- **streamlit-webrtc**: Real-time video streaming
- **MediaPipe Hands**: Hand landmark detection (21 points)
- **OpenCV**: Image processing
- **NumPy**: Mathematical operations

### Performance Optimizations

- `static_image_mode=True` prevents MediaPipe timestamp conflicts
- Async video processing for smooth frame handling
- WebRTC with STUN servers for reliable camera connections

## 🌐 Deployment

### Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy!

The app is configured with:
- `runtime.txt` → Python 3.11
- `packages.txt` → System dependencies (libgl1, libglib2.0-0)
- `requirements.txt` → Python packages

### Environment Variables

No environment variables required for basic deployment.

## 🎨 Customization

### Modify Game Rules

Edit `game_logic.py` to change:
- Win condition (default: first to 3)
- AI difficulty
- Scoring system

### Adjust Detection Sensitivity

In `hand_classifier.py`:
```python
straight_threshold = 160.0  # Lower = more sensitive detection
```

### Change UI Theme

Modify CSS variables in `app.py`:
```css
--accent-cyan: #00D9FF;
--accent-magenta: #FF006E;
--success-green: #00FF88;
```

## 🐛 Troubleshooting

### Camera Not Working
- Ensure browser has camera permissions
- Check if another app is using the camera
- Try refreshing the page

### Hand Not Detected
- Ensure good lighting
- Keep hand within camera frame
- Try adjusting detection confidence in `video_processor.py`

### "Missing ScriptRunContext" Warnings
- These are normal with async processing
- They don't affect functionality
- Can be safely ignored

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**ajt28-dev**

## 🙏 Acknowledgments

- MediaPipe team for the hand tracking solution
- Streamlit for the amazing web framework
- The computer vision community

---

Made with ❤️ and Python
