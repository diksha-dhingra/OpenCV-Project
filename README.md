# 👁️ OpenCV Projects Collection

A growing collection of real-time computer vision projects built with Python + OpenCV.

---

## 🚀 Projects

### ✅ 1. Drowsiness Detector
> Detects if eyes are closed for more than 10 seconds and triggers an alarm.

**Run:**
```bash
cd drowsiness_detector
python main.py
```

**Features:**
- Real-time eye tracking via webcam
- EAR (Eye Aspect Ratio) based detection
- Auto alarm using pygame (no audio file needed)
- Visual countdown bar on screen

**Libraries:** `opencv-python`, `mediapipe`, `pygame`, `numpy`

---

### 🔜 2. Hand Detection *(Coming Soon)*
> Detect and track hand landmarks in real-time using MediaPipe Hands.

---

## 🛠️ General Setup

Make sure Python is installed, then for any project:
```bash
pip install -r requirements.txt
python main.py
```

## 📁 Folder Structure
```
opencv-projects/
├── drowsiness_detector/
│   ├── main.py
│   ├── eye_detector.py
│   ├── alarm.py
│   ├── requirements.txt
│   └── README.md  ← (this file)
│
├── hand_detection/        ← coming soon
```

## 💡 How to Add a New Project

1. Create a new folder with the project name
2. Add `main.py`, `requirements.txt` inside it
3. Update this README — add entry under **Projects** section
4. Change `🔜 Coming Soon` to `✅` when done!

---

## 🧑‍💻 Tech Stack

| Tool        | Purpose                  |
|-------------|--------------------------|
| Python 3.x  | Core language            |
| OpenCV      | Video & image processing |
| pygame      | Audio/alarm              |
| NumPy       | Math & array operations  |

---

> ⭐ More projects being added regularly!
