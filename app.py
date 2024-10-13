from flask import Flask, render_template, send_file
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

# PostgreSQL database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="attendance",
        user="postgres",
        password="#password"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()

    # Fetch attendance records
    cur.execute("SELECT name, date, course FROM attendance")
    attendance_records = cur.fetchall()

    # Fetch overall course summary
    cur.execute("SELECT course, COUNT(*) FROM attendance GROUP BY course ORDER BY course")
    course_summary = cur.fetchall()

    # Fetch daily attendance summary
    cur.execute("SELECT date, COUNT(*) FROM attendance GROUP BY date ORDER BY date")
    daily_summary = cur.fetchall()

    # Fetch weekly attendance trend
    cur.execute("SELECT EXTRACT(DOW FROM date) AS day_of_week, COUNT(*) FROM attendance GROUP BY day_of_week ORDER BY day_of_week")
    weekly_trend = cur.fetchall()
    
    conn.close()

    # Days of the week for mapping
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    weekly_trend = [(days_of_week[int(day)], count) for day, count in weekly_trend]

    return render_template(
        'index.html',
        records=attendance_records,
        course_summary=course_summary,
        daily_summary=daily_summary,
        weekly_trend=weekly_trend
    )

# Course Distribution Bar Chart
@app.route('/plot/course-distribution-bar.png')
def course_distribution_bar():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT course, COUNT(*) FROM attendance GROUP BY course ORDER BY course")
    records = cur.fetchall()
    conn.close()

    df = pd.DataFrame(records, columns=['course', 'count'])
    fig, ax = plt.subplots()
    df.plot(x='course', y='count', kind='bar', ax=ax)
    ax.set_title('Course-wise Attendance Count')
    ax.set_xlabel('Course')
    ax.set_ylabel('Attendance Count')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

# Course Attendance Pie Chart
@app.route('/plot/course-distribution-pie.png')
def course_distribution_pie():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT course FROM attendance")
    attendance_records = cur.fetchall()
    conn.close()

    df = pd.DataFrame(attendance_records, columns=['course'])
    course_distribution = df['course'].value_counts()

    fig, ax = plt.subplots()
    course_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax)
    ax.set_ylabel('')
    ax.set_title('Course Attendance Distribution (Pie)')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

# Attendance Heatmap (Pie Chart by Day of the Week)
@app.route('/plot/attendance-pie-heatmap.png')
def attendance_pie_heatmap():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT EXTRACT(DOW FROM date) AS day_of_week, COUNT(*) FROM attendance GROUP BY day_of_week ORDER BY day_of_week")
    records = cur.fetchall()
    conn.close()

    # Days of the week for plotting
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    df = pd.DataFrame(records, columns=['day_of_week', 'count'])
    df['day_of_week'] = df['day_of_week'].apply(lambda x: days_of_week[int(x)])

    fig, ax = plt.subplots()
    df.set_index('day_of_week').plot(kind='pie', y='count', autopct='%1.1f%%', startangle=90, ax=ax, legend=False)
    ax.set_ylabel('')
    ax.set_title('Attendance Distribution by Day of the Week')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
