# eye_detector.py
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade  = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

def are_eyes_closed(frame):
    gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return None  # No face detected

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes     = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes) >= 2:
            return False  # Eyes open
        else:
            return True   # Eyes closed

    return None