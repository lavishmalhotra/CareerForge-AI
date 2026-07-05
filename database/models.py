from database.db import get_connection


def save_resume(resume):

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

    experience

    )

    VALUES(?,?,?,?,?,?,?,?,?,?)

    """,

    (

        resume["Name"],

        resume["Email"],

        resume["Phone"],

        resume["GitHub"],

        resume["LinkedIn"],

        ",".join(resume["Skills"]),

        ",".join(resume["Education"]),

        ",".join(resume["Projects"]),

        ",".join(resume["Certifications"]),

        ",".join(resume["Experience"])

    )

    )

    conn.commit()

    conn.close()