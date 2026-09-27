from flask import Flask, jsonify, send_file
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = "lectures.db"


# =========================================================
# STUDENTS
# Enrollment + Name + Batch
# =========================================================

students = [

    # ================= CP1 =================

    ("CE01", "Kamalkumar Satishbhai Prajapati", "CP1"),
    ("CE03", "Bhumi Panchabhai Prajapati", "CP1"),
    ("CE04", "Mittalben Dolabhai Chaudhary", "CP1"),
    ("CE05", "Shlok Gautambhai Patel", "CP1"),
    ("CE06", "Nihal Rajeshkumar Chaudhari", "CP1"),
    ("CE07", "Bariya Chiragkumar", "CP1"),
    ("CE09", "Varunkumar Rajendrakumar Asari", "CP1"),
    ("CE10", "Riyu Kapildev Suthar", "CP1"),
    ("CE14", "Harsh Rajkishor Tiwari", "CP1"),
    ("CE17", "Tarunkumar Arvind Gupta", "CP1"),
    ("CE19", "Maitri Anilkumar Panchal", "CP1"),
    ("CE21", "Bhavishya Sureshbhai Ghediya", "CP1"),
    ("CE24", "Kamaxiben Prakashkumar Dabhi", "CP1"),
    ("CE78", "Thakor Jaydeep Jitendrasinh", "CP1"),
    ("CE79", "Nansiben Rajendrabhai Yadav", "CP1"),
    ("CE82", "Mahi Ashvinbhai Menat", "CP1"),
    ("CE86", "Bhuva Payal Ramji", "CP1"),
    ("CE87", "Nayanbhai Sureshbhai Purohit", "CP1"),
    ("CE88", "Dhakad Pratham Shailendrabhai", "CP1"),
    ("CE91", "Sisara Pragnesh Shamjibhai", "CP1"),
    ("CE92", "Mohammad Nijamuddin Junakiya", "CP1"),
    ("CE93", "Meena Ramashankar Kanojiya", "CP1"),
    ("CE94", "Jalpaben Ashokbhai Prajapati", "CP1"),
    ("CE95", "Jashkumar Ashwinbhai Prajapati", "CP1"),
    ("CE96", "Singh Kishan Dilip", "CP1"),

    # ================= CP2 =================

    ("CE26", "Sk Sahil Gayen", "CP2"),
    ("CE28", "Niraliben Dharamshibhai Sonagra", "CP2"),
    ("CE29", "Sahilkumar Khushalbhai Baivadiya", "CP2"),
    ("CE30", "Charmiben Yogeshkumar Modi", "CP2"),
    ("CE31", "Anushka Ashwinbhai Balsara", "CP2"),
    ("CE32", "Vardan Abhaykumar Gaur", "CP2"),
    ("CE33", "Diya Navinbhai Patel", "CP2"),
    ("CE34", "Mahiben Vishnuji Zala", "CP2"),
    ("CE37", "Chauhan Vishnubhai Pithabhai", "CP2"),
    ("CE38", "Bhavya Ashokbhai Prajapati", "CP2"),
    ("CE39", "Anirudhdh Nagbhai Jajda", "CP2"),
    ("CE40", "Vaghela Suryaprakashsinh Rajendrasinh", "CP2"),
    ("CE41", "Diyaben Vijaybhai Davda", "CP2"),
    ("CE42", "Himanshu Kumar Shailesh Kumar Sharma", "CP2"),
    ("CE43", "Jay Tulsidas Senghani", "CP2"),
    ("CE45", "Milan Mahendrabhai Maru", "CP2"),
    ("CE46", "Riyaben Lalitbhai Parmar", "CP2"),
    ("CE49", "Krishbhai Vajarambhai Brahman", "CP2"),
    ("CE97", "Ajwa Rahmatullah Moriya", "CP2"),
    ("CE98", "Gadhavi Anandsinh Arvinddan", "CP2"),
    ("CE99", "Dharana Jiteshbhai Moradiya", "CP2"),
    ("CE100", "Pandya Shrutiben Vipulkumar", "CP2"),
    ("CE101", "Jayeshbhai Bhikhabhai Chaudhary", "CP2"),
    ("CE102", "Ayaman Iqbalbhai Meman", "CP2"),
    ("CE103", "Ayushiben Bharatbhai Nai", "CP2"),

    # ================= CP3 =================

    ("CE52", "Harshadkumar Shanabhai Koli", "CP3"),
    ("CE53", "Parmar Yuvraj Galbabhai", "CP3"),
    ("CE55", "Modh Roshani Sanjaykumar", "CP3"),
    ("CE56", "Rina Babubhai Prajapati", "CP3"),
    ("CE57", "Singh Vishal Shankarkumar", "CP3"),
    ("CE58", "Shivan Harshadkumar Vaishnav", "CP3"),
    ("CE59", "Sakshi Karansinh Chauhan", "CP3"),
    ("CE61", "Bharvi Vijaykumar Patel", "CP3"),
    ("CE62", "Axit Manojbhai Prajapati", "CP3"),
    ("CE63", "Vaghela Harsiddh Chandanji", "CP3"),
    ("CE65", "Dhukka Mohammad M.Akram", "CP3"),
    ("CE66", "Harsh Nitinbhai Golaniya", "CP3"),
    ("CE68", "Mili Lalitkumar Patel", "CP3"),
    ("CE70", "Shankarbhai Ramabhai Dangar", "CP3"),
    ("CE72", "Priyanka Rameshbhai Hadiya", "CP3"),
    ("CE73", "Swet Ahokbhai Prajapati", "CP3"),
    ("CE74", "Sunasara Sheza Mobinali", "CP3"),
    ("CE76", "Chaudhary Dhavalkumar Bhavabhai", "CP3"),
    ("CE77", "Modi Bijal Ashokkumar", "CP3"),
    ("CE104", "Khushi Ankurbhai Modi", "CP3"),
    ("CE105", "Bhargav Boghabhai Pathak", "CP3"),
    ("CE106", "Aeiman Altafbhai Ajmeri", "CP3"),
    ("CE107", "Khushkumar Nareshbhai Thakkar", "CP3"),
    ("CE108", "Krishna Krunalbhai Soni", "CP3"),
    ("CE109", "Yash Kanabhai Solanki", "CP3"),
    ("CE110", "Kavya Rameshkumar Patel", "CP3"),
    ("CE111", "Chaudhary Divya Haribhai", "CP3"),
    ("CE112", "Neelkumar Vinodkumar Patel", "CP3")
]


# =========================================================
# COMMON LECTURES
# =========================================================

common_lectures = [

    ("Monday", "10:30 AM", "11:30 AM", "BME", "AKP", "8109"),
    ("Monday", "11:30 AM", "12:30 PM", "PPS", "KMG", "8109"),
    ("Monday", "01:00 PM", "02:00 PM", "MATHS-1", "DAP", "8109"),
    ("Monday", "02:00 PM", "03:00 PM", "BEE", "JHP", "8109"),

    ("Tuesday", "10:30 AM", "11:30 AM", "BEE", "JHP", "8109"),
    ("Tuesday", "11:30 AM", "12:30 PM", "BME", "PNB", "8109"),

    ("Wednesday", "10:30 AM", "11:30 AM", "MATHS-1", "DAP", "8109"),
    ("Wednesday", "11:30 AM", "12:30 PM", "BME", "PNB", "8109"),
    ("Wednesday", "01:00 PM", "03:00 PM", "IPDC", "CGP", "8012"),

    ("Thursday", "10:30 AM", "11:30 AM", "PPS", "KMG", "8109"),
    ("Thursday", "11:30 AM", "12:30 PM", "BEE", "JHP", "8109"),

    ("Friday", "01:00 PM", "03:00 PM", "LIBRARY / S.L.", "-", "-"),
    ("Friday", "03:10 PM", "05:10 PM", "LIBRARY / S.L.", "-", "-")
]


# =========================================================
# BATCH-WISE LECTURES
# =========================================================

batch_lectures = {

    "CP1": [
        ("Monday", "03:10 PM", "05:10 PM", "MATHS 1", "DAP", "8109"),
        ("Tuesday", "01:00 PM", "03:00 PM", "PPS", "KMG", "8114"),
        ("Tuesday", "03:10 PM", "05:10 PM", "BEE", "JHP", "4010"),
        ("Wednesday", "03:10 PM", "05:10 PM", "BME", "BDP", "5112"),
        ("Thursday", "01:00 PM", "03:00 PM", "DFWS", "MGP", "4009"),
        ("Thursday", "03:10 PM", "05:10 PM", "S.L. / LIB.", "-", "-"),
        ("Friday", "10:30 AM", "12:30 PM", "PPS", "VF", "8114")
    ],

    "CP2": [
        ("Monday", "03:10 PM", "05:10 PM", "MATHS 1", "VF", "8109"),
        ("Tuesday", "01:00 PM", "03:00 PM", "PPS", "VF", "8114"),
        ("Tuesday", "03:10 PM", "05:10 PM", "DFWS", "MGP", "4009"),
        ("Wednesday", "03:10 PM", "05:10 PM", "S.L. / LIB.", "-", "-"),
        ("Thursday", "01:00 PM", "03:00 PM", "BME", "ADP", "5112"),
        ("Thursday", "03:10 PM", "05:10 PM", "PPS", "KMG", "8114"),
        ("Friday", "10:30 AM", "12:30 PM", "BEE", "JHP", "4010")
    ],

    "CP3": [
        ("Monday", "03:10 PM", "05:10 PM", "MATHS 1", "VF", "8109"),
        ("Tuesday", "01:00 PM", "03:00 PM", "BME", "BDP", "5112"),
        ("Tuesday", "03:10 PM", "05:10 PM", "S.L. / LIB.", "-", "-"),
        ("Wednesday", "03:10 PM", "05:10 PM", "DFWS", "BRP", "4009"),
        ("Thursday", "01:00 PM", "03:00 PM", "BEE", "JHP", "4010"),
        ("Thursday", "03:10 PM", "05:10 PM", "PPS", "VF", "8114"),
        ("Friday", "10:30 AM", "12:30 PM", "PPS", "KMG", "8114")
    ]
}


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def time_to_minutes(time_string):
    time_object = datetime.strptime(time_string, "%I:%M %p")
    return time_object.hour * 60 + time_object.minute


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

    return days.get(day, 8)


# =========================================================
# CREATE DATABASE
# =========================================================

def create_database():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Remove old tables
    cursor.execute("DROP TABLE IF EXISTS students")
    cursor.execute("DROP TABLE IF EXISTS lectures")

    # Students table
    cursor.execute("""
        CREATE TABLE students (
            enrollment TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            batch TEXT NOT NULL
        )
    """)

    # Lectures table
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
        (enrollment, name, batch)
        VALUES (?, ?, ?)
        """,
        students
    )

    # Create lectures for every student
    for enrollment, name, batch in students:

        lectures = common_lectures.copy()

        lectures += batch_lectures[batch].copy()

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


# =========================================================
# PAGES
# =========================================================

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


# =========================================================
# GET LECTURES
# =========================================================

@app.route("/api/lectures/<enrollment>")
def get_lectures(enrollment):

    enrollment = enrollment.strip().upper()

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    # Find student
    cursor.execute(
        """
        SELECT enrollment, name, batch
        FROM students
        WHERE enrollment = ?
        """,
        (enrollment,)
    )

    student = cursor.fetchone()

    if student is None:

        conn.close()

        return jsonify({
            "success": False,
            "message": "Enrollment number not found.",
            "enrollment": enrollment,
            "lectures": []
        }), 404

    # Find lectures
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

    lectures = [dict(row) for row in rows]

    return jsonify({

        "success": True,

        "message": "Lectures found.",

        "student": {
            "enrollment": student["enrollment"],
            "name": student["name"],
            "batch": student["batch"]
        },

        "total_lectures": len(lectures),

        "lectures": lectures
    })


# =========================================================
# GET STUDENT
# =========================================================

@app.route("/api/student/<enrollment>")
def get_student(enrollment):

    enrollment = enrollment.strip().upper()

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT enrollment, name, batch
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
            "name": student["name"],
            "batch": student["batch"]
        }
    })


# =========================================================
# HEALTH CHECK
# =========================================================

@app.route("/api/health")
def health_check():

    return jsonify({

        "success": True,

        "message": "Student Lecture Finder API is running.",

        "status": "online",

        "server_time": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    })


# =========================================================
# START DATABASE + SERVER
# =========================================================

create_database()


if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )