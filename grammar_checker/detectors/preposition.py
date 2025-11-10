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
        for i, word in enumerate(tokens):
            lw = word.lower()
            if lw in self.knowledge.PREPOSITION_COLLOCATIONS:
                prep_dict = self.knowledge.PREPOSITION_COLLOCATIONS[lw]
                # look ahead for a preposition token within next 3 tokens
                found_prep = None
                found_prep_index = None
                for j in range(i + 1, min(i + 4, len(tokens))):
                    candidate = tokens[j].lower()
                    if candidate in prep_dict:
                        found_prep = candidate
                        found_prep_index = j
                        break

                if found_prep:
                    # check the noun after preposition if available
                    noun_index = found_prep_index + 1
                    if noun_index < len(tokens):
                        noun = tokens[noun_index].lower()
                        allowed_nouns = prep_dict.get(found_prep)
                        if isinstance(allowed_nouns, list) and allowed_nouns and noun not in allowed_nouns:
                            # try to find an alternative preposition that fits this noun
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
                    # suggest inserting the most likely preposition (first key)
                    likely_prep = next(iter(prep_dict.keys()))
                    errors.append({
                        'pos': i,
                        'message': f"Possible missing or unexpected preposition after '{word}'",
                        'suggestion': {'type': 'insert', 'index': i+1, 'word': likely_prep}
                    })
        return errors