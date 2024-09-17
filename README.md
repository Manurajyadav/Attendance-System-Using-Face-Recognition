# Face Recognition Attendance System 🎓🤖

This is a real-time **Face Recognition Attendance System** that automatically marks attendance using your webcam. The system recognizes students based on their faces and logs their attendance into a CSV file—no manual roll calls required! 📋🎉

## 🚀 Features
- 🎥 **Real-Time Face Recognition** using your webcam.
- 📁 **Automated Attendance Logging** into a CSV file with the current date.
- 🖥️ **On-Screen Display** showing which students are recognized.
- 🛠️ **Customizable** by adding/removing student images easily.

## 🛠️ Technologies Used
- 🐍 **Python**: Core programming language.
- 👁️ **OpenCV**: For capturing and displaying the webcam feed.
- 🤖 **face_recognition**: Library for recognizing faces.
- 📝 **CSV**: For saving attendance logs.

## 🎒 How It Works
1. 📸 **Load Student Faces**: The system loads images of students and encodes their facial features.
2. 🎥 **Capture Webcam Feed**: It continuously processes live video from your webcam.
3. 🧠 **Recognize Faces**: If a student's face matches, it marks them as present and logs the time in a CSV file.
4. 📝 **CSV Logging**: Attendance is saved with the student’s name and the time they were marked present.

## 📋 Getting Started
1. 🛠️ **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/face-recognition-attendance.git
2. 📦 Install the Required Libraries
To get started, you need to install the required dependencies:

   ```bash
   pip install opencv-python numpy face_recognition
3. 🖼️ Add Student Images
Place the images of the students you want to recognize in the faces/ folder.

4. ▶️ Run the Program
Once the dependencies are installed and the images are ready, run the program:
   ```bash
   python attendance_system.py
## 📂 CSV Output Example
Each day, a new CSV file will be created with attendance logs like this:

Name      | Time
---------------------
Manu      | 09:15:21 AM


## ✏️ Customizing
To add more students:

1. 🖼️ Place their images in the `faces/` folder.
2. 📝 Update the script to include the new faces in the recognition list.

## 🛡️ Privacy
🔒 This system works entirely on your **local machine**, and no data is shared online.

