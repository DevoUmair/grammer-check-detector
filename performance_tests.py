"""
Grammar Checker Demo - Fixes 30+ grammatically incorrect sentences
"""

from grammar_checker.core import GrammarChecker
import time

class GrammarFixerDemo:
    def __init__(self):
        self.checker = GrammarChecker()
        self.wrong_sentences = self._load_wrong_sentences()
    
    def _load_wrong_sentences(self):
        """Load a collection of grammatically incorrect sentences."""
        return [
            # Basic subject-verb agreement errors
            "He go to school every day.",
            "She like to read books.",
            "They is playing football.",
            "I has a new car.",
            "We was at the park yesterday.",
            
            # Article errors
            "She is a engineer.",
            "I saw an university.",
            "He went to the school yesterday.",  # unnecessary 'the'
            "She wants a apple.",
            "It was an unique experience.",
            
            # Confusion word errors
            "Their going to the party.",
            "You're book is on the table.",
            "Its raining outside.",
            "There going to be trouble.",
            "The effect was immediate on his mood.",  # should be 'affect'
            
            # Tense errors
            "Yesterday I go to the store.",
            "Last week she work very hard.",
            "Tomorrow I went to the doctor.",
            "When I was child, I live in Paris.",
            "He told me he is coming tomorrow.",
            
            # Preposition errors
            "She arrived to the station.",
            "I'm looking my keys.",
            "He is good in math.",
            "We discussed about the project.",
            "She married with a doctor.",
            
            # Multiple errors in one sentence
            "Their going to an university and he have a problem.",
            "She go to the school yesterday and they is happy.",
            "Me and him was late for the meeting.",
            "Each of the students have their own books.",
            "Neither John or Mary like the movie.",
            
            # Complex sentence errors
            "The team of researchers have made important discoveries.",
            "One of my friends are coming over.",
            "The data shows that the results is significant.",
            "If I was you, I would have went home earlier.",
            "The company need to improve it's customer service.",
            
            # Additional challenging cases
            "He don't know nothing about it.",
            "She sings beautiful.",
            "I could of gone to the party.",
            "Between you and I, he is wrong.",
            "The reason is because I was tired."
        ]
    
    def run_demo(self):
        """Run the grammar fixing demo."""
        print("🚀 GRAMMAR FIXER DEMO")
        print("=" * 70)
        print("Fixing 30+ grammatically incorrect sentences...")
        print("=" * 70)
        
        total_sentences = len(self.wrong_sentences)
        fixed_count = 0
        improvement_count = 0
        
        for i, sentence in enumerate(self.wrong_sentences, 1):
            print(f"\n{i:2d}/{total_sentences} 📝 ORIGINAL: {sentence}")
            
            result = self.checker.check(sentence)
            
            if result['errors']:
                print(f"    ⚠️  ERRORS FOUND: {len(result['errors'])}")
                for error in result['errors']:
                    print(f"       - {error['message']}")
                    if error.get('suggestion'):
                        sugg = error['suggestion']
                        if sugg['type'] == 'replace':
                            print(f"         💡 Suggestion: Replace '{sentence.split()[sugg['index']]}' with '{sugg['word']}'")
                        elif sugg['type'] == 'remove':
                            print(f"         💡 Suggestion: Remove '{sentence.split()[sugg['index']]}'")
                        elif sugg['type'] == 'insert':
                            print(f"         💡 Suggestion: Insert '{sugg['word']}' after '{sentence.split()[sugg['index']-1]}'")
                
                corrected = result['corrected_sentence']
                if corrected != sentence:
                    print(f"    ✅ CORRECTED: {corrected}")
                    fixed_count += 1
                else:
                    print(f"    ❌ NO CORRECTION APPLIED")
                    corrected = sentence
            else:
                corrected = sentence
                print(f"    ✅ NO ERRORS DETECTED")
            
            # Check if the sentence was improved
            if corrected != sentence:
                improvement_count += 1
            
            # Add small delay for better readability in output
            time.sleep(0.1)
        
        # Summary
        print("\n" + "=" * 70)
        print("📊 DEMO SUMMARY")
        print("=" * 70)
        print(f"Total sentences processed: {total_sentences}")
        print(f"Sentences with errors detected: {fixed_count}")
        print(f"Sentences improved: {improvement_count}")
        print(f"Improvement rate: {improvement_count/total_sentences*100:.1f}%")
        
        if improvement_count == total_sentences:
            print("🎉 Excellent! All sentences were improved!")
        elif improvement_count >= total_sentences * 0.7:
            print("✅ Good performance! Most sentences were improved.")
        elif improvement_count >= total_sentences * 0.5:
            print("⚠️  Fair performance. About half the sentences were improved.")
        else:
            print("❌ Needs improvement. Less than half the sentences were improved.")
    
    def show_detailed_comparison(self):
        """Show a detailed before/after comparison."""
        print("\n" + "=" * 70)
        print("📋 DETAILED COMPARISON")
        print("=" * 70)
        
        comparisons = []
        
        for sentence in self.wrong_sentences[:10]:  # Show first 10 for brevity
            result = self.checker.check(sentence)
            corrected = result['corrected_sentence']
            error_count = len(result['errors'])
            
            comparisons.append({
                'original': sentence,
                'corrected': corrected,
                'errors': error_count,
                'improved': corrected != sentence
            })
        
        print("\nBefore → After Comparison:")
        print("-" * 70)
        
        for comp in comparisons:
            status = "✅ IMPROVED" if comp['improved'] else "❌ UNCHANGED"
            print(f"\n{status} ({comp['errors']} errors detected)")
            print(f"BEFORE: {comp['original']}")
            print(f"AFTER:  {comp['corrected']}")
    
    def test_specific_categories(self):
        """Test specific grammar categories."""
        print("\n" + "=" * 70)
        print("🔍 CATEGORY ANALYSIS")
        print("=" * 70)
        
        categories = {
            'Subject-Verb Agreement': [
                "He go to school.",
                "They is happy.",
                "She have a cat.",
                "Each of the students have books.",
                "The list of items are long.",
                "My brother like to play.",
                "Everyone know the answer.",
                "The dogs barks at night.",
                "Mathematics are difficult for me.",
                "The team are winning."
            ],

            'Article Usage': [
                "She is a engineer.",
                "I saw an university.",
                "He went to the school.",
                "She wants a apple.",
                "I need an help.",
                "We visited a Eiffel Tower.",
                "He bought a umbrella.",
                "She adopted an unique strategy.",
                "He is the honest person.",
                "I ate the breakfast."
            ],

            'Confusion Words': [
                "Their going to park.",
                "You're book is here.",
                "Its raining.",
                "There going to be fun.",
                "I can't bare this pain.",
                "She needs to except the truth.",
                "Your the best friend I have.",
                "He lost all of he's money.",
                "Their house is over their.",
                "I want to loose weight."
            ],

            'Tense Consistency': [
                "Yesterday I go to store.",
                "Last week she work hard.",
                "When I was child, I live there.",
                "She was crying when he arrives.",
                "I eat dinner and went to sleep.",
                "He walks in and told me to leave.",
                "They were playing when the rain starts.",
                "I will call you yesterday.",
                "She goes to the market and bought fruits.",
                "We were happy until he interrupts."
            ],

            'Preposition Usage': [
                "She arrived to station.",
                "I'm looking my keys.",
                "He is good in math.",
                "We discussed about the plan.",
                "He depends of his parents.",
                "I will meet you in Monday.",
                "She is married with a doctor.",
                "They apologized to the mistake.",
                "I prefer coffee than tea.",
                "He is responsible of the event."
            ]
        }

        
        for category, sentences in categories.items():
            print(f"\n{category}:")
            print("-" * 40)
            
            for sentence in sentences:
                result = self.checker.check(sentence)
                corrected = result['corrected_sentence']
                
                if corrected != sentence:
                    print(f"  ✅ {sentence} → {corrected}")
                else:
                    print(f"  ❌ {sentence} (no change)")
    
    def benchmark_performance(self):
        """Simple performance benchmark."""
        print("\n" + "=" * 70)
        print("⏱️  PERFORMANCE BENCHMARK")
        print("=" * 70)
        
        import time
        
        start_time = time.time()
        
        for sentence in self.wrong_sentences:
            self.checker.check(sentence)
        
        end_time = time.time()
        total_time = end_time - start_time
        
        print(f"Processed {len(self.wrong_sentences)} sentences in {total_time:.2f} seconds")
        print(f"Average time per sentence: {total_time/len(self.wrong_sentences)*1000:.1f} ms")
        
        if total_time/len(self.wrong_sentences) < 0.1:
            print("⚡ Excellent performance - suitable for real-time use")
        elif total_time/len(self.wrong_sentences) < 0.5:
            print("✅ Good performance - suitable for interactive use")
        else:
            print("⚠️  Performance could be improved")
            
    # def test_specific_categories(self):
    #     """Test specific grammar categories."""
    #     print("\n" + "=" * 70)
    #     print("🔍 CATEGORY ANALYSIS")
    #     print("=" * 70)
        
    #     categories = {
    #         'Tense Consistency': [
    #             # Basic tense errors
    #             "Yesterday I go to store.",
    #             "Last week she work hard.", 
    #             "When I was child, I live there.",
    #             "She was crying when he arrives.",
    #             "I eat dinner and went to sleep.",
    #             "He walks in and told me to leave.",
    #             "They were playing when the rain starts.",
    #             "I will call you yesterday.",
    #             "She goes to the market and bought fruits.",
    #             "We were happy until he interrupts.",
                
    #             # Time clause sentences
    #             "When I was young, I play football every day.",
    #             "While she cooked dinner, he watch TV.",
    #             "Before I left, I forget to lock the door.",
    #             "After he finish work, he goes to the gym.",
    #             "Until she calls, I wait here.",
    #             "Since I move here, I meet many friends.",
    #             "Once you understand the rules, it become easy.",
    #             "As I walk home, it start to rain.",
                
    #             # Conditional sentences
    #             "If I have money, I will buys a car.",
    #             "If I was taller, I plays basketball.",
    #             "If I had studied, I passes the exam.",
    #             "If it rain, we cancels the picnic.",
    #             "Unless you hurries, you misses the bus.",
    #             "Provided that you works hard, you succeeds.",
                
    #             # Auxiliary conflicts
    #             "Tomorrow I was going to the park.",
    #             "Last year I will visit my grandparents.",
    #             "Next week she had a party.",
    #             "Yesterday they will arrive late.",
                
    #             # Mixed tense in compound sentences
    #             "I wake up early and went for a run.",
    #             "She cooks dinner and then watched a movie.",
    #             "They study hard and gets good grades.",
    #             "He works all day and then play video games.",
                
    #             # Third person singular errors
    #             "He like to read books.",
    #             "She don't know the answer.",
    #             "It look very beautiful.",
    #             "My brother have a new car.",
                
    #             # Future in the past
    #             "I thought I will see you tomorrow.",
    #             "She said she will comes later.",
    #             "They promised they will helps us.",
                
    #             # Present perfect context
    #             "I already eat lunch.",
    #             "She never visits Paris.",
    #             "They just finish their homework.",
                
    #             # Past perfect context  
    #             "After I ate, I realized I forget my keys.",
    #             "When she arrived, he already leaves.",
    #             "By the time we got there, the movie start.",
                
    #             # Modal + base form protection
    #             "I can speaks three languages.",
    #             "She should takes a break.",
    #             "They might goes to the party.",
    #             "We must finishes this project.",
                
    #             # Infinitive protection
    #             "I want to goes home.",
    #             "She needs to buys groceries.",
    #             "They try to finds a solution.",
    #             "He hopes to meets her soon.",
                
    #             # Complex mixed cases
    #             # "If I know you were coming, I will bake a cake.",
    #             # "When she calls, I was watching TV and eats popcorn.",
    #             # "Yesterday I think I will goes to the store but then I remembers it is closed.",
    #             # "She said she will calls me when she arrives, but I never hears from her."
    #         ],
    #             # ... other categories
    #     }

        # for category, sentences in categories.items():
        #     print(f"\n{category}:")
        #     print("-" * 40)
            
        #     for sentence in sentences:
        #         result = self.checker.check(sentence)
        #         corrected = result['corrected_sentence']
                
        #         # Show detected tense if available
        #         tense_info = None
        #         for error in result.get('errors', []):
        #             if error.get('type') == 'tense_info':
        #                 tense_info = error.get('tense')
        #                 break
                
        #         if corrected != sentence:
        #             tense_str = f" [{tense_info}]" if tense_info else ""
        #             print(f"  ✅ {sentence} → {corrected}{tense_str}")
        #         else:
        #             tense_str = f" [{tense_info}]" if tense_info else ""
        #             print(f"  ❌ {sentence} (no change){tense_str}")

def main():
    """Run the grammar fixer demo."""
    demo = GrammarFixerDemo()
    
    # Run the main demo
    # demo.run_demo()
    
    # Show detailed comparison
    # demo.show_detailed_comparison()
    
    # Test specific categories
    demo.test_specific_categories()
    
    # Benchmark performance
    # demo.benchmark_performance()
    
    print("\n" + "=" * 70)
    print("🎯 DEMO COMPLETED")
    print("=" * 70)
    print("The grammar checker has demonstrated its ability to:")
    print("• Detect various types of grammatical errors")
    print("• Provide specific suggestions for corrections") 
    print("• Automatically generate corrected sentences")
    print("• Handle complex sentences with multiple errors")

if __name__ == "__main__":
    main()