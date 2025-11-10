import pytest
from grammar_checker.core import GrammarChecker

class TestGrammarCheckerIntegration:
    """Integration tests for grammar checker components"""
    
    def test_detector_integration(self):
        """Test that all detectors work together"""
        checker = GrammarChecker()
        
        # Test sentence with multiple error types
        test_sentence = "Their going to the school yesterday and she have a book."
        
        result = checker.check(test_sentence)
        
        assert 'errors' in result
        assert 'corrected_sentence' in result
        assert 'original_tokens' in result
        
        # Should detect at least some errors
        assert len(result['errors']) > 0
        
        print(f"\nIntegration Test:")
        print(f"Original: {test_sentence}")
        print(f"Corrected: {result['corrected_sentence']}")
        print(f"Errors detected: {len(result['errors'])}")
        
        for error in result['errors']:
            print(f"  - {error.get('message')}")
    
    def test_empty_sentence(self):
        """Test handling of empty input"""
        checker = GrammarChecker()
        result = checker.check("")
        
        assert result['errors'] == []
        assert result['corrected_sentence'] == ""
    
    def test_special_characters(self):
        """Test handling of sentences with special characters"""
        checker = GrammarChecker()
        
        test_cases = [
            "Hello, world!",
            "What's your name?",
            "I have 100 dollars.",
            "Email: test@example.com"
        ]
        
        for sentence in test_cases:
            result = checker.check(sentence)
            assert 'errors' in result
            assert 'corrected_sentence' in result