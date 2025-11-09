from grammar_checker.core import GrammarChecker

def main():
    checker = GrammarChecker()
    print("=" * 60)
    print("           ADVANCED GRAMMAR CHECKER")
    print("=" * 60)
    print("Type 'exit' to quit\n")
    
    while True:
        sentence = input("Enter sentence: ").strip()
        
        if sentence.lower() == 'exit':
            print("Goodbye!")
            break
            
        if not sentence:
            continue
            
        print(f"\nAnalyzing: '{sentence}'")
        print("-" * 40)
        
        results = checker.check(sentence)
        
        if results['errors']:
            print("❌ Potential errors detected:")
            for error in results['errors']:
                print(f"   • Position {error['position']}: {error['message']}")
                print(f"     Suggestion: {error['suggestion']}")
                print()
        else:
            print("✅ No grammar errors detected!")
            
        print(f"Confidence Score: {results['confidence']:.1%}")
        print("-" * 40)

if __name__ == "__main__":
    main()