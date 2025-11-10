import pytest
import time
from grammar_checker.core import GrammarChecker

class TestGrammarCheckerPerformance:
    """Test performance and efficiency of grammar checker"""
    
    @pytest.fixture
    def checker(self):
        return GrammarChecker()
    
    @pytest.fixture
    def performance_cases(self):
        from test_dataset import PERFORMANCE_TEST_CASES
        return PERFORMANCE_TEST_CASES
    
    def test_response_time(self, checker, performance_cases):
        """Test that response time is within acceptable limits"""
        max_response_time = 2.0  # seconds
        
        for i, sentence in enumerate(performance_cases):
            start_time = time.time()
            result = checker.check(sentence)
            end_time = time.time()
            response_time = end_time - start_time
            
            print(f"Test {i}: {response_time:.4f}s - '{sentence}'")
            
            assert response_time < max_response_time, \
                f"Response time {response_time:.4f}s exceeds limit {max_response_time}s"
    
    def test_throughput(self, checker, performance_cases):
        """Test throughput by processing multiple sentences"""
        start_time = time.time()
        
        for sentence in performance_cases:
            result = checker.check(sentence)
        
        end_time = time.time()
        total_time = end_time - start_time
        throughput = len(performance_cases) / total_time
        
        print(f"\nThroughput: {throughput:.2f} sentences/second")
        print(f"Total time for {len(performance_cases)} sentences: {total_time:.4f}s")
        
        assert throughput > 1.0, f"Throughput too low: {throughput:.2f} sentences/second"