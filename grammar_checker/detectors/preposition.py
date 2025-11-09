from grammar_checker.knowledge import LinguisticKnowledge

class PrepositionDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, sentence_tokens):
        errors = []
        for i, word in enumerate(sentence_tokens):
            lw = word.lower()
            for verb, prep_dict in self.knowledge.PREPOSITION_COLLOCATIONS.items():
                if lw == verb and i+1 < len(sentence_tokens):
                    next_word = sentence_tokens[i+1].lower()
                    if next_word not in prep_dict:
                        errors.append((i, f"Check preposition usage for '{verb}'"))
        return errors
