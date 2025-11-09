from grammar_checker.context import ContextAnalyzer
from grammar_checker.detectors.article import ArticleDetector
from grammar_checker.detectors.confusion_set import ConfusionSetDetector
from grammar_checker.detectors.preposition import PrepositionDetector
from grammar_checker.detectors.subject_verb_agreement import SubjectVerbAgreementDetector
from grammar_checker.detectors.tense_consistency import TenseConsistencyDetector

class GrammarChecker:
    def __init__(self):
        self.context_analyzer = ContextAnalyzer()
        self.article_detector = ArticleDetector()
        self.confusion_detector = ConfusionSetDetector()
        self.preposition_detector = PrepositionDetector()
        self.subject_verb_detector = SubjectVerbAgreementDetector()
        self.tense_detector = TenseConsistencyDetector()

    def check(self, sentence: str):
        context = self.context_analyzer.analyze(sentence)

        # Collect structured error objects from detectors. Each error is a dict:
        # {"pos": int, "message": str, "suggestion": {"type":..., ...} | None}
        errors = []
        errors.extend(self.article_detector.detect(context))
        errors.extend(self.confusion_detector.detect(context))
        errors.extend(self.preposition_detector.detect(context))
        errors.extend(self.subject_verb_detector.detect(context))
        errors.extend(self.tense_detector.detect(context))

        # Collect suggestions and apply them to produce a corrected sentence.
        suggestions = [e.get('suggestion') for e in errors if e.get('suggestion')]
        corrected_tokens = self._apply_suggestions(context.get('tokens', []), suggestions)
        corrected_sentence = ' '.join(corrected_tokens)

        return {
            'errors': errors,
            'corrected_sentence': corrected_sentence,
            'original_tokens': context.get('tokens', [])
        }

    def _apply_suggestions(self, tokens, suggestions):
        """Apply simple suggestions to a token list and return a new token list.

        Suggestions are applied in the order provided. Supported suggestion types:
        - replace: {'type':'replace','index':i,'word':new_word}
        - remove: {'type':'remove','index':i}
        - insert: {'type':'insert','index':i,'word':new_word} (insert before index)
        """
        if not suggestions:
            return list(tokens)

        tokens_out = list(tokens)
        offset = 0
        # Apply in order of ascending index to keep behavior predictable
        def keyfn(s):
            return (s.get('index', 0), 0 if s.get('type') == 'remove' else 1)

        for s in sorted(suggestions, key=keyfn):
            typ = s.get('type')
            idx = s.get('index', 0) + offset
            if typ == 'replace':
                if 0 <= idx < len(tokens_out):
                    tokens_out[idx] = s.get('word', tokens_out[idx])
            elif typ == 'remove':
                if 0 <= idx < len(tokens_out):
                    tokens_out.pop(idx)
                    offset -= 1
            elif typ == 'insert':
                if 0 <= idx <= len(tokens_out):
                    tokens_out.insert(idx, s.get('word'))
                    offset += 1

        return tokens_out
