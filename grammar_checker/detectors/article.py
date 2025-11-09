from grammar_checker.knowledge import LinguisticKnowledge

class ArticleDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, sentence_tokens):
        errors = []
        for i, word in enumerate(sentence_tokens):
            lw = word.lower()
            if lw in self.knowledge.ZERO_ARTICLE_NOUNS and i > 0:
                prev_word = sentence_tokens[i-1].lower()
                if prev_word in ['a', 'an', 'the']:
                    errors.append((i-1, f"Unnecessary article '{prev_word}' before '{word}'"))
        return errors
