from grammar_checker.core import GrammarChecker

tests = [
    "She adopted an dog from the shelter.",
    "He visited a Eiffel Tower last summer.",
    "She is good in mathematics.",
    "He arrived to the office early.",
    "He was walking to school when he sees a dog.",
    "She studies all night and submitted the assignment this morning.",
    "The list of items are on the table.",
    "Each of the students have a laptop.",
    "Their going to win the match."
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
