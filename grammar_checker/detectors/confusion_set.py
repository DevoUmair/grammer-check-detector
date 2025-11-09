from grammar_checker.knowledge import LinguisticKnowledge

class ConfusionSetDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()
        self.confusion_sets = {
            'their': ["there", "they're"],
            'there': ["their", "they're"],
            "they're": ["their", "there"],
            'your': ["you're"],
            "you're": ["your"],
            'its': ["it's"],
            "it's": ["its"],
            'affect': ["effect"],
            'effect': ["affect"],
            'then': ["than"],
            'than': ["then"],
        }

    def detect(self, tokens, pos_tags, context):
        errors = []
        
        for i, token in enumerate(tokens):
            lower_token = token.lower()
            
            if lower_token in self.confusion_sets:
                alternatives = self.confusion_sets[lower_token]
                errors.append({
                    'position': i,
                    'message': f"Possible confusion word: '{token}'",
                    'suggestion': f"Did you mean: {', '.join(alternatives)}?",
                    'type': 'confusion_set'
                })
        
        return errors