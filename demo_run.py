from grammar_checker.core import GrammarChecker

examples = [
    "He go to school.",
    "I went yesterday and he goes now.",
    "She put the book on the table.",
    "I visited the museum yesterday.",
    "Their going to win the match.",
    "He is the best in football."
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
