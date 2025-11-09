from grammar_checker.knowledge import LinguisticKnowledge

class TenseConsistencyDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, tokens, pos_tags, context):
        errors = []
        tense_markers = context['tense_info']
        
        if len(tense_markers) > 1:
            # Check for mixed tenses
            tenses = set(marker[0] for marker in tense_markers)
            if len(tenses) > 1:
                errors.append({
                    'position': 0,
                    'message': "Possible tense inconsistency detected",
                    'suggestion': "Ensure all verbs use the same tense throughout the sentence",
                    'type': 'tense_consistency'
                })
        
        # Check for time marker and tense mismatch
        time_words = set()
        for i, token in enumerate(tokens):
            lower_token = token.lower()
            if lower_token in self.knowledge.PAST_MARKERS:
                time_words.add(('past', i))
            elif lower_token in self.knowledge.FUTURE_MARKERS:
                time_words.add(('future', i))
        
        # Simple check for obvious mismatches
        for time_type, pos in time_words:
            for tense_type, _ in tense_markers:
                if (time_type == 'past' and tense_type == 'present') or \
                   (time_type == 'future' and tense_type == 'past'):
                    errors.append({
                        'position': pos,
                        'message': f"Time word '{tokens[pos]}' may not match verb tense",
                        'suggestion': f"Adjust verb tense to match time reference '{tokens[pos]}'",
                        'type': 'tense_consistency'
                    })
        
        return errors