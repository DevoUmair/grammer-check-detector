from grammar_checker.knowledge import LinguisticKnowledge

class SpellingDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, tokens, pos_tags, context):
        errors = []
        
        for i, token in enumerate(tokens):
            lower_token = token.lower()
            
            if lower_token in self.knowledge.COMMON_MISS_SPELLINGS:
                correct_spelling = self.knowledge.COMMON_MISS_SPELLINGS[lower_token]
                errors.append({
                    'position': i,
                    'message': f"Possible spelling error: '{token}'",
                    'suggestion': f"Did you mean '{correct_spelling}'?",
                    'type': 'spelling'
                })
        
        return errors