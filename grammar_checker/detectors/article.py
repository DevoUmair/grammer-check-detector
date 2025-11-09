from grammar_checker.knowledge import LinguisticKnowledge

class ArticleDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, tokens, pos_tags, context):
        errors = []
        
        for i, (token, pos) in enumerate(zip(tokens, pos_tags)):
            lower_token = token.lower()
            
            # Check for unnecessary articles before zero-article nouns
            if (lower_token in self.knowledge.ZERO_ARTICLE_NOUNS and 
                i > 0 and tokens[i-1].lower() in ['a', 'an', 'the']):
                errors.append({
                    'position': i-1,
                    'message': f"Unnecessary article '{tokens[i-1]}' before '{token}'",
                    'suggestion': f"Remove '{tokens[i-1]}' or use a different noun",
                    'type': 'article'
                })
            
            # Check for missing articles before countable nouns
            if (pos == 'NOUN' and 
                lower_token not in self.knowledge.UNCOUNTABLE_NOUNS and
                lower_token not in self.knowledge.ZERO_ARTICLE_NOUNS and
                i > 0 and tokens[i-1].lower() not in ['a', 'an', 'the', 'my', 'your', 'his', 'her', 'our', 'their']):
                # Simple heuristic for missing articles
                if i == 0 or pos_tags[i-1] not in ['DET', 'PRON']:
                    errors.append({
                        'position': i,
                        'message': f"Possible missing article before '{token}'",
                        'suggestion': f"Consider adding 'a', 'an', or 'the' before '{token}'",
                        'type': 'article'
                    })
        
        return errors