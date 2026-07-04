import re

COMMON_SKILLS = [
    "Python", "Java", "C", "C++", "JavaScript", "TypeScript",
    "HTML", "CSS", "SQL", "React", "Node.js", "FastAPI",
    "Flask", "Django", "Machine Learning", "Deep Learning",
    "TensorFlow", "PyTorch", "OpenCV", "Pandas", "NumPy",
    "Scikit-learn", "Git", "GitHub", "Docker",
    "AWS", "Azure", "MongoDB", "MySQL", "PostgreSQL",
    "Linux", "Kubernetes"
]


def find_name(lines):
    for line in lines:
        line = line.strip()

        if (
            len(line.split()) >= 2
            and len(line) < 40
            and "@" not in line
            and "github" not in line.lower()
            and "linkedin" not in line.lower()
        ):
            return line

    return "Not Found"


def extract_section(lines, keywords):
    data = []

    for line in lines:
        lower = line.lower()

        for keyword in keywords:
            if keyword.lower() in lower:
                data.append(line.strip())
                break

    return list(dict.fromkeys(data))


def extract_skills(text):

    found = []

    lower = text.lower()

    for skill in COMMON_SKILLS:

        if skill.lower() in lower:
            found.append(skill)

    return sorted(list(set(found)))


def parse_resume(text):

    lines = text.splitlines()

    data = {}

    data["Name"] = find_name(lines)

    email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    data["Email"] = email.group() if email else "Not Found"

    phone = re.search(r'(\+91[\s-]?)?[6-9]\d{9}', text)
    data["Phone"] = phone.group() if phone else "Not Found"

    github = re.search(
        r'github\.com/[A-Za-z0-9_-]+',
        text,
        re.IGNORECASE
    )

    data["GitHub"] = github.group() if github else "Not Found"

    linkedin = re.search(
        r'linkedin\.com/in/[A-Za-z0-9_-]+',
        text,
        re.IGNORECASE
    )

    data["LinkedIn"] = linkedin.group() if linkedin else "Not Found"

    data["Skills"] = extract_skills(text)

    data["Education"] = extract_section(
        lines,
        [
            "University",
            "College",
            "Institute",
            "School",
            "Bachelor",
            "B.Tech",
            "M.Tech",
            "BCA",
            "MCA",
            "Diploma"
        ]
    )

    data["Projects"] = extract_section(
        lines,
        [
            "Project",
            "Developed",
            "Built",
            "Created",
            "Implemented"
        ]
    )

    data["Certifications"] = extract_section(
        lines,
        [
            "Certification",
            "Certificate",
            "Coursera",
            "Udemy",
            "NPTEL",
            "Microsoft",
            "Oracle",
            "AWS"
        ]
    )

    data["Experience"] = extract_section(
        lines,
        [
            "Intern",
            "Internship",
            "Experience",
            "Worked",
            "Software Engineer"
        ]
    )

    return data