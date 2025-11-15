from grammar_checker.core import GrammarChecker

tests = [
    "He walk to the market every day.",               # subject-verb agreement error
    "I finished my work and he finish his later.",    # tense consistency error
    "She place her keys on the desk.",                # incorrect verb form (simple grammar issue)
    "We explored the old castle last weekend.",       # correct sentence (no error)
    "There going to lose if they don’t practice.",    # confusion-set error (There → They’re)
    "She is excellent in physics."                    # preposition error (in → at)
]


checker = GrammarChecker()

for s in tests:
    print('\nInput:', s)
    res = checker.check(s)
    print('Corrected:', res.get('corrected_sentence'))
    errs = res.get('errors', [])
    if errs:
        print('Errors:')
        for e in errs:
            print(f" - {e.get('message')} (pos {e.get('pos')}) suggestion={e.get('suggestion')}")
    else:
        print(' - No errors detected')
