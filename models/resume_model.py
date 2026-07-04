from dataclasses import dataclass
from typing import List


@dataclass
class Resume:

    name: str

    email: str

    phone: str

    github: str

    linkedin: str

    skills: List[str]

    education: List[str]

    projects: List[str]

    certifications: List[str]