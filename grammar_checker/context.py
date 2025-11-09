import spacy

class ContextAnalyzer:
    """Analyzes sentence context for tense, subject, and other grammar signals."""

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def analyze(self, sentence: str):
        doc = self.nlp(sentence)
        subjects = [tok for tok in doc if "subj" in tok.dep_]
        verbs = [tok for tok in doc if tok.pos_ == "VERB"]
        objects = [tok for tok in doc if "obj" in tok.dep_]
        return {
            "doc": doc,
            "subjects": subjects,
            "verbs": verbs,
            "objects": objects,
            "tokens": [tok.text for tok in doc],
            "pos": [tok.pos_ for tok in doc],
            "dep": [tok.dep_ for tok in doc],
        }
