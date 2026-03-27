Got you 👍 — I’ll cleanly add your **Colour Detection project** in the same style (and fix that incorrect description too).

Here’s your updated `README.md` 👇

---

````markdown
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
````

**Features:**

* Real-time eye tracking via webcam
* EAR (Eye Aspect Ratio) based detection
* Auto alarm using pygame (no audio file needed)
* Visual countdown bar on screen

**Libraries:** `opencv-python`, `pygame`, `numpy`

---

### ✅ 2. Colour Detection

> Detect and track colored objects in real-time using HSV color space.

**Run:**

```bash
cd colour_detection
python main.py
```

**Features:**

* Real-time color detection using webcam
* Supports multiple colors: Red, Green, Blue, Yellow, Black, White
* HSV-based masking for accurate detection
* Noise removal using morphological operations
* Object tracking with bounding boxes and center points
* Live mask preview on screen
* Keyboard controls to switch between colors

**Controls:**

* `1` → Red
* `2` → Green
* `3` → Blue
* `4` → Yellow
* `5` → Black
* `6` → White
* `Q` → Quit

**Libraries:** `opencv-python`, `numpy`

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
│   └── README.md
│
├── colour_detection/
│   ├── main.py
│   ├── requirements.txt
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

| Tool       | Purpose                  |
| ---------- | ------------------------ |
| Python 3.x | Core language            |
| OpenCV     | Video & image processing |
| pygame     | Audio/alarm              |
| NumPy      | Math & array operations  |

---

> ⭐ More projects being added regularly!