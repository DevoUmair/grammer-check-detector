import spacy

class ContextAnalyzer:
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            raise Exception(
                "SpaCy English model not found. Please install it using: "
                "python -m spacy download en_core_web_sm"
            )

    def analyze(self, sentence: str):
        doc = self.nlp(sentence)
        
        subjects = [tok for tok in doc if "subj" in tok.dep_.lower()]
        verbs = [tok for tok in doc if tok.pos_ == "VERB"]
        objects = [tok for tok in doc if "obj" in tok.dep_.lower()]
        
        # Extract tense information
        tense_info = self._extract_tense_info(doc)
        
        return {
            "doc": doc,
            "tokens": [tok.text for tok in doc],
            "pos": [tok.pos_ for tok in doc],
            "lemmas": [tok.lemma_ for tok in doc],
            "dep": [tok.dep_ for tok in doc],
            "subjects": subjects,
            "verbs": verbs,
            "objects": objects,
            "tense_info": tense_info,
            "sentence_text": sentence
        }
    
    def _extract_tense_info(self, doc):
        tense_markers = []
        for token in doc:
            if token.tag_ in ['VBD', 'VBN']:  # Past tense
                tense_markers.append(('past', token.text))
            elif token.tag_ in ['VBZ', 'VBP']:  # Present tense
                tense_markers.append(('present', token.text))
            elif token.tag_ == 'VBG':  # Gerund/Continuous
                tense_markers.append(('continuous', token.text))
                
        return tense_markers