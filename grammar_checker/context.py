import spacy
from grammar_checker.knowledge import LinguisticKnowledge

class ContextAnalyzer:
    """Context analyzer using spaCy and lemminflect."""
    
    def __init__(self):
        self.nlp = None
        self.knowledge = LinguisticKnowledge()
        
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except Exception as e:
            print(f"Warning: spaCy model not available: {e}")

    def analyze(self, sentence: str):
        """Analyze sentence context."""
        if self.nlp is None:
            return self._fallback_analysis(sentence)

        doc = self.nlp(sentence)
        
        return {
            "doc": doc,
            "tokens": [token.text for token in doc],
            "lemmas": [token.lemma_ for token in doc],
            "pos": [token.pos_ for token in doc],
            "dep": [token.dep_ for token in doc],
            "morph": [str(token.morph) for token in doc],
            "subjects": [token for token in doc if "subj" in token.dep_],
            "verbs": [token for token in doc if token.pos_ == "VERB"],
            "objects": [token for token in doc if "obj" in token.dep_],
            "proper_nouns": [token for token in doc if token.pos_ == "PROPN"],
            "noun_phrases": [chunk.text for chunk in doc.noun_chunks]
        }

    def _fallback_analysis(self, sentence):
        """Fallback when spaCy is unavailable."""
        tokens = sentence.split()
        return {
            "doc": None,
            "tokens": tokens,
            "lemmas": tokens,
            "pos": [],
            "dep": [],
            "morph": [],
            "subjects": [],
            "verbs": [],
            "objects": [],
            "proper_nouns": [token for token in tokens if token and token[0].isupper()],
            "noun_phrases": []
        }

    def get_verb_inflection(self, base_verb, form='VBD'):
        """Get verb inflection using lemminflect."""
        try:
            import lemminflect
            inflections = lemminflect.getInflection(base_verb, form)
            return inflections[0] if inflections else None
        except Exception as e:
            print(f"Lemminflect error for '{base_verb}': {e}")
            return None