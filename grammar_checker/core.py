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
        tokens = context['tokens']

        errors = []
        errors.extend(self.article_detector.detect(tokens))
        errors.extend(self.confusion_detector.detect(tokens))
        errors.extend(self.preposition_detector.detect(tokens))
        errors.extend(self.subject_verb_detector.detect(tokens))
        errors.extend(self.tense_detector.detect(tokens))

        return errors
