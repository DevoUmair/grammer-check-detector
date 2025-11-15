from grammar_checker.knowledge import LinguisticKnowledge

class SubjectVerbAgreementDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, sentence_or_context):
        if isinstance(sentence_or_context, dict):
            tokens = sentence_or_context.get('tokens', [])
        else:
            tokens = sentence_or_context or []

        errors = []

        third_person_pronouns = {'he', 'she', 'it'}
        auxiliaries = set()
        for v in self.knowledge.AUXILIARY_VERBS.values():
            if isinstance(v, dict):
                auxiliaries.update(v.get('present', []))
            elif isinstance(v, list):
                auxiliaries.update(v)

        for i, word in enumerate(tokens[:-1]):
            lw = word.lower()
            if lw in third_person_pronouns:
                for j in range(i + 1, min(i + 4, len(tokens))):
                    candidate = tokens[j]
                    cl = candidate.lower()
                    if cl in auxiliaries:
                        break
                    if cl.endswith('ed') or cl.endswith('ing') or cl in ('is', 'are', 'was', 'were', 'has', 'have'):
                        break

                    needs_suggest = False
                    suggested_form = None
                    base = cl.rstrip('.?,!')
                    if base in self.knowledge.IRREGULAR_VERBS:
                        suggested_form = self.knowledge.IRREGULAR_VERBS[base].get('present_3sg') or self.knowledge.IRREGULAR_VERBS[base].get('present_3sg', None)
                        if suggested_form and not (cl.endswith('s') or cl.endswith('es')):
                            needs_suggest = True
                    else:
                        if not (cl.endswith('s') or cl.endswith('es')) and cl.isalpha():
                            suggested_form = cl + 's'
                            needs_suggest = True

                    if needs_suggest and suggested_form:
                        errors.append({
                            'pos': j,
                            'message': f"Possible agreement error: subject '{word}' may require 3rd-person singular verb form at '{candidate}'",
                            'suggestion': {'type': 'replace', 'index': j, 'word': suggested_form}
                        })
                    break

        for i, word in enumerate(tokens):
            if word.lower() == 'each':
                for j in range(i + 1, min(i + 6, len(tokens))):
                    if tokens[j].lower() == 'of':
                        for k in range(j + 1, min(len(tokens), j + 6)):
                            tok = tokens[k].lower()
                            if tok in ('have', 'are', 'were'):
                                replacement = 'has' if tok == 'have' else ('is' if tok == 'are' else 'was')
                                errors.append({
                                    'pos': k,
                                    'message': f"Agreement: 'Each' is singular; '{tokens[k]}' should be '{replacement}'",
                                    'suggestion': {'type': 'replace', 'index': k, 'word': replacement}
                                })
                                break
                        break

        for i, word in enumerate(tokens):
            if word.lower() == 'of' and i - 1 >= 0:
                head = tokens[i - 1]
                for j in range(i + 1, min(len(tokens), i + 6)):
                    tok = tokens[j].lower()
                    if tok in ('is', 'are', 'was', 'were', 'has', 'have'):
                        if not head.lower().endswith('s') and tok in ('are', 'have', 'were'):
                            replacement = 'is' if tok == 'are' else ('has' if tok == 'have' else 'was')
                            errors.append({
                                'pos': j,
                                'message': f"Subject-verb agreement: '{head}' is singular; '{tokens[j]}' should be '{replacement}'",
                                'suggestion': {'type': 'replace', 'index': j, 'word': replacement}
                            })
                        break
        return errors
