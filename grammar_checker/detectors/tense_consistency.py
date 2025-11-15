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

        present_like = []
        past_like = []
        be_past = set(self.knowledge.AUXILIARY_VERBS.get('be', {}).get('past', []))
        have_past = set(self.knowledge.AUXILIARY_VERBS.get('have', {}).get('past', []))
        
        irregular_pasts = set()
        for base, info in self.knowledge.IRREGULAR_VERBS.items():
            past = info.get('past')
            if isinstance(past, str):
                irregular_pasts.add(past)

        for idx, tok in enumerate(tokens):
            t = tok.lower()
            
            if t in be_past or t in have_past or t in irregular_pasts:
                past_like.append(idx)
                continue
            if t.endswith('s') and not t.endswith('ss'):
                present_like.append(idx)
            if t.endswith('ed'):
                past_like.append(idx)


        if present_like and past_like:
            for p_idx in present_like:
                tok = tokens[p_idx].lower()
                if tok in getattr(self.knowledge, 'DETERMINERS', set()) or tok in getattr(self.knowledge, 'PREPOSITIONS', set()):
                    continue

                candidate_bases = []
                if tok.endswith('ies'):
                    candidate_bases.append(tok[:-3] + 'y')
                if tok.endswith('es'):
                    candidate_bases.append(tok[:-2])
                if tok.endswith('s'):
                    candidate_bases.append(tok[:-1])
                candidate_bases.append(tok)

                suggested = None
                chosen_base = None
                for base in candidate_bases:
                    if base in self.knowledge.IRREGULAR_VERBS:
                        suggested = self.knowledge.IRREGULAR_VERBS[base].get('past')
                        chosen_base = base
                        break

                if not suggested:
                    if tok.endswith('ies'):
                        chosen_base = tok[:-3]
                        suggested = chosen_base + 'ied'
                    elif tok.endswith('es'):
                        chosen_base = tok[:-2]
                        suggested = chosen_base + 'ed'
                    elif tok.endswith('s'):
                        chosen_base = tok[:-1]
                        suggested = chosen_base + 'ed'

                if suggested:
                    errors.append({
                        'pos': p_idx,
                        'message': f"Possible tense inconsistency: verb '{tokens[p_idx]}' looks present while sentence contains past verbs/markers",
                        'suggestion': {'type': 'replace', 'index': p_idx, 'word': suggested}
                    })

        past_markers = self.knowledge.PAST_MARKERS
        be_past = set(self.knowledge.AUXILIARY_VERBS.get('be', {}).get('past', []))
        for i, word in enumerate(tokens):
            lw = word.lower()
            if lw in past_markers or lw in be_past:
                for j in range(i + 1, min(i + 7, len(tokens))):
                    tj = tokens[j].lower()
                    if tj.endswith('s') and not tj.endswith('ss'):
                        base = None
                        if tj.endswith('ies'):
                            base = tj[:-3] + 'y'
                        elif tj.endswith('es'):
                            base = tj[:-2]
                        elif tj.endswith('s'):
                            base = tj[:-1]
                        else:
                            base = tj

                        suggested = None
                        if base in self.knowledge.IRREGULAR_VERBS:
                            suggested = self.knowledge.IRREGULAR_VERBS[base].get('past')
                        else:
                            if tj.endswith('ies'):
                                suggested = base + 'ied'
                            elif tj.endswith('es'):
                                suggested = base + 'ed'
                            elif tj.endswith('s'):
                                suggested = base + 'ed'
                                
                        if any(e.get('pos') == j for e in errors):
                            break

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
