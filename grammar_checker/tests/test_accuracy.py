import pytest
import time
from grammar_checker.core import GrammarChecker

class TestGrammarCheckerAccuracy:
    """Test accuracy of grammar checker using comprehensive test dataset"""
    
    @pytest.fixture
    def checker(self):
        return GrammarChecker()
    
    @pytest.fixture
    def test_cases(self):
        from test_dataset import GRAMMAR_TEST_CASES
        return GRAMMAR_TEST_CASES
    
    def test_individual_cases(self, checker, test_cases):
        """Test individual test cases and collect results"""
        results = []
        
        for i, test_case in enumerate(test_cases):
            sentence = test_case["input_sentence"]
            expected_errors = test_case["expected_errors"]
            
            # Get actual results
            result = checker.check(sentence)
            actual_errors = result.get("errors", [])
            corrected_sentence = result.get("corrected_sentence", "")
            
            # Calculate metrics for this test case
            true_positives = 0
            false_positives = 0
            false_negatives = 0
            
            # Check for expected errors that were detected
            for expected_error in expected_errors:
                expected_pos = expected_error["pos"]
                expected_type = expected_error["type"]
                
                found = False
                for actual_error in actual_errors:
                    if (abs(actual_error.get('pos', -1) - expected_pos) <= 2 and
                        expected_type in actual_error.get('message', '').lower()):
                        true_positives += 1
                        found = True
                        break
                
                if not found:
                    false_negatives += 1
            
            # Check for unexpected errors (false positives)
            for actual_error in actual_errors:
                actual_pos = actual_error.get('pos', -1)
                found_expected = False
                
                for expected_error in expected_errors:
                    expected_pos = expected_error["pos"]
                    if abs(actual_pos - expected_pos) <= 2:
                        found_expected = True
                        break
                
                if not found_expected and len(expected_errors) > 0:
                    false_positives += 1
            
            results.append({
                "test_case": i,
                "sentence": sentence,
                "true_positives": true_positives,
                "false_positives": false_positives,
                "false_negatives": false_negatives,
                "expected_errors": len(expected_errors),
                "actual_errors": len(actual_errors),
                "corrected_sentence": corrected_sentence
            })
        
        return results
    
    def test_accuracy_metrics(self, checker, test_cases):
        """Calculate overall accuracy metrics"""
        results = self.test_individual_cases(checker, test_cases)
        
        total_true_positives = sum(r["true_positives"] for r in results)
        total_false_positives = sum(r["false_positives"] for r in results)
        total_false_negatives = sum(r["false_negatives"] for r in results)
        total_expected_errors = sum(r["expected_errors"] for r in results)
        
        # Calculate metrics
        precision = (total_true_positives / (total_true_positives + total_false_positives) 
                    if (total_true_positives + total_false_positives) > 0 else 0)
        recall = (total_true_positives / (total_true_positives + total_false_negatives) 
                 if (total_true_positives + total_false_negatives) > 0 else 0)
        f1_score = (2 * precision * recall / (precision + recall) 
                   if (precision + recall) > 0 else 0)
        accuracy = (total_true_positives / total_expected_errors 
                   if total_expected_errors > 0 else 1.0)
        
        # Print detailed results
        print("\n" + "="*60)
        print("GRAMMAR CHECKER ACCURACY REPORT")
        print("="*60)
        
        for result in results:
            status = "✅ PASS" if result["true_positives"] >= result["expected_errors"] else "❌ FAIL"
            print(f"\nTest {result['test_case']:2d}: {status}")
            print(f"  Sentence: '{result['sentence']}'")
            print(f"  Expected errors: {result['expected_errors']}, Found: {result['actual_errors']}")
            print(f"  TP: {result['true_positives']}, FP: {result['false_positives']}, FN: {result['false_negatives']}")
            if result['corrected_sentence']:
                print(f"  Corrected: '{result['corrected_sentence']}'")
        
        print("\n" + "="*60)
        print("OVERALL METRICS:")
        print(f"  Precision:    {precision:.3f} ({total_true_positives}/{(total_true_positives + total_false_positives)})")
        print(f"  Recall:       {recall:.3f} ({total_true_positives}/{(total_true_positives + total_false_negatives)})")
        print(f"  F1-Score:     {f1_score:.3f}")
        print(f"  Accuracy:     {accuracy:.3f}")
        print(f"  Total Tests:  {len(results)}")
        print("="*60)
        
        # Assert minimum performance thresholds
        assert precision >= 0.6, f"Precision too low: {precision:.3f}"
        assert recall >= 0.5, f"Recall too low: {recall:.3f}"
        assert f1_score >= 0.5, f"F1-score too low: {f1_score:.3f}"