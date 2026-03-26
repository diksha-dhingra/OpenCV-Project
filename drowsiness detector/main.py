# main.py
# ── Drowsiness Detector ──
# If eyes are closed for more than 10 seconds → ALARM!

import cv2
import mediapipe as mp
import time

from eye_detector import are_eyes_closed
from alarm import play_alarm, stop_alarm

# ──────────────────────────────────────────
# Settings
# ──────────────────────────────────────────
CLOSED_EYE_LIMIT = 10      # seconds before alarm triggers
FONT = cv2.FONT_HERSHEY_SIMPLEX

# ──────────────────────────────────────────
# Setup MediaPipe Face Mesh
# ──────────────────────────────────────────
mp_face_mesh = mp.solutions.face_mesh
face_mesh    = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

# ──────────────────────────────────────────
# Start Webcam
# ──────────────────────────────────────────
cap = cv2.VideoCapture(0)   # 0 = default webcam

if not cap.isOpened():
    print("Cannot open webcam. Check your camera.")
    exit()

print("Drowsiness Detector Started. Press 'Q' to quit.")

# ──────────────────────────────────────────
# Tracking variables
# ──────────────────────────────────────────
eyes_closed_start = None
alarm_triggered   = False

# ──────────────────────────────────────────
# Main Loop
# ──────────────────────────────────────────
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame.")
        break

    frame = cv2.flip(frame, 1)   # Mirror effect
    img_h, img_w = frame.shape[:2]

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results   = face_mesh.process(rgb_frame)

    status_text  = "No Face Detected"
    status_color = (100, 100, 100)

    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0]
        closed, ear_value = are_eyes_closed(face_landmarks, img_w, img_h)

        if closed:
            if eyes_closed_start is None:
                eyes_closed_start = time.time()

            elapsed = time.time() - eyes_closed_start

            status_text  = f"Eyes CLOSED  {elapsed:.1f}s"
            status_color = (0, 60, 255)

            # Countdown bar at the bottom
            bar_width = int((elapsed / CLOSED_EYE_LIMIT) * img_w)
            bar_width = min(bar_width, img_w)
            cv2.rectangle(frame, (0, img_h - 20), (bar_width, img_h), (0, 60, 255), -1)

            if elapsed >= CLOSED_EYE_LIMIT:
                alarm_triggered = True
                play_alarm()
                cv2.putText(frame, "!! WAKE UP !!", (img_w//2 - 130, img_h//2),
                            FONT, 1.4, (0, 0, 255), 3)
        else:
            eyes_closed_start = None
            alarm_triggered   = False
            stop_alarm()

            status_text  = f"Eyes OPEN   EAR: {ear_value}"
            status_color = (0, 200, 80)

        cv2.putText(frame, f"EAR: {ear_value}", (img_w - 140, 30),
                    FONT, 0.65, (255, 255, 0), 2)

    # Status bar at top
    cv2.rectangle(frame, (0, 0), (img_w, 45), (30, 30, 30), -1)
    cv2.putText(frame, status_text, (10, 30), FONT, 0.75, status_color, 2)

    cv2.imshow("Drowsiness Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ──────────────────────────────────────────
# Cleanup
# ──────────────────────────────────────────
cap.release()
cv2.destroyAllWindows()
stop_alarm()
print("Detector stopped.")