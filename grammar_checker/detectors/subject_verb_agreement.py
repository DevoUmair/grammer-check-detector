from grammar_checker.knowledge import LinguisticKnowledge

class SubjectVerbAgreementDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, tokens, pos_tags, context):
        errors = []
        doc = context['doc']
        
        # Find subject-verb pairs
        for token in doc:
            if token.pos_ == "VERB" and token.head.pos_ == "NOUN":
                subject = token.head
                verb = token
                
                # Check for basic agreement
                if (subject.text.lower() in ['he', 'she', 'it'] and 
                    verb.text.endswith(('s', 'es')) == False and
                    verb.lemma_ not in ['be', 'have']):
                    errors.append({
                        'position': token.i,
                        'message': f"Subject-verb agreement issue: '{subject.text}' and '{verb.text}'",
                        'suggestion': f"Consider using '{verb.lemma_}s' for third person singular",
                        'type': 'subject_verb_agreement'
                    })
        
        return errors