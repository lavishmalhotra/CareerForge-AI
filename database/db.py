import sqlite3
from datetime import datetime

DB_NAME = "careerforge.db"


# ==========================================================
# Connection
# ==========================================================

def get_connection():
    return sqlite3.connect(DB_NAME)


# ==========================================================
# Create Tables
# ==========================================================

def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    # ------------------------------------------------------
    # Resume Table
    # ------------------------------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,
        email TEXT,
        phone TEXT,

        github TEXT,
        linkedin TEXT,

        skills TEXT,
        education TEXT,
        projects TEXT,
        certifications TEXT,
        experience TEXT,

        created_at TEXT
    )
    """)

    # ------------------------------------------------------
    # History Table
    # ------------------------------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        report_type TEXT,

        title TEXT,

        content TEXT,

        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


# ==========================================================
# Save Resume
# ==========================================================

def save_resume(info):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO resumes(

        name,
        email,
        phone,

        github,
        linkedin,

        skills,
        education,
        projects,
        certifications,
        experience,

        created_at

    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?)

    """,

    (

        info["Name"],
        info["Email"],
        info["Phone"],

        info["GitHub"],
        info["LinkedIn"],

        ", ".join(info["Skills"]),
        "\n".join(info["Education"]),
        "\n".join(info["Projects"]),
        "\n".join(info["Certifications"]),
        "\n".join(info["Experience"]),

        datetime.now().strftime("%d-%m-%Y %H:%M")

    )

    )

    conn.commit()
    conn.close()


# ==========================================================
# Save AI Report
# ==========================================================

def save_history(
    report_type,
    title,
    content
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO history(

        report_type,
        title,
        content,
        created_at

    )

    VALUES(?,?,?,?)

    """,

    (

        report_type,
        title,
        content,
        datetime.now().strftime("%d-%m-%Y %H:%M")

    )

    )

    conn.commit()
    conn.close()


# ==========================================================
# Get History
# ==========================================================

def get_history():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT
        report_type,
        title,
        created_at

    FROM history

    ORDER BY id DESC

    """)

    data = cursor.fetchall()

    conn.close()

    return data


# ==========================================================
# Get Full Report
# ==========================================================

def get_report(report_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM history

    WHERE id=?

    """,

    (report_id,)

    )

    data = cursor.fetchone()

    conn.close()

    return data