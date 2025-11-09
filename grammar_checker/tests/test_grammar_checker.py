import pytest
from grammar_checker import GrammarChecker

def test_basic_sentence():
    checker = GrammarChecker()
    text = "He go to school every day."
    result = checker.check(text)  # result is a list

    # Filter for subject-verb agreement errors
    sv_errors = [e for e in result if e.get('error_type') == 'sv_agreement']
    suggested_corrections = [e.get('suggested_correction') for e in sv_errors]

    assert "goes" in suggested_corrections

def test_article_insertion():
    checker = GrammarChecker()
    text = "I saw cat yesterday."
    result = checker.check(text)  # list of errors

    # Reconstruct corrected text manually for test
    corrected_text = text
    for e in result:
        if 'suggested_correction' in e and 'span' in e:
            start, end = e['span']
            corrected_text = corrected_text[:start] + e['suggested_correction'] + corrected_text[end:]

    assert "a cat" in corrected_text
