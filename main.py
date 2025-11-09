from grammar_checker.core import GrammarChecker

def main():
    checker = GrammarChecker()
    print("Context-Aware Grammar Checker")
    print("Type 'exit' to quit")
    while True:
        sentence = input("\nEnter sentence: ")
        if sentence.lower() == "exit":
            break
        errors = checker.check(sentence)
        if errors:
            print("Potential errors detected:")
            for pos, msg in errors:
                print(f"- {msg} (token index {pos})")
        else:
            print("No errors detected!")

if __name__ == "__main__":
    main()
