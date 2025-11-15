from grammar_checker.core import GrammarChecker

examples = [
    "He walk to the market every day.",               # subject-verb agreement error
    "I finished my work and he finish his later.",    # tense consistency error
    "She place her keys on the desk.",                # incorrect verb form (simple grammar issue)
    "We explored the old castle last weekend.",       # correct sentence (no error)
    "There going to lose if they don’t practice.",    # confusion-set error (There → They’re)
    "She is excellent in physics."                    # preposition error (in → at)
]


checker = GrammarChecker()
for s in examples:
    print('\nSentence:', s)
    result = checker.check(s)
    errors = result.get('errors', [])
    corrected = result.get('corrected_sentence')
    if errors:
        for e in errors:
            print(f" - {e.get('message')} (pos {e.get('pos')}) | suggestion: {e.get('suggestion')}")
        print(' Suggested sentence:', corrected)
    else:
        print(' - No errors detected')
