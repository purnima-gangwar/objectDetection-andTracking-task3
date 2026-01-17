📌 Project Overview

This project implements a real-time object detection and tracking system using **YOLO (You Only Look Once) and OpenCV.
The system detects objects through a webcam and assigns a unique ID to each detected object while tracking it across frames.

This project was developed as part of Task 4 of my internship, following all the given requirements.

 🚀 Features

 Real-time object detection using YOLO
 Webcam-based live detection
 Object tracking with unique ID assignment
 Bounding boxes displayed on detected objects
 Green-colored bounding box for clear visualization
 Smooth real-time performance

 🛠️ Technologies Used
 Python
 OpenCV
 YOLO (Ultralytics)
 FilterPy
 Scikit-image
 Matplotlib

 📂 Project Structure
 
Task4_ObjectDetection/
│
├── main.py              # Main execution file
├── requirements.txt     # Required libraries
├── yolov8n.pt           # YOLO model file
└── venv/                # Virtual environment

 ⚙️ Installation & Setup
 1️⃣ Create & Activate Virtual Environment

 2️⃣ Install Required Libraries
pip install -r requirements.txt
(This is a one-time setup)

 ▶️ How to Run the Project
Run the following command in the terminal:
 python main.py
 Webcam will open automatically
 Detected objects will be highlighted with green bounding boxes
 Each object will have a unique tracking ID

To stop the program:
 Press ESC on the camera window
  or
 Press Ctrl + C in terminal
 

🧪 Working Explanation
 YOLO model detects objects from the webcam feed
 Detected objects are tracked frame-by-frame
 Each object is assigned a unique ID
 Bounding boxes and IDs are displayed in real time


 ✅ Task Requirements Fulfilled
✔ Real-time detection
✔ Object tracking
✔ Unique ID assignment
✔ Webcam integration
✔ Proper visualization

All requirements mentioned in Task 4 have been successfully implemented.


📸 Output
 Live webcam feed
 Objects detected with green bounding boxes
 Unique ID displayed above each object


👩‍💻 Author
Purnima Gangwar

