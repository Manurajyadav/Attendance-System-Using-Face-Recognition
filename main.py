import face_recognition
import cv2
import numpy as np
import psycopg2
from datetime import datetime, time

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",      # Replace with your host
    database="attendance",  # Replace with your database name
    user="postgres",       # Replace with your database user
    password="password"  # Replace with your password
)

# Create a cursor object
cur = conn.cursor()

# Create the attendance table if it doesn't exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        name VARCHAR(50),
        date DATE,
        time TIME,
        course VARCHAR(50)  -- Add course column to store course name
    )
''')
conn.commit()

# Load the background image
imgBackground = cv2.imread("background.jpg")

# Load known faces
manu_image = face_recognition.load_image_file("faces/manu.jpg")
manu_encoding = face_recognition.face_encodings(manu_image)[0]

utkarsh_image = face_recognition.load_image_file("faces/Utkarsh.jpg")
utkarsh_encoding = face_recognition.face_encodings(utkarsh_image)[0]

shashank_image = face_recognition.load_image_file("faces/Shashank.jpg")
shashank_encoding = face_recognition.face_encodings(shashank_image)[0]

# rajesh_image = face_recognition.load_image_file("faces/Rajesh.jpg")
# rajesh_encoding = face_recognition.face_encodings(rajesh_image)[0]

known_face_encodings = [manu_encoding, utkarsh_encoding, shashank_encoding]
known_face_names = ["Manu", "Utkarsh", "Shashank"]

# List of expected students
students = known_face_names.copy()

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    # Resize the frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distance)

        name = ""  # Initialize variable to avoid undefined error
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        if name in known_face_names:
            # Scale face locations back to the original frame size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a rectangle around the faces
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Display the person's name and "Present" text below the face
            cv2.putText(frame, f"{name} Present", (left, bottom + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

            if name in students:
                students.remove(name)
                now = datetime.now()
                current_time = now.time()  # Get current time
                current_date = now.strftime("%Y-%m-%d")
                course = ""

                # Directly check the time in the if conditions
                if time(9, 30, 0) <= current_time <= time(10, 30, 0):
                    course = "Cloud Computing"
                elif time(10, 30, 0) <= current_time <= time(11, 30, 0):
                    course = "Soft Computing"
                elif time(11, 30, 0) <= current_time <= time(1, 30, 0):
                    course = "IOT Lab"
                elif time(1, 30, 0) <= current_time <= time(2, 30, 0):
                    course = "Machine Learning"
                elif time(2, 30, 0) <= current_time <= time(3, 30, 0):
                    course = "Data Science"
                elif time(3, 30, 0) <= current_time <= time(4, 30, 0):
                    course = "Modeling & Simulation"
                elif time(4, 30, 0) <= current_time <= time(5, 30, 0):
                    course = "Internet of Things"
                else:
                    course = "No Course Scheduled"

                # Print to console (for debugging)
                print(f"Recording attendance: {name}, Date: {current_date}, Course: {course}")

                # Insert attendance record into PostgreSQL
                cur.execute('''
                    INSERT INTO attendance (name, date, course)
                    VALUES (%s, %s, %s)
                ''', (name, current_date, course))
                conn.commit()  # Commit the transaction

    # Resize and display the video frame on top of the background
    frame_resized = cv2.resize(frame, (640, 480))
    imgBackground[162:162 + 480, 55:55 + 640] = frame_resized
    cv2.imshow("Attendance", imgBackground)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Close database connection
cur.close()
conn.close()

# Release the video capture and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
