import spacy
from grammar_checker.context import ContextAnalyzer
from grammar_checker.detectors.article import ArticleDetector
from grammar_checker.detectors.confusion_set import ConfusionSetDetector
from grammar_checker.detectors.preposition import PrepositionDetector
from grammar_checker.detectors.subject_verb_agreement import SubjectVerbAgreementDetector
from grammar_checker.detectors.tense_consistency import TenseConsistencyDetector
from grammar_checker.detectors.spelling import SpellingDetector

class GrammarChecker:
    def __init__(self):
        self.context_analyzer = ContextAnalyzer()
        self.detectors = {
            'article': ArticleDetector(),
            'confusion_set': ConfusionSetDetector(),
            'preposition': PrepositionDetector(),
            'subject_verb_agreement': SubjectVerbAgreementDetector(),
            'tense_consistency': TenseConsistencyDetector(),
            'spelling': SpellingDetector()
        }
        
    def check(self, sentence: str):
        if not sentence.strip():
            return {'errors': [], 'confidence': 1.0}
            
        try:
            context = self.context_analyzer.analyze(sentence)
            tokens = context['tokens']
            pos_tags = context['pos']
            
            all_errors = []
            
            # Run all detectors
            for detector_name, detector in self.detectors.items():
                errors = detector.detect(tokens, pos_tags, context)
                all_errors.extend(errors)
            
            # Calculate confidence score
            confidence = self._calculate_confidence(sentence, all_errors)
            
            return {
                'errors': all_errors,
                'confidence': confidence,
                'token_count': len(tokens)
            }
            
        except Exception as e:
            return {
                'errors': [{
                    'position': 0,
                    'message': f'Analysis error: {str(e)}',
                    'suggestion': 'Please check your input and try again.'
                }],
                'confidence': 0.0,
                'token_count': 0
            }
    
    def _calculate_confidence(self, sentence: str, errors: list) -> float:
        words = sentence.split()
        if not words:
            return 1.0
            
        error_ratio = len(errors) / len(words)
        confidence = max(0.0, 1.0 - error_ratio)
        return min(1.0, confidence * 0.8 + 0.2)  # Keep some base confidence