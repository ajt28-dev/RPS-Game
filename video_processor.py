import cv2
import mediapipe as mp
import mediapipe.solutions
from streamlit_webrtc import VideoProcessorBase
import streamlit as st
import av

# --- Import our custom classifier module ---
import hand_classifier

# --- MediaPipe Setup ---
mp_hands = mediapipe.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=True,  # Treat each frame independently to avoid timestamp issues
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_draw = mediapipe.solutions.drawing_utils

class RpsTransformer(VideoProcessorBase):
    def __init__(self):
        self.user_move = "None"
        self.ai_move = "Waiting..."

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        
        self.user_move = "None" # Reset each frame
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks
                mp_draw.draw_landmarks(
                    img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # --- THIS IS THE KEY CHANGE ---
                # Use the classifier from our imported module 
                self.user_move = hand_classifier.classify_hand(hand_landmarks.landmark)

        # Get image dimensions for proper text positioning
        height, width = img.shape[:2]
        
        # Display the recognized move on the LEFT side of the video feed
        cv2.putText(img, f"You: {self.user_move}",
                    (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.8, (0, 255, 0), 2, cv2.LINE_AA)  # Green color for user
        
        # Display AI's move on the RIGHT side
        # Try to get from session state and update self.ai_move
        try:
            if hasattr(st, 'session_state') and 'computer_move_display' in st.session_state:
                ai_move_from_state = st.session_state.computer_move_display
                if ai_move_from_state and ai_move_from_state != "N/A":
                    self.ai_move = ai_move_from_state
        except:
            pass  # Keep current ai_move if access fails
        
        # Calculate text width to right-align properly
        text = f"AI: {self.ai_move}"
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
        text_x = width - text_size[0] - 10  # 10 pixels from right edge
        
        cv2.putText(img, text,
                    (text_x, 40), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.8, (0, 255, 255), 2, cv2.LINE_AA)  # Cyan color for AI
        
        return av.VideoFrame.from_ndarray(img, format="bgr24")