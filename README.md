# Grammar Check Detector

A small, rule-based context-aware grammar checker written in Python. It analyzes sentences and returns a list of potential grammar issues together with simple correction suggestions, and can produce a corrected sentence by applying those suggestions.

This repository is a lightweight educational tool — detectors are heuristic/rule-based and make conservative suggestions. For better parsing (subject/verb detection, dependency info) you can enable spaCy and its `en_core_web_sm` model.

**Contents**
- `main.py` — simple Tkinter UI to enter a sentence and see results (also shows POS tags when spaCy is available).
- `test_runner.py` — non-interactive script that runs a set of example sentences and prints corrections and detector messages.
- `grammar_checker/` — core package
  - `core.py` — `GrammarChecker` orchestration, applies detector suggestions and builds `corrected_sentence`.
  - `context.py` — sentence analyzer; uses spaCy if installed, otherwise falls back to a simple tokenizer.
  - `knowledge.py` — linguistic knowledge (prepositions, irregular verbs, collocations).
  - `detectors/` — rule-based detectors. Key detectors: `article.py`, `preposition.py`, `subject_verb_agreement.py`, `tense_consistency.py`, `confusion_set.py`.

## Installation

1. Create a virtual environment (recommended):

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install the minimal requirements (if a `requirements.txt` exists):

```powershell
pip install -r requirements.txt
```

3. (Optional) Install spaCy and the small English model for richer parsing:

```powershell
pip install spacy
py -m spacy download en_core_web_sm
```

If spaCy or the model is missing, the tool still runs — `ContextAnalyzer` will fall back to a simple whitespace tokenizer. However, detectors benefit from spaCy's POS/dependency information when available.

## Usage

- GUI (Tkinter):

```powershell
py main.py
```

- CLI/example runner to exercise built-in test sentences:

```powershell
py test_runner.py
```

- Programmatic usage (import API):

```python
from grammar_checker.core import GrammarChecker

checker = GrammarChecker()
result = checker.check("She adopted an dog from the shelter.")
print(result['corrected_sentence'])
print(result['errors'])
```

`GrammarChecker.check(sentence)` returns a dict with keys:
- `errors`: list of structured error dicts: `{'pos': int, 'message': str, 'suggestion': dict|None}`
- `corrected_sentence`: the token-joined sentence after applying detector suggestions (simple token-based replacement)
- `original_tokens`: the token list produced by the tokenizer / spaCy doc

## Examples and behavior
The detectors are rule-based and targeted to common issues. Examples handled by the included `test_runner.py`:
- Article fixes: `She adopted an dog` → `She adopted a dog` (fix `a/an` and prefer `the` before proper nouns)
- Preposition collocations: `She is good in mathematics` → `She is good at mathematics` (suggest `at` for `good`)
- Arrival prepositions: `He arrived to the office` → `He arrived at the office` (suggest `at`)
- Tense consistency: `He was walking to school when he sees a dog` → `... when he saw a dog` (suggest changing present to past)
- Subject–verb agreement: `The list of items are on the table` → `... is on the table`; `Each of the students have a laptop` → `Each ... has a laptop`
- Confusion sets: `Their going to win` → suggest `there` / `they're` alternatives

These corrections are heuristic and conservative. The system attempts to prefer known irregular forms (e.g., `sees` → `saw`) where possible.

## Design notes
- Detectors accept a `context` dict from `ContextAnalyzer` containing tokens and, when spaCy is available, a `doc` with POS/dependency info.
- Detectors return structured dictionaries so the core can both display messages and apply token-level suggestions to produce a corrected sentence.
- Suggestion types supported by `core._apply_suggestions`:
  - `replace`: replace token at `index` with `word`
  - `remove`: remove token at `index`
  - `insert`: insert `word` before `index`

## Limitations and next steps
- This project is intentionally small and heuristic-driven — it is not a replacement for a full grammar engine or large-language approach.
- Suggested improvements:
  - Use spaCy's `doc` to apply corrections at lemma/form level rather than token-level string manipulation.
  - Add conflict resolution when multiple suggestions overlap (currently suggestions are applied in ascending index order).
  - Add unit tests for each detector and a CI workflow (GitHub Actions) to prevent regressions.
  - Add an "conservative" mode (fewer suggestions) and an "aggressive" mode (apply more automated corrections).

## Contributing
- Open an issue or PR with test sentences that trigger unexpected behavior. Include the input sentence and expected correction.

---
If you want, I can now: (A) make suggestions conservative, (B) add unit tests and `pytest` support, or (C) add conflict-resolution for overlapping suggestions. Tell me which and I'll proceed.
