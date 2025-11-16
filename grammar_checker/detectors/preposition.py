from grammar_checker.knowledge import LinguisticKnowledge

class PrepositionDetector:
    def __init__(self):
        self.kb = LinguisticKnowledge()

        # Universal replacement rules
        self.UNIVERSAL_RULES = {
            ('discuss', 'about'): None,
            ('married', 'with'): 'to',
            ('different', 'than'): 'from',
            ('prefer', 'than'): 'to',
            ('capable', 'for'): 'of',
            ('responsible', 'of'): 'for',
            ('angry', 'on'): 'with',
            ('good', 'in'): 'at',
            ('interested', 'on'): 'in',
            ('depend', 'of'): 'on',
            ('believe', 'on'): 'in',
        }

        # Days & months
        self.DAYS = {"monday","tuesday","wednesday","thursday","friday","saturday","sunday"}
        self.MONTHS = {
            "january","february","march","april","may","june",
            "july","august","september","october","november","december"
        }

    def detect(self, context):
        tokens = context.get("tokens", [])
        pos = context.get("pos", [])
        errors = []

        for i, tok in enumerate(tokens):
            low = tok.lower()

            # 1 — UNIVERSAL RULES
            if i > 0:
                prev = tokens[i-1].lower()
                key = (prev, low)
                if key in self.UNIVERSAL_RULES:
                    correct = self.UNIVERSAL_RULES[key]
                    if correct is None:
                        errors.append(self._make_remove(i, prev, low))
                    else:
                        errors.append(self._make_replace(i, prev, low, correct))

            # 2 — COLLOCATION RULES
            if i > 0:
                prev = tokens[i-1].lower()
                if prev in self.kb.PREPOSITION_COLLOCATIONS:
                    valid_map = self.kb.PREPOSITION_COLLOCATIONS[prev]

                    # If current preposition is correct, skip
                    if low in valid_map:
                        pass
                    else:
                        # Check if following noun requires a specific prep
                        for expected_prep, nouns in valid_map.items():
                            if i+1 < len(tokens) and tokens[i+1].lower() in nouns:
                                errors.append(
                                    self._make_replace(i, prev, low, expected_prep)
                                )

            # 3 — TIME / LOCATION RULES
            if low in {"in", "on", "at"} and i+1 < len(tokens):
                nxt = tokens[i+1].lower()

                # Days → on
                if nxt in self.DAYS and low != "on":
                    errors.append(self._make_replace(i, low, nxt, "on"))

                # Months → in
                if nxt in self.MONTHS and low != "in":
                    errors.append(self._make_replace(i, low, nxt, "in"))

                # Night → at
                if nxt == "night" and low != "at":
                    errors.append(self._make_replace(i, low, nxt, "at"))

        return errors


    def _make_replace(self, index, prev, wrong, correct):
        return {
            "type": "replace",
            "index": index,
            "word": correct,
            "message": f"Preposition '{wrong}' is incorrect after '{prev}'. Use '{correct}'.",
            "suggestion": {
                "type": "replace",
                "index": index,
                "word": correct
            }
        }

    def _make_remove(self, index, prev, wrong):
        return {
            "type": "remove",
            "index": index,
            "word": wrong,
            "message": f"Unnecessary preposition '{wrong}' after '{prev}'.",
            "suggestion": {
                "type": "remove",
                "index": index
            }
        }
