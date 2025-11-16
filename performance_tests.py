from grammar_checker.core import GrammarChecker
import time
import traceback
import json
from datetime import datetime

class GrammarFixerDemo:
    def __init__(self):
        self.checker = GrammarChecker()
        self.wrong_sentences = [
            "He go to school every day.",
            "She like to read books.",
            "They is playing football.",
            "I has a new car.",
            "We was at the park yesterday.",
            "She is a engineer.",
            "I saw an university.",
            "He went to the school yesterday.",
            "She wants a apple.",
            "It was an unique experience.",
            "Their going to the party.",
            "You're book is on the table.",
            "Its raining outside.",
            "There going to be trouble.",
            "The effect was immediate on his mood.",
            "Yesterday I go to the store.",
            "Last week she work very hard.",
            "Tomorrow I went to the doctor.",
            "When I was child, I live in Paris.",
            "He told me he is coming tomorrow.",
            "She arrived to the station.",
            "I'm looking my keys.",
            "He is good in math.",
            "We discussed about the project.",
            "She married with a doctor.",
            "Their going to an university and he have a problem.",
            "Me and him was late for the meeting.",
            "Each of the students have their own books.",
            "Neither John or Mary like the movie.",
            "The team of researchers have made important discoveries.",
            "One of my friends are coming over.",
            "The data shows that the results is significant.",
            "If I was you, I would have went home earlier.",
            "The company need to improve it's customer service.",
            "He don't know nothing about it.",
            "She sings beautiful.",
            "I could of gone to the party.",
            "Between you and I, he is wrong.",
            "The reason is because I was tired."
        ]
    
    def run_demo(self):
        print("🚀 GRAMMAR FIXER DEMO")
        print("=" * 70)
        print("Fixing grammatically incorrect sentences...")
        print("=" * 70)
        
        total_sentences = len(self.wrong_sentences)
        fixed_count = 0
        improvement_count = 0
        error_count = 0
        results = []
        
        for i, sentence in enumerate(self.wrong_sentences, 1):
            print(f"\n{i:2d}/{total_sentences} 📝 ORIGINAL: {sentence}")
            
            try:
                result = self.checker.check(sentence)
                test_result = {
                    'sentence_id': i,
                    'original': sentence,
                    'errors_found': len(result['errors']),
                    'corrected': result['corrected_sentence'],
                    'improved': result['corrected_sentence'] != sentence,
                    'errors': []
                }
                
                if result['errors']:
                    print(f"    ⚠️  ERRORS FOUND: {len(result['errors'])}")
                    for error in result['errors']:
                        error_data = {
                            'message': error['message'],
                            'suggestion': error.get('suggestion')
                        }
                        test_result['errors'].append(error_data)
                        print(f"       - {error['message']}")
                        if error.get('suggestion'):
                            sugg = error['suggestion']
                            if sugg['type'] == 'replace':
                                words = sentence.split()
                                if sugg['index'] < len(words):
                                    original_word = words[sugg['index']]
                                    print(f"         💡 Suggestion: Replace '{original_word}' with '{sugg['word']}'")
                            elif sugg['type'] == 'remove':
                                words = sentence.split()
                                if sugg['index'] < len(words):
                                    word_to_remove = words[sugg['index']]
                                    print(f"         💡 Suggestion: Remove '{word_to_remove}'")
                            elif sugg['type'] == 'insert':
                                words = sentence.split()
                                if sugg['index'] - 1 < len(words) and sugg['index'] - 1 >= 0:
                                    previous_word = words[sugg['index'] - 1]
                                    print(f"         💡 Suggestion: Insert '{sugg['word']}' after '{previous_word}'")
                    
                    corrected = result['corrected_sentence']
                    if corrected != sentence:
                        print(f"    ✅ CORRECTED: {corrected}")
                        fixed_count += 1
                    else:
                        print(f"    ❌ NO CORRECTION APPLIED")
                else:
                    print(f"    ✅ NO ERRORS DETECTED")
                
                if result['corrected_sentence'] != sentence:
                    improvement_count += 1
                    
            except Exception as e:
                print(f"    🔴 ERROR PROCESSING SENTENCE: {str(e)}")
                error_count += 1
                test_result = {
                    'sentence_id': i,
                    'original': sentence,
                    'error': str(e),
                    'improved': False
                }
            
            results.append(test_result)
            time.sleep(0.1)
        
        print("\n" + "=" * 70)
        print("📊 DEMO SUMMARY")
        print("=" * 70)
        print(f"Total sentences processed: {total_sentences}")
        print(f"Sentences with errors detected: {fixed_count}")
        print(f"Sentences improved: {improvement_count}")
        print(f"Processing errors: {error_count}")
        
        if total_sentences - error_count > 0:
            success_rate = (improvement_count / (total_sentences - error_count)) * 100
            print(f"Success rate: {success_rate:.1f}%")
        
        return results, {
            'total_sentences': total_sentences,
            'sentences_with_errors_detected': fixed_count,
            'sentences_improved': improvement_count,
            'processing_errors': error_count,
            'success_rate': success_rate if total_sentences - error_count > 0 else 0
        }
    
    def generate_json_report(self, results, summary):
        report = {
            'test_report': {
                'timestamp': datetime.now().isoformat(),
                'summary': summary,
                'detailed_results': results
            }
        }
        
        filename = f"grammar_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 JSON report saved to: {filename}")
        return filename

def main():
    demo = GrammarFixerDemo()
    results, summary = demo.run_demo()
    demo.generate_json_report(results, summary)
    
    print("\n" + "=" * 70)
    print("🎯 DEMO COMPLETED")
    print("=" * 70)

if __name__ == "__main__":
    main()