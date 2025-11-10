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
                # look for next verb-like token in the next 3 tokens
                for j in range(i + 1, min(i + 4, len(tokens))):
                    candidate = tokens[j]
                    cl = candidate.lower()
                    if cl in auxiliaries:
                        # auxiliary present, less likely an agreement issue
                        break
                    # naive verb check: present 3sg should end with 's' or be irregular 's'
                    needs_suggest = False
                    suggested_form = None
                    base = cl.rstrip('.?,!')
                    if base in self.knowledge.IRREGULAR_VERBS:
                        suggested_form = self.knowledge.IRREGULAR_VERBS[base].get('s')
                        if suggested_form and not (cl.endswith('s') or cl.endswith('es')):
                            needs_suggest = True
                    else:
                        # regular verbs: if it doesn't end with 's' or 'es', suggest adding 's'
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
        return errors