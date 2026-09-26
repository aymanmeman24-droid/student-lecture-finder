from flask import Flask, jsonify, send_file
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = "lectures.db"


# =====================================================
# STUDENT DATA
# =====================================================

students = [
    # CP1
    ("CE01", "CP1"),
    ("CE03", "CP1"),
    ("CE04", "CP1"),
    ("CE05", "CP1"),
    ("CE06", "CP1"),
    ("CE07", "CP1"),
    ("CE09", "CP1"),
    ("CE10", "CP1"),
    ("CE14", "CP1"),
    ("CE17", "CP1"),
    ("CE19", "CP1"),
    ("CE21", "CP1"),
    ("CE24", "CP1"),
    ("CE78", "CP1"),
    ("CE79", "CP1"),
    ("CE82", "CP1"),
    ("CE86", "CP1"),
    ("CE87", "CP1"),
    ("CE88", "CP1"),
    ("CE91", "CP1"),
    ("CE92", "CP1"),
    ("CE93", "CP1"),
    ("CE94", "CP1"),
    ("CE95", "CP1"),
    ("CE96", "CP1"),

    # CP2
    ("CE26", "CP2"),
    ("CE28", "CP2"),
    ("CE29", "CP2"),
    ("CE30", "CP2"),
    ("CE31", "CP2"),
    ("CE32", "CP2"),
    ("CE33", "CP2"),
    ("CE34", "CP2"),
    ("CE37", "CP2"),
    ("CE38", "CP2"),
    ("CE39", "CP2"),
    ("CE40", "CP2"),
    ("CE41", "CP2"),
    ("CE42", "CP2"),
    ("CE43", "CP2"),
    ("CE45", "CP2"),
    ("CE46", "CP2"),
    ("CE49", "CP2"),
    ("CE97", "CP2"),
    ("CE98", "CP2"),
    ("CE99", "CP2"),
    ("CE100", "CP2"),
    ("CE101", "CP2"),
    ("CE102", "CP2"),
    ("CE103", "CP2"),

    # CP3
    ("CE52", "CP3"),
    ("CE53", "CP3"),
    ("CE55", "CP3"),
    ("CE56", "CP3"),
    ("CE57", "CP3"),
    ("CE58", "CP3"),
    ("CE59", "CP3"),
    ("CE61", "CP3"),
    ("CE62", "CP3"),
    ("CE63", "CP3"),
    ("CE65", "CP3"),
    ("CE66", "CP3"),
    ("CE68", "CP3"),
    ("CE70", "CP3"),
    ("CE72", "CP3"),
    ("CE73", "CP3"),
    ("CE74", "CP3"),
    ("CE76", "CP3"),
    ("CE77", "CP3"),
    ("CE104", "CP3"),
    ("CE105", "CP3"),
    ("CE106", "CP3"),
    ("CE107", "CP3"),
    ("CE108", "CP3"),
    ("CE109", "CP3"),
    ("CE110", "CP3"),
    ("CE111", "CP3"),
    ("CE112", "CP3")
]


# =====================================================
# COMMON LECTURES
# =====================================================

common_lectures = [

    ("Monday", "10:30 AM", "11:30 AM",
     "BME", "AKP", "8109"),

    ("Monday", "11:30 AM", "12:30 PM",
     "PPS", "KMG", "8109"),

    ("Monday", "01:00 PM", "02:00 PM",
     "MATHS-1", "DAP", "8109"),

    ("Monday", "02:00 PM", "03:00 PM",
     "BEE", "JHP", "8109"),

    ("Tuesday", "10:30 AM", "11:30 AM",
     "BEE", "JHP", "8109"),

    ("Tuesday", "11:30 AM", "12:30 PM",
     "BME", "PNB", "8109"),

    ("Wednesday", "10:30 AM", "11:30 AM",
     "MATHS-1", "DAP", "8109"),

    ("Wednesday", "11:30 AM", "12:30 PM",
     "BME", "PNB", "8109"),

    ("Wednesday", "01:00 PM", "03:00 PM",
     "IPDC", "CGP", "8012"),

    ("Thursday", "10:30 AM", "11:30 AM",
     "PPS", "KMG", "8109"),

    ("Thursday", "11:30 AM", "12:30 PM",
     "BEE", "JHP", "8109"),

    ("Friday", "01:00 PM", "03:00 PM",
     "LIBRARY / S.L.", "-", "-"),

    ("Friday", "03:10 PM", "05:10 PM",
     "LIBRARY / S.L.", "-", "-")
]


# =====================================================
# BATCH-SPECIFIC LECTURES
# =====================================================

batch_lectures = {

    "CP1": [

        ("Monday", "03:10 PM", "05:10 PM",
         "MATHS 1", "DAP", "8109"),

        ("Tuesday", "01:00 PM", "03:00 PM",
         "PPS", "KMG", "8114"),

        ("Tuesday", "03:10 PM", "05:10 PM",
         "BEE", "JHP", "4010"),

        ("Wednesday", "03:10 PM", "05:10 PM",
         "BME", "BDP", "5112"),

        ("Thursday", "01:00 PM", "03:00 PM",
         "DFWS", "MGP", "4009"),

        ("Thursday", "03:10 PM", "05:10 PM",
         "S.L. / LIB.", "-", "-"),

        ("Friday", "10:30 AM", "12:30 PM",
         "PPS", "VF", "8114")
    ],

    "CP2": [

        ("Monday", "03:10 PM", "05:10 PM",
         "MATHS 1", "VF", "8109"),

        ("Tuesday", "01:00 PM", "03:00 PM",
         "PPS", "VF", "8114"),

        ("Tuesday", "03:10 PM", "05:10 PM",
         "DFWS", "MGP", "4009"),

        ("Wednesday", "03:10 PM", "05:10 PM",
         "S.L. / LIB.", "-", "-"),

        ("Thursday", "01:00 PM", "03:00 PM",
         "BME", "ADP", "5112"),

        ("Thursday", "03:10 PM", "05:10 PM",
         "PPS", "KMG", "8114"),

        ("Friday", "10:30 AM", "12:30 PM",
         "BEE", "JHP", "4010")
    ],

    "CP3": [

        ("Monday", "03:10 PM", "05:10 PM",
         "MATHS 1", "VF", "8109"),

        ("Tuesday", "01:00 PM", "03:00 PM",
         "BME", "BDP", "5112"),

        ("Tuesday", "03:10 PM", "05:10 PM",
         "S.L. / LIB.", "-", "-"),

        ("Wednesday", "03:10 PM", "05:10 PM",
         "DFWS", "BRP", "4009"),

        ("Thursday", "01:00 PM", "03:00 PM",
         "BEE", "JHP", "4010"),

        ("Thursday", "03:10 PM", "05:10 PM",
         "PPS", "VF", "8114"),

        ("Friday", "10:30 AM", "12:30 PM",
         "PPS", "KMG", "8114")
    ]
}


# =====================================================
# HELPER FUNCTIONS
# =====================================================

def time_to_minutes(time_string):

    parts = time_string.split()

    time_part = parts[0]
    period = parts[1]

    hours, minutes = map(
        int,
        time_part.split(":")
    )

    if period == "PM" and hours != 12:
        hours += 12

    if period == "AM" and hours == 12:
        hours = 0

    return hours * 60 + minutes


def get_day_number(day):

    days = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
    }

    return days.get(day, 99)


# =====================================================
# CREATE DATABASE
# =====================================================

def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS students")
    cursor.execute("DROP TABLE IF EXISTS lectures")

    # -----------------------------
    # STUDENTS TABLE
    # -----------------------------

    cursor.execute("""
        CREATE TABLE students (

            enrollment TEXT PRIMARY KEY,

            batch TEXT NOT NULL

        )
    """)

    # -----------------------------
    # LECTURES TABLE
    # -----------------------------

    cursor.execute("""
        CREATE TABLE lectures (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            enrollment TEXT NOT NULL,

            day TEXT NOT NULL,

            start_time TEXT NOT NULL,

            end_time TEXT NOT NULL,

            subject TEXT NOT NULL,

            professor TEXT NOT NULL,

            room TEXT NOT NULL

        )
    """)

    # Insert students

    cursor.executemany(
        """
        INSERT INTO students
        (enrollment, batch)

        VALUES (?, ?)
        """,
        students
    )

    # Insert lectures

    for enrollment, batch in students:

        lectures = (
            common_lectures.copy()
            +
            batch_lectures[batch].copy()
        )

        lectures.sort(
            key=lambda lecture: (
                get_day_number(lecture[0]),
                time_to_minutes(lecture[1])
            )
        )

        for lecture in lectures:

            cursor.execute(
                """
                INSERT INTO lectures
                (
                    enrollment,
                    day,
                    start_time,
                    end_time,
                    subject,
                    professor,
                    room
                )

                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    enrollment,
                    lecture[0],
                    lecture[1],
                    lecture[2],
                    lecture[3],
                    lecture[4],
                    lecture[5]
                )
            )

    conn.commit()

    conn.close()


# =====================================================
# FRONTEND ROUTES
# =====================================================

@app.route("/")
def home():

    return send_file("index.html")


@app.route("/today.html")
def today():

    return send_file("today.html")


@app.route("/yesterday.html")
def yesterday():

    return send_file("yesterday.html")


@app.route("/tomorrow.html")
def tomorrow():

    return send_file("tomorrow.html")


@app.route("/timetable.html")
def timetable():

    return send_file("timetable.html")


@app.route("/style.css")
def style():

    return send_file("style.css")


@app.route("/script.js")
def script():

    return send_file("script.js")


# =====================================================
# API — GET STUDENT LECTURES
# =====================================================

@app.route("/api/lectures/<enrollment>")
def get_lectures(enrollment):

    enrollment = enrollment.strip().upper()

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    # Check student first

    cursor.execute(
        """
        SELECT enrollment, batch
        FROM students
        WHERE enrollment = ?
        """,
        (enrollment,)
    )

    student = cursor.fetchone()

    # Invalid enrollment

    if student is None:

        conn.close()

        return jsonify({
            "success": False,
            "message": "Enrollment number not found.",
            "enrollment": enrollment,
            "lectures": []
        }), 404

    # Get lectures

    cursor.execute(
        """
        SELECT
            id,
            enrollment,
            day,
            start_time,
            end_time,
            subject,
            professor,
            room

        FROM lectures

        WHERE enrollment = ?

        ORDER BY
            CASE day

                WHEN 'Monday' THEN 1
                WHEN 'Tuesday' THEN 2
                WHEN 'Wednesday' THEN 3
                WHEN 'Thursday' THEN 4
                WHEN 'Friday' THEN 5
                WHEN 'Saturday' THEN 6
                WHEN 'Sunday' THEN 7

            END,

            id
        """,
        (enrollment,)
    )

    rows = cursor.fetchall()

    conn.close()

    lectures = [
        dict(row)
        for row in rows
    ]

    return jsonify({

        "success": True,

        "message": "Lectures found.",

        "student": {
            "enrollment": student["enrollment"],
            "batch": student["batch"]
        },

        "total_lectures": len(lectures),

        "lectures": lectures

    })


# =====================================================
# API — STUDENT INFORMATION
# =====================================================

@app.route("/api/student/<enrollment>")
def get_student(enrollment):

    enrollment = enrollment.strip().upper()

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT enrollment, batch
        FROM students
        WHERE enrollment = ?
        """,
        (enrollment,)
    )

    student = cursor.fetchone()

    conn.close()

    if student is None:

        return jsonify({

            "success": False,

            "message": "Enrollment number not found."

        }), 404

    return jsonify({

        "success": True,

        "student": {

            "enrollment": student["enrollment"],

            "batch": student["batch"]

        }

    })


# =====================================================
# API — HEALTH CHECK
# =====================================================

@app.route("/api/health")
def health_check():

    return jsonify({

        "success": True,

        "message": "Student Lecture Finder API is running.",

        "status": "online",

        "server_time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

    })


# =====================================================
# START SERVER
# =====================================================

create_database()


if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )