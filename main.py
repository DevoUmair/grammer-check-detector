import tkinter as tk
from grammar_checker.core import GrammarChecker

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
    else:
        output_box.insert(tk.END, "No errors detected!")

checker = GrammarChecker()
root = tk.Tk()
root.title("Grammar Checker")

tk.Label(root, text="Enter your sentence:").pack()
input_box = tk.Text(root, height=5, width=50)
input_box.pack()

tk.Button(root, text="Check Grammar", command=check_grammar).pack(pady=5)

output_box = tk.Text(root, height=10, width=50)
output_box.pack()

root.mainloop()
