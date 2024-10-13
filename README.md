# Attendance Web App 🎓📊

This is a **Face Recognition Attendance System** that uses a webcam to automatically recognize students and logs their attendance into a PostgreSQL database. The system also provides a web dashboard to visualize attendance data, making it perfect for managing classroom attendance efficiently—no manual roll calls required! 📋🎉

## 🚀 Features

- 🎥 **Real-Time Face Recognition** using your webcam.
- 🗃️ **Database Logging**: Attendance is logged into a PostgreSQL database with the current date and time.
- 🖥️ **Web Dashboard**: Visualizes attendance data with basic charts and tables.
- 👁️ **On-Screen Display**: Shows which students are recognized and present.
- 🛠️ **Easily Customizable**: Add or remove student images for recognition effortlessly.

## 🛠️ Technologies Used

- 🐍 **Python**: Core programming language.
- 👁️ **OpenCV**: For capturing and displaying the webcam feed.
- 🤖 **face_recognition**: Library for detecting and recognizing faces.
- 🗃️ **PostgreSQL**: Database for storing attendance records.
- 🌐 **Flask**: Web framework to create the dashboard.
- 📊 **Chart.js**: Library for visualizing attendance data on the web.

## 🎒 How It Works

1. 📸 **Load Student Faces**: The system loads images of students and encodes their facial features for recognition.
2. 🎥 **Capture Webcam Feed**: Continuously processes live video from your webcam to detect faces.
3. 🧠 **Recognize Faces**: If a face matches, it marks the student as present and logs the attendance into the PostgreSQL database.
4. 🗃️ **Database Logging**: Attendance data (name, date, time) is stored in a PostgreSQL database.
5. 🌐 **Web Dashboard**: Displays attendance records in an interactive and easy-to-use format.

## 📋 Getting Started

### 🛠️ Clone the Repository

```bash
https://github.com/Manurajyadav/Attendance-System-Using-Face-Recognition.git
```
## 📦 Install the Required Libraries

To get started, install the dependencies using the following command:

```bash
pip install -r requirements.txt
```
## 🖼️ Add Student Images

Place the images of the students you want to recognize in the `faces/` folder. For each student, ensure that the filename reflects the student's name (e.g., `manu.jpg` for "Manu").

## 🗃️ Set Up the Database

1. Install PostgreSQL and set up a database named `attendance`.
2. Create a table to store attendance records:

```sql
CREATE TABLE attendance_records (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    date DATE,
    time TIME
);
```
## 🔑 Update Credentials

Update `app.py` and `main.py` with your PostgreSQL credentials to connect to the database.

## ▶️ Run the Program

### Face Recognition Attendance System

Once the student images are added, and the database is set up, run the face recognition script:

```bash
python main.py
```
## 📊 Web Dashboard

To launch the web dashboard that visualizes attendance records, run the following command:

```bash
python app.py
```
Then, visit the dashboard at http://127.0.0.1:5000/ in your web browser.
## 📂 Database Output Example

Attendance records will be stored in the PostgreSQL database in the following format:

| Name | Date       | Course   |
|------|------------|----------|
| Manu | 2024-10-13 |   AI     |

## ✏️ Customizing

To add more students to the recognition system:

1. 🖼️ Place their images in the `faces/` folder.
2. 📝 Update the `main.py` script to include the new faces in the recognition list.

## 📊 Web Dashboard

The dashboard displays attendance records in a table and visualizes attendance data using **Chart.js**. You can customize the charts by modifying the `index.html` file.

## 🛡️ Privacy

🔒 This system operates entirely on your local machine, and no data is shared online. Your data remains private and secure.

## 🚀 Future Improvements

- Integration with additional databases or cloud storage options.
- SMS/email notifications for marked attendance.
- Improved data analytics and visualizations.
