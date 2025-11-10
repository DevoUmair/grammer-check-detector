from grammar_checker.knowledge import LinguisticKnowledge

class ConfusionSetDetector:
    # Keep a small static list for quick checks; a richer map lives in knowledge.
    CONFUSION_SETS = [
        ('their', 'there', "they're"),
        ('your', "you're"),
        ('its', "it's"),
        ('affect', 'effect'),
        ('then', 'than'),
        ('accept', 'except')
    ]

    def detect(self, sentence_or_context):
        if isinstance(sentence_or_context, dict):
            tokens = sentence_or_context.get('tokens', [])
        else:
            tokens = sentence_or_context or []

        errors = []
        for i, word in enumerate(tokens):
            lw = word.lower()
            for group in self.CONFUSION_SETS:
                if lw in group:
                    # suggest the first alternative as a minimal correction
                    alternatives = [g for g in group if g != lw]
                    suggestion_word = alternatives[0] if alternatives else None
                    sugg = None
                    if suggestion_word:
                        sugg = {'type': 'replace', 'index': i, 'word': suggestion_word}
                    errors.append({
                        'pos': i,
                        'message': f"Possible confusion: '{word}'. Alternatives: {', '.join(alternatives)}",
                        'suggestion': sugg
                    })
        return errors