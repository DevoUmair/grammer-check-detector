from grammar_checker.knowledge import LinguisticKnowledge

class PrepositionDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, tokens, pos_tags, context):
        errors = []
        
        for i, (token, pos) in enumerate(zip(tokens, pos_tags)):
            lower_token = token.lower()
            
            # Check verb-preposition collocations
            if lower_token in self.knowledge.PREPOSITION_COLLOCATIONS:
                expected_preps = self.knowledge.PREPOSITION_COLLOCATIONS[lower_token]
                
                if i + 1 < len(tokens):
                    next_token = tokens[i + 1].lower()
                    if (next_token not in expected_preps and 
                        pos_tags[i + 1] in ['ADP', 'PART']):  # ADP is preposition, PART is particle
                        errors.append({
                            'position': i,
                            'message': f"Check preposition usage after '{token}'",
                            'suggestion': f"Common prepositions for '{token}': {list(expected_preps.keys())}",
                            'type': 'preposition'
                        })
        
        return errors