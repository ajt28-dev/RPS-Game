import numpy as np

# --- This section directly implements your paper's math ---

def get_angle(p_base, p_mid, p_tip):
    """
    Calculates the angle at the middle joint (PIP) based on 
    your paper's dot product formula .
    """
    # Create numpy arrays for the 3 points
    base = np.array([p_base.x, p_base.y, p_base.z])
    mid = np.array([p_mid.x, p_mid.y, p_mid.z])
    tip = np.array([p_tip.x, p_tip.y, p_tip.z])
    
    # Create vectors from mid-to-base and mid-to-tip 
    vec1 = base - mid
    vec2 = tip - mid
    
    # Calculate dot product
    dot_prod = np.dot(vec1, vec2)
    
    # Calculate vector magnitudes
    mag_vec1 = np.linalg.norm(vec1)
    mag_vec2 = np.linalg.norm(vec2)
    
    # Calculate angle in radians, then degrees
    # We use np.clip to avoid math errors from floating point inaccuracy
    cos_theta = np.clip(dot_prod / (mag_vec1 * mag_vec2), -1.0, 1.0)
    angle_rad = np.arccos(cos_theta)
    angle_deg = np.degrees(angle_rad)
    
    return angle_deg

def classify_hand(landmarks):
    """
    Classifies the hand gesture based on the "count how many
    fingers are extended" rule from your paper .
    """
    
    # Get angles for the 4 main fingers 
    angle_index = get_angle(landmarks[5], landmarks[6], landmarks[8])
    angle_middle = get_angle(landmarks[9], landmarks[10], landmarks[12])
    angle_ring = get_angle(landmarks[13], landmarks[14], landmarks[16])
    angle_pinky = get_angle(landmarks[17], landmarks[18], landmarks[20])
    
    # "If angle ≈ 180° the finger is straight" 
    straight_threshold = 160.0 
    
    extended_fingers = 0
    if angle_index > straight_threshold: extended_fingers += 1
    if angle_middle > straight_threshold: extended_fingers += 1
    if angle_ring > straight_threshold: extended_fingers += 1
    if angle_pinky > straight_threshold: extended_fingers += 1

    # Apply the classification rules from your paper 
    
    # Rule for Paper: 4 or 5 fingers extended 
    if extended_fingers >= 4:
        return "Paper"
        
    # Rule for Scissors: 2 fingers extended (index + middle) 
    elif extended_fingers == 2 and \
         angle_index > straight_threshold and \
         angle_middle > straight_threshold:
        return "Scissors"
        
    # Rule for Rock: 0 or 1 finger extended 
    elif extended_fingers <= 1:
        return "Rock"
        
    return "None"