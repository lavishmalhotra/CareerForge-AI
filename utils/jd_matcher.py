def extract_skills(job_description, skill_database):
    found_skills = []

    job_description = job_description.lower()

    for skill in skill_database:
        if skill.lower() in job_description:
            found_skills.append(skill)

    return found_skills


def match_resume_with_jd(resume_skills, jd_skills):

    resume_set = set(skill.lower() for skill in resume_skills)
    jd_set = set(skill.lower() for skill in jd_skills)

    matched = sorted(list(resume_set.intersection(jd_set)))
    missing = sorted(list(jd_set - resume_set))

    if len(jd_set) == 0:
        percentage = 0
    else:
        percentage = round((len(matched) / len(jd_set)) * 100)

    recommendations = [
        f"Learn {skill.title()} and build a project using it."
        for skill in missing
    ]

    return {
        "percentage": percentage,
        "matched": matched,
        "missing": missing,
        "recommendations": recommendations
    }