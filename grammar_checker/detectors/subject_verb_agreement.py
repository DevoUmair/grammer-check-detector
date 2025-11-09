from grammar_checker.knowledge import LinguisticKnowledge

class SubjectVerbAgreementDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, sentence_tokens):
        errors = []
        for i, word in enumerate(sentence_tokens):
            if word.lower() in self.knowledge.IRREGULAR_VERBS:
                pass
        return errors
