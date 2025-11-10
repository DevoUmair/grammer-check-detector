"""
Test dataset for grammar checker accuracy evaluation
Each test case contains:
- input_sentence: The sentence with potential errors
- expected_errors: List of expected error positions and types
- expected_corrections: Expected correction suggestions
"""

GRAMMAR_TEST_CASES = [
    # ==================== ARTICLE ERROR TESTS ====================
    {
        "input_sentence": "I go to the school every day.",
        "expected_errors": [
            {"pos": 3, "type": "article", "message": "Unnecessary article"}
        ],
        "expected_corrections": ["I go to school every day."]
    },
    {
        "input_sentence": "She is in the hospital for checkup.",
        "expected_errors": [
            {"pos": 3, "type": "article", "message": "Unnecessary article"}
        ],
        "expected_corrections": ["She is in hospital for checkup."]
    },
    {
        "input_sentence": "Student went to university.",
        "expected_errors": [
            {"pos": 0, "type": "article", "message": "missing article"}
        ],
        "expected_corrections": ["A student went to university."]
    },
    
    # ==================== CONFUSION WORD TESTS ====================
    {
        "input_sentence": "Their going to the park.",
        "expected_errors": [
            {"pos": 0, "type": "confusion", "message": "Possible confusion"}
        ],
        "expected_corrections": ["They're going to the park."]
    },
    {
        "input_sentence": "Your welcome to join us.",
        "expected_errors": [
            {"pos": 0, "type": "confusion", "message": "Possible confusion"}
        ],
        "expected_corrections": ["You're welcome to join us."]
    },
    {
        "input_sentence": "The dog wagged it's tail.",
        "expected_errors": [
            {"pos": 3, "type": "confusion", "message": "Possible confusion"}
        ],
        "expected_corrections": ["The dog wagged its tail."]
    },
    
    # ==================== SPELLING ERROR TESTS ====================
    {
        "input_sentence": "I recieved your message.",
        "expected_errors": [
            {"pos": 1, "type": "spelling", "message": "Possible spelling"}
        ],
        "expected_corrections": ["I received your message."]
    },
    {
        "input_sentence": "This is definately correct.",
        "expected_errors": [
            {"pos": 2, "type": "spelling", "message": "Possible spelling"}
        ],
        "expected_corrections": ["This is definitely correct."]
    },
    
    # ==================== TENSE ERROR TESTS ====================
    {
        "input_sentence": "I go to school yesterday.",
        "expected_errors": [
            {"pos": 1, "type": "tense", "message": "Tense inconsistency"}
        ],
        "expected_corrections": ["I went to school yesterday."]
    },
    {
        "input_sentence": "Tomorrow I visited my friend.",
        "expected_errors": [
            {"pos": 2, "type": "tense", "message": "Tense inconsistency"}
        ],
        "expected_corrections": ["Tomorrow I will visit my friend."]
    },
    
    # ==================== SUBJECT-VERB AGREEMENT TESTS ====================
    {
        "input_sentence": "She have a beautiful voice.",
        "expected_errors": [
            {"pos": 1, "type": "agreement", "message": "agreement error"}
        ],
        "expected_corrections": ["She has a beautiful voice."]
    },
    {
        "input_sentence": "He go to school every day.",
        "expected_errors": [
            {"pos": 1, "type": "agreement", "message": "agreement error"}
        ],
        "expected_corrections": ["He goes to school every day."]
    },
    
    # ==================== PREPOSITION ERROR TESTS ====================
    {
        "input_sentence": "She arrived to the city.",
        "expected_errors": [
            {"pos": 1, "type": "preposition", "message": "preposition"}
        ],
        "expected_corrections": ["She arrived in the city."]
    },
    
    # ==================== MULTIPLE ERROR TESTS ====================
    {
        "input_sentence": "Their going to the school yesterday.",
        "expected_errors": [
            {"pos": 0, "type": "confusion", "message": "Possible confusion"},
            {"pos": 3, "type": "article", "message": "Unnecessary article"},
            {"pos": 4, "type": "tense", "message": "Tense inconsistency"}
        ],
        "expected_corrections": ["They're going to school yesterday."]
    },
    
    # ==================== CORRECT SENTENCE TESTS ====================
    {
        "input_sentence": "I go to school every day.",
        "expected_errors": [],
        "expected_corrections": ["I go to school every day."]
    },
    {
        "input_sentence": "She has a beautiful voice.",
        "expected_errors": [],
        "expected_corrections": ["She has a beautiful voice."]
    },
    {
        "input_sentence": "They received the message yesterday.",
        "expected_errors": [],
        "expected_corrections": ["They received the message yesterday."]
    }
]

# Performance test cases
PERFORMANCE_TEST_CASES = [
    "This is a simple correct sentence.",
    "The students are studying mathematics at university.",
    "She goes to work every day and enjoys her job.",
    "They will arrive at the station tomorrow morning.",
    "He looks at the picture carefully and understands its meaning."
]