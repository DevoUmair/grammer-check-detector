# import tkinter as tk
# from grammar_checker.core import GrammarChecker

# def check_grammar():
#     text = input_box.get("1.0", tk.END).strip()
#     result = checker.check(text)
#     corrected = result.get("corrected_sentence", "")
#     errors = result.get("errors", [])
#     output_box.delete("1.0", tk.END)
#     if errors:
#         output_box.insert(tk.END, f"Corrected: {corrected}\n\nErrors:\n")
#         for e in errors:
#             output_box.insert(tk.END, f"- {e.get('message')}\n")
#     else:
#         output_box.insert(tk.END, "No errors detected!")

# checker = GrammarChecker()
# root = tk.Tk()
# root.title("Grammar Checker")

# tk.Label(root, text="Enter your sentence:").pack()
# input_box = tk.Text(root, height=5, width=50)
# input_box.pack()

# tk.Button(root, text="Check Grammar", command=check_grammar).pack(pady=5)

# output_box = tk.Text(root, height=10, width=50)
# output_box.pack()

# root.mainloop()
import tkinter as tk
import spacy
from grammar_checker.core import GrammarChecker

# Load spaCy model for POS tagging
nlp = spacy.load("en_core_web_sm")

def check_grammar():
    text = input_box.get("1.0", tk.END).strip()
    result = checker.check(text)
    corrected = result.get("corrected_sentence", "")
    errors = result.get("errors", [])

    output_box.delete("1.0", tk.END)

    if errors:
        output_box.insert(tk.END, f"Corrected: {corrected}\n\nErrors:\n")
        for e in errors:
            output_box.insert(tk.END, f"- {e.get('message')}\n")

        # Add POS tagging for the corrected sentence
        output_box.insert(tk.END, "\n\nPart-of-Speech (POS) Tags:\n")
        doc = nlp(corrected)
        for token in doc:
            output_box.insert(tk.END, f"{token.text} ({token.pos_})  ")
    else:
        output_box.insert(tk.END, "No errors detected!\n")

        # Still show POS tags even if no errors
        output_box.insert(tk.END, "\n\nPart-of-Speech (POS) Tags:\n")
        doc = nlp(text)
        for token in doc:
            output_box.insert(tk.END, f"{token.text} ({token.pos_})  ")

checker = GrammarChecker()

root = tk.Tk()
root.title("Grammar Checker")

tk.Label(root, text="Enter your sentence:").pack()
input_box = tk.Text(root, height=5, width=50)
input_box.pack()

tk.Button(root, text="Check Grammar", command=check_grammar).pack(pady=5)

output_box = tk.Text(root, height=15, width=60)
output_box.pack()

root.mainloop()
