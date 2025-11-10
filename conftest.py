import pytest
from grammar_checker.core import GrammarChecker

@pytest.fixture
def grammar_checker():
    """Fixture to provide grammar checker instance"""
    return GrammarChecker()

@pytest.fixture
def test_dataset():
    """Fixture to provide test dataset"""
    from test_dataset import GRAMMAR_TEST_CASES, PERFORMANCE_TEST_CASES
    return {
        'grammar_cases': GRAMMAR_TEST_CASES,
        'performance_cases': PERFORMANCE_TEST_CASES
    }