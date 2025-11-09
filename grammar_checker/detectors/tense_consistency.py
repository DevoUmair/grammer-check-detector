from grammar_checker.knowledge import LinguisticKnowledge

class TenseConsistencyDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, sentence_tokens):
        errors = []
        # Simplified: real implementation would compare verb tense and context markers
        for i, word in enumerate(sentence_tokens):
            if word.lower() in self.knowledge.PAST_MARKERS:
                errors.append((i, f"Past tense marker '{word}' detected"))
        return errors
