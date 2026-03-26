# eye_detector.py
# Handles detecting whether eyes are open or closed using MediaPipe landmarks

import numpy as np

# MediaPipe face mesh landmark indices for left and right eyes
LEFT_EYE  = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33,  160, 158, 133, 153, 144]

# EAR below this value = eyes considered closed
EAR_THRESHOLD = 0.25


def get_ear(landmarks, eye_points, img_w, img_h):
    """
    EAR = Eye Aspect Ratio
    Open eyes  → EAR ~0.30 or more
    Closed eyes → EAR drops below 0.25
    """
    coords = []
    for idx in eye_points:
        lm = landmarks[idx]
        coords.append((int(lm.x * img_w), int(lm.y * img_h)))

    # Vertical distances
    v1 = np.linalg.norm(np.array(coords[1]) - np.array(coords[5]))
    v2 = np.linalg.norm(np.array(coords[2]) - np.array(coords[4]))

    # Horizontal distance
    h  = np.linalg.norm(np.array(coords[0]) - np.array(coords[3]))

    ear = (v1 + v2) / (2.0 * h)
    return ear


def are_eyes_closed(face_landmarks, img_w, img_h):
    """
    Returns:
        closed    (bool)  → True if both eyes are closed
        avg_ear   (float) → EAR value for display/debugging
    """
    lm = face_landmarks.landmark

    left_ear  = get_ear(lm, LEFT_EYE,  img_w, img_h)
    right_ear = get_ear(lm, RIGHT_EYE, img_w, img_h)

    avg_ear = (left_ear + right_ear) / 2.0
    closed  = avg_ear < EAR_THRESHOLD

    return closed, round(avg_ear, 2)