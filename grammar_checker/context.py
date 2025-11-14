try:
    import spacy
except Exception:
    spacy = None


class ContextAnalyzer:
    """Analyzes sentence context for tense, subject, and other grammar signals.

    If spaCy isn't available, fall back to a simple whitespace tokenizer so the
    detectors can still run in minimal environments.
    """

    def __init__(self):
        self.nlp = None
        if spacy is not None:
            try:
                self.nlp = spacy.load("en_core_web_sm")
            except Exception:
                self.nlp = None

    def analyze(self, sentence: str):
        if self.nlp is None:
            tokens = sentence.split()
            return {
                "doc": None,
                "subjects": [],
                "verbs": [],
                "objects": [],
                "tokens": tokens,
                "pos": [],
                "dep": [],
            }

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
