Advanced Grammar Checker
Project Overview

An advanced NLP-based grammar checker that detects various types of grammatical errors in English sentences using spaCy and custom rule-based detectors.
Features

    ✅ Article Usage Detection - Checks for missing/unnecessary articles

    ✅ Confusion Word Detection - Identifies commonly confused words (their/there/they're, your/you're, etc.)

    ✅ Preposition Collocation - Verifies correct preposition usage with verbs

    ✅ Subject-Verb Agreement - Ensures proper agreement between subjects and verbs

    ✅ Tense Consistency - Detects inconsistent verb tenses within sentences

    ✅ Spelling Check - Identifies common spelling mistakes

    ✅ Context-Aware Analysis - Uses spaCy for linguistic analysis

    ✅ Confidence Scoring - Provides confidence levels for detections

    ✅ Detailed Suggestions - Offers specific correction recommendations

Files:

    main.py - Launches the interactive grammar checker

    grammar_checker/core.py - Main grammar checker class and error detection orchestration

    grammar_checker/context.py - Context analyzer using spaCy for linguistic analysis

    grammar_checker/knowledge.py - Linguistic knowledge base with grammar rules and patterns

    grammar_checker/detectors/ - Directory containing specialized error detectors

        article.py - Article usage detection

        confusion_set.py - Confusion word detection

        preposition.py - Preposition collocation checking

        subject_verb_agreement.py - Subject-verb agreement verification

        tense_consistency.py - Tense consistency analysis

        spelling.py - Common spelling mistake detection

    grammar_checker/utils/text_processor.py - Text processing utilities

    requirements.txt - Python dependencies

    tests/ - Unit tests for the grammar checker
Setup:

    Requires Python 3.7 or higher

    spaCy and English language model required

Installation Steps:

    Create and activate virtual environment:
    bash

python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

Install dependencies:
bash

pip install spacy
python -m spacy download en_core_web_sm

Run:

    Activate virtual environment:
    bash

# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

Run the grammar checker:
bash

python main.py

Usage Examples:
text

Enter sentence: Their going to the school yesterday

Analyzing: 'Their going to the school yesterday'
----------------------------------------
❌ Potential errors detected:
   • Position 0: Possible confusion word: 'Their'
     Suggestion: Did you mean: there, they're?

   • Position 3: Unnecessary article 'the' before 'school'
     Suggestion: Remove 'the' or use a different noun

   • Position 4: Time word 'yesterday' may not match verb tense
     Suggestion: Adjust verb tense to match time reference 'yesterday'

Confidence Score: 40.0%
----------------------------------------

Error Types Detected:

    Article Errors: Unnecessary articles before zero-article nouns (school, hospital, home)

    Confusion Words: their/there/they're, your/you're, its/it's, affect/effect, then/than

    Preposition Errors: Incorrect verb-preposition combinations

    Subject-Verb Agreement: Third-person singular mismatches

    Tense Consistency: Mixed tenses and time marker mismatches

    Spelling Mistakes: Common misspellings (recieve/receive, definately/definitely)

Test Examples:
python

# Article errors
"I go to the school every day."
"Student went to university."

# Confusion words  
"Their going to the park."
"Your welcome to join us."

# Spelling errors
"I recieved your message."
"This is definately correct."

# Tense errors
"I go to school yesterday."
"Tomorrow I visited my friend."

Notes:

    The grammar checker uses rule-based detection combined with spaCy's linguistic analysis

    Confidence scores help indicate the reliability of detections

    Suggestions provide specific correction recommendations

    All detectors work together to provide comprehensive grammar checking

Testing:
bash

# Run unit tests
python -m pytest tests/
python -m unittest tests/test_core.py

Future Enhancements:

    Add more grammar rules and patterns

    Improve context-aware detection

    Add support for paragraph-level analysis

    Include style and readability suggestions

    Add progress indicators for long texts

    Support for saving analysis results

