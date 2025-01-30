from setuptools import setup, find_packages
from typing import List
from pathlib import Path

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:Path) -> List[str]:
    """
        this function will return list of requriements from requirements.txt file
    """
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name= "Mlproject",
    version="0.0.1",
    author= "Muhammad Hashir",
    author_email= "hashirgohar@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")
)


