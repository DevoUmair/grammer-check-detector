#preposition.py
from grammar_checker.knowledge import LinguisticKnowledge

class PrepositionDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, sentence_or_context):
        if isinstance(sentence_or_context, dict):
            tokens = sentence_or_context.get('tokens', [])
        else:
            tokens = sentence_or_context or []

        errors = []
        common_preps = {'in', 'on', 'at', 'to', 'for', 'of', 'with', 'about', 'by', 'from', 'into', 'onto', 'over', 'under', 'between', 'among', 'through', 'during'}

        for i, word in enumerate(tokens):
            lw = word.lower()
            verb_key = None
            if lw in self.knowledge.PREPOSITION_COLLOCATIONS:
                verb_key = lw
            else:
                if lw.endswith('ed'):
                    cand = lw[:-2]
                    cand2 = lw[:-1]
                    if cand in self.knowledge.PREPOSITION_COLLOCATIONS:
                        verb_key = cand
                    elif cand2 in self.knowledge.PREPOSITION_COLLOCATIONS:
                        verb_key = cand2
                elif lw.endswith('s'):
                    cand = lw[:-1]
                    cand2 = lw[:-2]
                    if cand in self.knowledge.PREPOSITION_COLLOCATIONS:
                        verb_key = cand
                    elif cand2 in self.knowledge.PREPOSITION_COLLOCATIONS:
                        verb_key = cand2

            if not verb_key:
                continue

            prep_dict = self.knowledge.PREPOSITION_COLLOCATIONS[verb_key]
            allowed_preps = set(prep_dict.keys())

            found_prep = None
            found_prep_index = None
            for j in range(i + 1, min(i + 4, len(tokens))):
                candidate = tokens[j].lower()
                if candidate in common_preps:
                    found_prep = candidate
                    found_prep_index = j
                    break

            if found_prep:
                if found_prep not in allowed_preps:
                    noun_index = found_prep_index + 1
                    preferred = None
                    if noun_index < len(tokens):
                        noun = tokens[noun_index].lower()
                        for p, nouns in prep_dict.items():
                            if isinstance(nouns, list):
                                for an in nouns:
                                    if noun == an or an in noun or noun in an:
                                        preferred = p
                                        break
                            if preferred:
                                break

                        if preferred:
                            likely_prep = preferred
                        else:
                            if 'at' in allowed_preps:
                                likely_prep = 'at'
                            else:
                                likely_prep = next(iter(allowed_preps)) if allowed_preps else None
                    sugg = None
                    if likely_prep:
                        sugg = {'type': 'replace', 'index': found_prep_index, 'word': likely_prep}
                    errors.append({
                        'pos': found_prep_index,
                        'message': f"Unexpected preposition '{tokens[found_prep_index]}' after '{word}'; expected: {', '.join(allowed_preps)}",
                        'suggestion': sugg
                    })
                else:
                    noun_index = found_prep_index + 1
                    if noun_index < len(tokens):
                        noun = tokens[noun_index].lower()
                        allowed_nouns = prep_dict.get(found_prep)
                        if isinstance(allowed_nouns, list) and allowed_nouns and noun not in allowed_nouns:
                            replacement_prep = None
                            for p, nouns in prep_dict.items():
                                if isinstance(nouns, list) and noun in nouns:
                                    replacement_prep = p
                                    break
                            sugg = None
                            if replacement_prep:
                                sugg = {'type': 'replace', 'index': found_prep_index, 'word': replacement_prep}
                            errors.append({
                                'pos': noun_index,
                                'message': f"Unusual collocation: '{lw} {found_prep} {tokens[noun_index]}'",
                                'suggestion': sugg
                            })
            else:
                likely_prep = next(iter(prep_dict.keys()))
                errors.append({
                    'pos': i,
                    'message': f"Possible missing preposition after '{word}'",
                    'suggestion': {'type': 'insert', 'index': i+1, 'word': likely_prep}
                })
        return errors
