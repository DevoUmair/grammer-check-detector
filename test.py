import json
from grammar_checker.core import GrammarChecker
from datetime import datetime
import re

class AccuracyTester:
    def __init__(self):
        self.checker = GrammarChecker()
        self.results = {
            'total_tests': 0,
            'passed_tests': 0,
            'failed_tests': 0,
            'accuracy': 0.0,
            'detailed_results': []
        }
    
    def run_accuracy_test(self, test_cases):
        """Run accuracy test with improved matching"""
        print("🧪 RUNNING ACCURACY TEST")
        print("=" * 60)
        
        self.results['total_tests'] = len(test_cases)
        self.results['detailed_results'] = []
        
        for i, test_case in enumerate(test_cases, 1):
            result = self._evaluate_test_case(test_case, i)
            self.results['detailed_results'].append(result)
            
            if result['status'] == 'PASS':
                self.results['passed_tests'] += 1
        
        self.results['failed_tests'] = self.results['total_tests'] - self.results['passed_tests']
        self.results['accuracy'] = (self.results['passed_tests'] / self.results['total_tests']) * 100
        
        self._generate_report()
        return self.results
    
    def _clean_text(self, text):
        """Clean text for comparison"""
        if not text:
            return ""
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\s+([.,!?])', r'\1', text)
        return text.strip().lower()
    
    def _evaluate_test_case(self, test_case, test_num):
        """Evaluate a single test case with smart matching"""
        input_text = test_case['input']
        expected_output = test_case.get('expected_output', '')
        expected_errors = test_case.get('expected_errors', [])
        
        actual_result = self.checker.check(input_text)
        actual_corrected = actual_result.get('corrected_sentence', '')
        actual_errors = actual_result.get('errors', [])
        
        clean_expected = self._clean_text(expected_output)
        clean_actual = self._clean_text(actual_corrected)
        
        status = 'PASS'
        issues = []

        should_detect_errors = len(expected_errors) > 0
        actually_detected_errors = len(actual_errors) > 0
        
        if should_detect_errors and not actually_detected_errors:
            status = 'FAIL'
            issues.append("Failed to detect expected errors")
        elif not should_detect_errors and actually_detected_errors:
            status = 'FAIL'
            issues.append("Falsely detected errors in correct sentence")
        
        if expected_errors and actual_errors:
            actual_messages = ' '.join([e.get('message', '') for e in actual_errors]).lower()
            for expected_keyword in expected_errors:
                if expected_keyword.lower() not in actual_messages:
                    status = 'FAIL'
                    issues.append(f"Missing error keyword: '{expected_keyword}'")
                    break  
                
        if expected_output and clean_expected != clean_actual:
            expected_words = set(clean_expected.split())
            actual_words = set(clean_actual.split())
            diff_count = len(expected_words.symmetric_difference(actual_words))
            
            if diff_count > 2: 
                status = 'FAIL'
                issues.append(f"Correction differs significantly (diff: {diff_count} words)")
        
        return {
            'test_number': test_num,
            'description': test_case['description'],
            'input': input_text,
            'expected_output': expected_output,
            'actual_output': actual_corrected,
            'expected_errors': expected_errors,
            'actual_errors': [e.get('message') for e in actual_errors],
            'status': status,
            'issues': issues
        }
    
    def _generate_report(self):
        """Generate comprehensive accuracy report"""
        print(f"\n{'='*80}")
        print("📊 GRAMMAR CHECKER ACCURACY REPORT")
        print(f"{'='*80}")

        print(f"\n🎯 OVERALL ACCURACY: {self.results['accuracy']:.1f}%")
        print(f"   Total Tests: {self.results['total_tests']}")
        print(f"   Passed: {self.results['passed_tests']}")
        print(f"   Failed: {self.results['failed_tests']}")

        self._show_category_breakdown()
        self._show_detailed_results()
        self._save_report()
    
    def _show_category_breakdown(self):
        """Show accuracy by error category"""
        categories = {
            'Article Errors': [],
            'Preposition Errors': [],
            'Confusion Sets': [],
            'Tense Consistency': [],
            'Subject-Verb Agreement': [],
            'Correct Sentences': []
        }
        
        for test in self.results['detailed_results']:
            desc = test['description'].lower()
            if 'article' in desc:
                categories['Article Errors'].append(test)
            elif 'preposition' in desc:
                categories['Preposition Errors'].append(test)
            elif 'confusion' in desc:
                categories['Confusion Sets'].append(test)
            elif 'tense' in desc:
                categories['Tense Consistency'].append(test)
            elif 'agreement' in desc:
                categories['Subject-Verb Agreement'].append(test)
            elif 'correct' in desc:
                categories['Correct Sentences'].append(test)
        
        print(f"\n📈 CATEGORY BREAKDOWN:")
        print(f"   {'Category':<25} {'Accuracy':<10} {'Passed':<8} {'Total':<6}")
        print(f"   {'-'*25} {'-'*10} {'-'*8} {'-'*6}")
        
        for category, tests in categories.items():
            if tests:
                passed = sum(1 for t in tests if t['status'] == 'PASS')
                total = len(tests)
                accuracy = (passed / total * 100) if total > 0 else 0
                print(f"   {category:<25} {accuracy:>6.1f}%   {passed:>2d}/{total:<2d}   {total:>2d}")
    
    def _show_detailed_results(self):
        """Show detailed test results"""
        failed_tests = [t for t in self.results['detailed_results'] if t['status'] == 'FAIL']
        
        if failed_tests:
            print(f"\n❌ FAILED TESTS ({len(failed_tests)}):")
            for test in failed_tests:
                print(f"\n   {test['test_number']:2d}. {test['description']}")
                print(f"      Input:    '{test['input']}'")
                print(f"      Expected: '{test['expected_output']}'")
                print(f"      Actual:   '{test['actual_output']}'")
                
                if test['actual_errors']:
                    print(f"      Errors detected: {len(test['actual_errors'])}")
                    for err in test['actual_errors']:
                        print(f"        - {err}")
                
                if test['issues']:
                    print(f"      Issues:")
                    for issue in test['issues']:
                        print(f"        - {issue}")
        
        passed_tests = [t for t in self.results['detailed_results'] if t['status'] == 'PASS']
        if passed_tests:
            print(f"\n✅ PASSED TESTS ({len(passed_tests)}):")
            for test in passed_tests:
                print(f"   {test['test_number']:2d}. {test['description']}")

    def _save_report(self):
        """Save detailed report to file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"accuracy_report_{timestamp}.json"
        
        report_data = {
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_tests': self.results['total_tests'],
                'passed_tests': self.results['passed_tests'],
                'failed_tests': self.results['failed_tests'],
                'accuracy': self.results['accuracy']
            },
            'detailed_results': self.results['detailed_results']
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Full report saved to: {filename}")


TEST_DATASET = [
    {
        'description': 'Article: "an" before consonant',
        'input': 'She has an dog.',
        'expected_output': 'She has a dog.',
        'expected_errors': ['article', 'an', 'dog']
    },
    {
        'description': 'Article: "a" before vowel sound',
        'input': 'He ate a apple.',
        'expected_output': 'He ate an apple.',
        'expected_errors': ['article', 'a', 'apple']
    },
    {
        'description': 'Article: unnecessary "the" with school',
        'input': 'Children go to the school.',
        'expected_output': 'Children go to school.',
        'expected_errors': ['unnecessary', 'article', 'school']
    },
    {
        'description': 'Article: unnecessary "the" with work',
        'input': 'She drives to the work.',
        'expected_output': 'She drives to work.',
        'expected_errors': ['unnecessary', 'article', 'work']
    },
    {
        'description': 'Preposition: "good in" instead of "good at"',
        'input': 'She is good in mathematics.',
        'expected_output': 'She is good at mathematics.',
        'expected_errors': ['preposition', 'good', 'mathematics']
    },
    {
        'description': 'Preposition: "arrived to" instead of "arrived at"',
        'input': 'He arrived to the station.',
        'expected_output': 'He arrived at the station.',
        'expected_errors': ['preposition', 'arrived', 'station']
    },
    {
        'description': 'Preposition: missing "to" after listen',
        'input': 'We listened music.',
        'expected_output': 'We listened to music.',
        'expected_errors': ['missing preposition', 'listened']
    },
    {
        'description': 'Preposition: "depend of" instead of "depend on"',
        'input': 'It depends of the weather.',
        'expected_output': 'It depends on the weather.',
        'expected_errors': ['preposition', 'depends', 'weather']
    },
    {
        'description': 'Confusion: Their/They\'re',
        'input': 'Their going to the party.',
        'expected_output': 'They\'re going to the party.',
        'expected_errors': ['confusion', 'Their', 'they\'re']
    },
    {
        'description': 'Confusion: Your/You\'re',
        'input': 'Your going to love this.',
        'expected_output': 'You\'re going to love this.',
        'expected_errors': ['confusion', 'Your', 'you\'re']
    },
    {
        'description': 'Confusion: Its/It\'s',
        'input': 'The dog wagged it\'s tail.',
        'expected_output': 'The dog wagged its tail.',
        'expected_errors': ['confusion', 'it\'s', 'its']
    },
    {
        'description': 'Confusion: Then/Than',
        'input': 'She is taller then him.',
        'expected_output': 'She is taller than him.',
        'expected_errors': ['confusion', 'then', 'than']
    },
    {
        'description': 'Tense: present in past narrative',
        'input': 'He was walking when he sees the dog.',
        'expected_output': 'He was walking when he saw the dog.',
        'expected_errors': ['tense', 'inconsistency', 'sees']
    },
    {
        'description': 'Tense: mixed tenses',
        'input': 'She studied hard and gets good grades.',
        'expected_output': 'She studied hard and got good grades.',
        'expected_errors': ['tense', 'inconsistency', 'gets']
    },
    {
        'description': 'Agreement: third person singular',
        'input': 'He like football.',
        'expected_output': 'He likes football.',
        'expected_errors': ['agreement', 'He', 'like']
    },
    {
        'description': 'Agreement: "each" with plural verb',
        'input': 'Each of the students have a book.',
        'expected_output': 'Each of the students has a book.',
        'expected_errors': ['agreement', 'Each', 'have']
    },
    {
        'description': 'Correct: simple present',
        'input': 'She goes to school.',
        'expected_output': 'She goes to school.',
        'expected_errors': []
    },
    {
        'description': 'Correct: with articles',
        'input': 'I have a dog and an apple.',
        'expected_output': 'I have a dog and an apple.',
        'expected_errors': []
    },
    {
        'description': 'Correct: with prepositions',
        'input': 'He is good at mathematics.',
        'expected_output': 'He is good at mathematics.',
        'expected_errors': []
    },
    {
        'description': 'Correct: question format',
        'input': 'Where are you going?',
        'expected_output': 'Where are you going?',
        'expected_errors': []
    },
]

def main():
    """Main function to run accuracy tests"""
    print("🚀 GRAMMAR CHECKER ACCURACY TEST")
    print("=" * 60)

    tester = AccuracyTester()
    results = tester.run_accuracy_test(TEST_DATASET)

    print(f"\n{'='*80}")
    print("🎯 FINAL RESULTS")
    print(f"{'='*80}")
    print(f"Overall Accuracy: {results['accuracy']:.1f}%")
    print(f"Test Coverage: {len(TEST_DATASET)} grammar rules")
    
    if results['accuracy'] >= 80:
        print("✅ Excellent performance!")
    elif results['accuracy'] >= 60:
        print("⚠️  Good performance, room for improvement")
    else:
        print("❌ Needs significant improvement")

if __name__ == "__main__":
    main()