from grammar_checker.knowledge import LinguisticKnowledge

class TenseConsistencyDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, sentence_or_context):
        if isinstance(sentence_or_context, dict):
            tokens = sentence_or_context.get('tokens', [])
        else:
            tokens = sentence_or_context or []

        errors = []
        past_markers = self.knowledge.PAST_MARKERS
        for i, word in enumerate(tokens):
            lw = word.lower()
            if lw in past_markers:
                # look for a verb within next 6 tokens and check for present-tense hint
                for j in range(i + 1, min(i + 7, len(tokens))):
                    tj = tokens[j].lower()
                    if tj.endswith('s') and not tj.endswith('ss'):
                        # if we know an irregular past, suggest it
                        base = tj.rstrip('s')
                        suggested = None
                        if base in self.knowledge.IRREGULAR_VERBS:
                            suggested = self.knowledge.IRREGULAR_VERBS[base].get('past')
                        else:
                            # naive regular past
                            if tj.endswith('es'):
                                suggested = tj[:-2] + 'ed'
                            else:
                                suggested = tj[:-1] + 'ed'

                        sugg_obj = None
                        if suggested:
                            sugg_obj = {'type': 'replace', 'index': j, 'word': suggested}

                        errors.append({
                            'pos': j,
                            'message': f"Tense inconsistency: past marker '{word}' but verb '{tokens[j]}' looks present-tense",
                            'suggestion': sugg_obj
                        })
                        break
        return errors
