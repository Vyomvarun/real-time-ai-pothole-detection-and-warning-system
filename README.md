# 🚧 Real-Time AI Pothole Detection and Driver Warning System

An AI-powered real-time pothole detection and driver warning system developed using **YOLOv8**, **OpenCV**, and **Python**.

## 📌 Features

- Real-Time Pothole Detection
- Custom Trained YOLOv8 Model
- Webcam and Video Support
- Bounding Box Detection
- Confidence Score Display
- Pothole Counter
- FPS Monitoring
- Warning Banner
- Smart Beep Alert
- Screenshot Capture
- Output Video Saving

## 🛠 Tech Stack

- Python
- OpenCV
- YOLOv8
- Ultralytics
- NumPy

## 📂 Project Structure

```text
best.pt      -> Trained Model
detect.py    -> Main Code
road.mp4     -> Test Video
road.png     -> Sample Image
README.md
```

## 🚀 How to Run

```bash
pip install ultralytics
pip install opencv-python
pip install numpy

python detect.py
```

## 🧠 How It Works

1. Capture video from webcam or file.
2. Apply Gaussian Blur and Brightness Enhancement.
3. Send frames to YOLOv8 model.
4. Detect potholes in real-time.
5. Display alerts, confidence and pothole count.

## 🎯 Future Scope

- GPS Based Alerts
- Voice Warning System
- Distance Estimation
- Lane Detection
- ADAS Integration

## 👨‍💻 Author

**Vyom Varun**  
B.Tech CSE | AI & Computer Vision Enthusiast
