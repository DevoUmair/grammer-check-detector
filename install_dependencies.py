"""
Installation script for grammar checker dependencies
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required packages and download necessary models"""
    
    print("Installing Python packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    print("Downloading spaCy model...")
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    
    print("Downloading NLTK data...")
    import nltk
    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')
    
    print("All dependencies installed successfully!")

if __name__ == "__main__":
    install_dependencies()