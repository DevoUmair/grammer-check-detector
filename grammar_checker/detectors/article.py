#article.py
from grammar_checker.knowledge import LinguisticKnowledge


class ArticleDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, sentence_or_context):
        """Detect unnecessary articles and suggest removal.

        Accepts either a tokens list or a context dict with 'tokens'. Returns
        a list of structured error dicts.
        """
        if isinstance(sentence_or_context, dict):
            tokens = sentence_or_context.get('tokens', [])
        else:
            tokens = sentence_or_context or []

        errors = []
        vowels = set('aeiou')
        for i, word in enumerate(tokens):
            lw = word.lower()
            # Unnecessary zero-article case (existing behavior)
            if lw in self.knowledge.ZERO_ARTICLE_NOUNS and i > 0:
                prev_word = tokens[i - 1].lower()
                if prev_word in ['a', 'an', 'the']:
                    # be conservative: if there's a preposition before the article,
                    # keep the article (e.g., 'arrived at the office').
                    if i - 2 >= 0:
                        prev_prev = tokens[i - 2].lower()
                        if prev_prev in getattr(self.knowledge, 'PREPOSITIONS', set()):
                            continue
                    errors.append({
                        'pos': i - 1,
                        'message': f"Unnecessary article '{prev_word}' before '{word}'",
                        'suggestion': {'type': 'remove', 'index': i - 1}
                    })

            # Incorrect indefinite article usage: prefer checking proper nouns first
            if lw in ('a', 'an') and i + 1 < len(tokens):
                next_tok = tokens[i + 1]
                # proper-name/specific landmark heuristic: 'a Eiffel' -> 'the Eiffel'
                if next_tok and next_tok[0].isupper():
                    errors.append({
                        'pos': i,
                        'message': f"Article '{tokens[i]}' before proper noun '{next_tok}' may be wrong",
                        'suggestion': {'type': 'replace', 'index': i, 'word': 'the'}
                    })
                    continue

                # strip punctuation
                next_clean = next_tok.strip('.,!?').lower()
                if not next_clean:
                    continue
                first = next_clean[0]
                # prefer 'an' before vowel sounds (approx via vowel letter)
                if lw == 'an' and first not in vowels:
                    errors.append({
                        'pos': i,
                        'message': f"Incorrect article '{tokens[i]}' before '{next_tok}'",
                        'suggestion': {'type': 'replace', 'index': i, 'word': 'a'}
                    })
                elif lw == 'a' and first in vowels:
                    errors.append({
                        'pos': i,
                        'message': f"Incorrect article '{tokens[i]}' before '{next_tok}'",
                        'suggestion': {'type': 'replace', 'index': i, 'word': 'an'}
                    })
        return errors
