from setuptools import setup, find_packages

setup(
    name="grammar_checker",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "spacy>=3.0.0",
    ],
    python_requires=">=3.7",
    author="Your Name",
    author_email="your.email@example.com",
    description="An advanced context-aware grammar checker for English",
    keywords="nlp grammar checker spelling syntax",
)