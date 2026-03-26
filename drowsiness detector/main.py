# main.py
import cv2
import time
from eye_detector import are_eyes_closed
from alarm import play_alarm, stop_alarm

CLOSED_EYE_LIMIT = 10
FONT = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam.")
    exit()

print("Drowsiness Detector Started. Press 'Q' to quit.")

eyes_closed_start = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame        = cv2.flip(frame, 1)
    img_h, img_w = frame.shape[:2]
    status_text  = "No Face Detected"
    status_color = (100, 100, 100)

    result = are_eyes_closed(frame)

    if result is True:
        if eyes_closed_start is None:
            eyes_closed_start = time.time()

        elapsed   = time.time() - eyes_closed_start
        status_text  = f"Eyes CLOSED  {elapsed:.1f}s"
        status_color = (0, 60, 255)

        bar_width = min(int((elapsed / CLOSED_EYE_LIMIT) * img_w), img_w)
        cv2.rectangle(frame, (0, img_h - 20), (bar_width, img_h), (0, 60, 255), -1)

        if elapsed >= CLOSED_EYE_LIMIT:
            play_alarm()
            cv2.putText(frame, "!! WAKE UP !!", (img_w//2 - 130, img_h//2),
                        FONT, 1.4, (0, 0, 255), 3)

    elif result is False:
        eyes_closed_start = None
        stop_alarm()
        status_text  = "Eyes OPEN"
        status_color = (0, 200, 80)

    cv2.rectangle(frame, (0, 0), (img_w, 45), (30, 30, 30), -1)
    cv2.putText(frame, status_text, (10, 30), FONT, 0.75, status_color, 2)
    cv2.imshow("Drowsiness Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
stop_alarm()
print("Detector stopped.")
### requirements.txt
opencv-python
pygame-ce
numpy