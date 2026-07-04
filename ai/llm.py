import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"


def review_resume(resume_text, ats_score):

    prompt = f"""
You are an expert ATS recruiter.

Resume:

{resume_text}

ATS Score:

{ats_score}

Give:

1. Strengths
2. Weaknesses
3. Suggestions
4. Final Verdict

Keep the response concise and professional.
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "openai/gpt-4.1-mini",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(URL, headers=headers, json=payload, timeout=60)

    data = response.json()

    return data["choices"][0]["message"]["content"]