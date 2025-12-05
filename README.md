🚗 Real-Time Vehicle Counter using YOLOv8

This project counts vehicles in a video using YOLOv8 object detection. It identifies moving vehicles and counts how many cross a selected region.



🧠 Technologies Used

✓ Python
✓ YOLOv8 (Ultralytics)
✓ OpenCV
✓ NumPy
✓ Pandas



▶ How to Run the Project

Step 1: Install required libraries

pip install -r requirements.txt

Step 2: Download YOLOv8 model weights

Download from here:
https://github.com/ultralytics/ultralytics/releases

Choose:
yolov8n.pt

After downloading → place it inside your project folder.

Step 3: Run the program

Use this command:

python count.py



🎯 Key Features

✔ Detects vehicles from video
✔ Counts vehicles crossing the frame
✔ Shows bounding boxes on vehicles
✔ Supports MP4 input videos


 Files in This Project

File Name	Purpose

count.py	Main detection and counting script
traffic.mp4	Sample test video input
requirements.txt	Dependencies
README.md	Documentation




🚀 Future Scope

🔹 Category-wise counting (Car, Bus, Truck)
🔹 Real-time camera input
🔹 Dashboard to display stats

