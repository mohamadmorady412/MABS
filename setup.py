from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MABS-milan",
    version="0.1.0",
    author="Mohammadjavad Morady",
    packages=find_packages(),
)