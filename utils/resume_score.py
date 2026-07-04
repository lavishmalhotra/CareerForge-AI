import re

ACTION_VERBS = [
    "developed", "built", "created", "designed", "implemented",
    "optimized", "managed", "improved", "led", "deployed",
    "integrated", "automated", "engineered", "analyzed"
]


def calculate_ats_score(info, resume_text):

    score = 0

    strengths = []

    weaknesses = []

    suggestions = []

    # ---------------- Personal Information ----------------

    if info["Name"] != "Not Found":
        score += 5
    else:
        weaknesses.append("Name Missing")

    if info["Email"] != "Not Found":
        score += 5
    else:
        weaknesses.append("Email Missing")

    if info["Phone"] != "Not Found":
        score += 5
    else:
        weaknesses.append("Phone Number Missing")

    if info["GitHub"] != "Not Found":
        score += 5
        strengths.append("GitHub Profile Added")
    else:
        suggestions.append("Add your GitHub profile.")

    if info["LinkedIn"] != "Not Found":
        score += 5
        strengths.append("LinkedIn Profile Added")
    else:
        suggestions.append("Add your LinkedIn profile.")

    # ---------------- Skills ----------------

    skill_count = len(info["Skills"])

    if skill_count >= 10:
        score += 20
        strengths.append("Strong Technical Skillset")

    elif skill_count >= 6:
        score += 15

    elif skill_count >= 3:
        score += 10
        suggestions.append("Add more technical skills.")

    else:
        weaknesses.append("Very Few Skills")
        suggestions.append("Include relevant technical skills.")

    # ---------------- Education ----------------

    if len(info["Education"]) > 0:
        score += 10
    else:
        weaknesses.append("Education Missing")

    # ---------------- Projects ----------------

    if len(info["Projects"]) >= 2:
        score += 15
        strengths.append("Good Project Section")

    elif len(info["Projects"]) == 1:
        score += 8
        suggestions.append("Add one more strong project.")

    else:
        weaknesses.append("Projects Missing")

    # ---------------- Certifications ----------------

    if len(info["Certifications"]) > 0:
        score += 5

    else:
        suggestions.append("Add relevant certifications.")

    # ---------------- Action Verbs ----------------

    verb_count = 0

    lower_text = resume_text.lower()

    for verb in ACTION_VERBS:
        verb_count += lower_text.count(verb)

    if verb_count >= 5:
        score += 10
        strengths.append("Strong Action Verbs Used")

    elif verb_count >= 2:
        score += 5

    else:
        suggestions.append(
            "Use action verbs like Developed, Built, Designed, Implemented."
        )

    # ---------------- Quantified Achievements ----------------

    numbers = re.findall(r"\d+%|\d+\+", resume_text)

    if len(numbers) >= 3:
        score += 10
        strengths.append("Quantified Achievements Present")

    elif len(numbers) >= 1:
        score += 5

    else:
        suggestions.append(
            "Add measurable achievements (Example: Improved accuracy by 15%)."
        )

    if score > 100:
        score = 100

    return score, strengths, weaknesses, suggestions