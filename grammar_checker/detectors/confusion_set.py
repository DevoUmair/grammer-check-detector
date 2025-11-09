class ConfusionSetDetector:
    CONFUSION_SETS = [
        ('their', 'there', 'they\'re'),
        ('your', 'you\'re'),
        ('its', 'it\'s'),
        ('affect', 'effect'),
        ('then', 'than'),
        ('accept', 'except')
    ]

    def detect(self, sentence_tokens):
        errors = []
        for i, word in enumerate(sentence_tokens):
            for group in self.CONFUSION_SETS:
                if word.lower() in group:
                    errors.append((i, f"Check confusion set: '{word}'"))
        return errors
