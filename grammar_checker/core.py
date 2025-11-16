from grammar_checker.context import ContextAnalyzer
from grammar_checker.detectors.article import ArticleDetector
from grammar_checker.detectors.confusion_set import ConfusionSetDetector
from grammar_checker.detectors.preposition import PrepositionDetector
from grammar_checker.detectors.subject_verb_agreement import SubjectVerbAgreementDetector
from grammar_checker.detectors.tense_consistency import TenseConsistencyDetector
from grammar_checker.detectors.helping_verb import HelpingVerbDetector

class GrammarChecker:
    def __init__(self):
        self.context_analyzer = ContextAnalyzer()
        self.article_detector = ArticleDetector()
        # self.confusion_detector = ConfusionSetDetector()
        self.preposition_detector = PrepositionDetector()
        self.subject_verb_detector = SubjectVerbAgreementDetector()
        self.tense_detector = TenseConsistencyDetector()
        self.helping_verb_detector = HelpingVerbDetector() 

    def check(self, sentence: str):
        """Check grammar of a sentence."""
        context = self.context_analyzer.analyze(sentence)

        errors = []
        errors.extend(self.article_detector.detect(context))
        # errors.extend(self.confusion_detector.detect(context))
        errors.extend(self.preposition_detector.detect(context))
        errors.extend(self.subject_verb_detector.detect(context))
        errors.extend(self.tense_detector.detect(context))
        errors.extend(self.helping_verb_detector.detect(context))

        suggestions = [e.get('suggestion') for e in errors if e.get('suggestion')]
        corrected_tokens = self._apply_suggestions(context.get('tokens', []), suggestions)
        corrected_sentence = ' '.join(corrected_tokens)

        return {
            'errors': errors,
            'corrected_sentence': corrected_sentence,
            'original_tokens': context.get('tokens', [])
        }

    def _apply_suggestions(self, tokens, suggestions):
        """Apply suggestions to token list and fix punctuation spacing."""
        if not suggestions:
            return self._fix_punctuation_spacing(tokens)

        tokens_out = list(tokens)
        offset = 0
        
        for s in sorted(suggestions, key=lambda x: x.get('index', 0)):
            typ = s.get('type')
            idx = s.get('index', 0) + offset
            
            if typ == 'replace' and 0 <= idx < len(tokens_out):
                tokens_out[idx] = s.get('word', tokens_out[idx])
            elif typ == 'remove' and 0 <= idx < len(tokens_out):
                tokens_out.pop(idx)
                offset -= 1
            elif typ == 'insert' and 0 <= idx <= len(tokens_out):
                tokens_out.insert(idx, s.get('word'))
                offset += 1

        return self._fix_punctuation_spacing(tokens_out)

    def _fix_punctuation_spacing(self, tokens):
        """Remove spaces before punctuation."""
        if not tokens:
            return tokens
        
        punctuation = {'.', ',', '!', '?', ';', ':', "'", '"'}
        result = []
        
        for i, token in enumerate(tokens):
            if token in punctuation and result:
                result[-1] = result[-1] + token
            else:
                result.append(token)
        
        return result