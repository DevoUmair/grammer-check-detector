from grammar_checker.knowledge import LinguisticKnowledge


class ArticleDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, sentence_or_context):
        """Detect unnecessary articles and suggest removal.

        Accepts either a tokens list or a context dict with 'tokens'. Returns
        a list of structured error dicts.
        """
        if isinstance(sentence_or_context, dict):
            tokens = sentence_or_context.get('tokens', [])
        else:
            tokens = sentence_or_context or []

        errors = []
        for i, word in enumerate(tokens):
            lw = word.lower()
            if lw in self.knowledge.ZERO_ARTICLE_NOUNS and i > 0:
                prev_word = tokens[i - 1].lower()
                if prev_word in ['a', 'an', 'the']:
                    errors.append({
                        'pos': i - 1,
                        'message': f"Unnecessary article '{prev_word}' before '{word}'",
                        'suggestion': {'type': 'remove', 'index': i - 1}
                    })
        return errors