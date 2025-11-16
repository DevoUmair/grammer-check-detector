# article.py
from grammar_checker.knowledge import LinguisticKnowledge
import re
import spacy

class ArticleDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()
        # Load spaCy model for better proper noun detection
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            # Fallback if spaCy model is not available
            self.nlp = None

    def detect(self, sentence_or_context):
        """Detect article errors."""
        if isinstance(sentence_or_context, dict):
            doc = sentence_or_context.get('doc')
            tokens = sentence_or_context.get('tokens', [])
            if doc is None:
                return []
            return self._detect_with_context(doc, tokens)
        return []

    # ------------------------------------------------------------------

    def _detect_with_context(self, doc, tokens):
        """Detect article errors using context."""
        errors = []

        for i, token in enumerate(doc):
            # Detect wrong article usage (a/an/the)
            if token.text.lower() in ['a', 'an', 'the'] and i + 1 < len(doc):
                next_token = doc[i + 1]
                errors.extend(self._check_article_usage(token, next_token, i))

        # Missing articles before singular countable nouns
        errors.extend(self._detect_missing_articles(doc))

        # Extra articles before proper nouns and other zero-article cases
        errors.extend(self._detect_extra_articles(doc))

        return errors

    # ------------------------------------------------------------------

    def _check_article_usage(self, article_token, next_token, position):
        """Check article usage."""
        errors = []
        article_text = article_token.text.lower()
        word = next_token.text

        # Skip punctuation
        if next_token.pos_ == 'PUNCT':
            return errors

        # ---------------------------------------
        # A/AN RULES
        # ---------------------------------------
        if article_text in ['a', 'an']:
            requires_an = self._requires_an(word)

            if article_text == 'a' and requires_an:
                errors.append({
                    'pos': position,
                    'message': f"Use 'an' before '{word}' (vowel sound)",
                    'suggestion': {'type': 'replace', 'index': position, 'word': 'an'}
                })

            elif article_text == 'an' and not requires_an:
                errors.append({
                    'pos': position,
                    'message': f"Use 'a' before '{word}' (consonant sound)",
                    'suggestion': {'type': 'replace', 'index': position, 'word': 'a'}
                })

        # ---------------------------------------
        # THE RULES (zero-article situations)
        # ---------------------------------------
        if article_text == 'the':
            if self._should_be_zero_article(next_token):
                errors.append({
                    'pos': position,
                    'message': f"Unnecessary 'the' before '{word}'",
                    'suggestion': {'type': 'remove', 'index': position}
                })

        return errors

    # ------------------------------------------------------------------

    def _requires_an(self, word):
        """Improved detection of 'an' before vowel sounds."""
        w = word.lower()

        # Handle hyphenation: "hour-long", "X-ray"
        first = w.split('-')[0]

        # Silent H words from knowledge base
        if first in self.knowledge.SILENT_H_WORDS:
            return True

        # Words beginning with vowel letters but consonant sounds
        if first in self.knowledge.Y_SOUND_WORDS:
            return False

        # Acronyms pronounced by letter (FBI → "eff", MBA → "em")
        if word.isupper() and len(word) <= 5:
            if word[0] in self.knowledge.ACRONYM_VOWEL_SOUNDS:
                return True
            return False

        # Special cases: one, once
        if first in ['one', 'once']:
            return False

        # Standard vowel-sound rule
        return first[0] in "aeiou"

    # ------------------------------------------------------------------

    def _should_be_zero_article(self, noun_token):
        """Check if noun should normally have no article."""
        noun = noun_token.text.lower()

        # Enhanced proper noun detection
        if self._is_proper_noun(noun_token):
            return True

        # Check knowledge base for zero-article nouns
        if self.knowledge.should_have_zero_article(noun):
            return True

        # Check for institutional usage without article
        if self._is_institutional_usage(noun_token):
            return True

        return False

    def _is_proper_noun(self, token):
        """Robust proper noun detection using multiple methods."""
        # Method 1: Use spaCy POS tagging if available
        if self.nlp and len(token.text) > 1:
            doc = self.nlp(token.text)
            if doc[0].pos_ == "PROPN":
                return True

        # Method 2: Use existing spaCy doc POS tagging
        if token.pos_ == "PROPN":
            return True

        # Method 3: Capitalization rules (most reliable fallback)
        if (token.text[0].isupper() and 
            len(token.text) > 1 and 
            not token.text.isupper() and  # Exclude ALL CAPS
            token.text.lower() not in self.knowledge.ZERO_ARTICLE_NOUNS):
            
            # Common exceptions that look like proper nouns but aren't
            common_lowercase_proper_lookalikes = {
                'i', 'english', 'french', 'spanish', 'german', 'chinese', 
                'christmas', 'easter', 'halloween'
            }
            
            if token.text.lower() not in common_lowercase_proper_lookalikes:
                return True

        return False

    def _is_institutional_usage(self, token):
        """Check if noun is used in institutional sense without article."""
        noun = token.text.lower()
        
        institutional_nouns = {
            'school', 'college', 'university', 'church', 'hospital', 
            'prison', 'jail', 'court', 'work', 'home', 'bed'
        }
        
        if noun in institutional_nouns:
            # Check if it's being used in the institutional sense
            # e.g., "go to school" vs "go to the school"
            prev_token = token.i - 1 if token.i > 0 else None
            if prev_token and prev_token.text.lower() in ['to', 'at', 'in']:
                return True
        
        return False

    # ------------------------------------------------------------------

    def _detect_missing_articles(self, doc):
        """Detect missing articles before singular, countable nouns."""
        errors = []

        for i, token in enumerate(doc):
            # Only singular nouns
            if token.pos_ == "NOUN" and token.tag_ in ["NN", "NNP"]:
                
                # Skip if it's actually a proper noun
                if self._is_proper_noun(token):
                    continue

                word_lower = token.text.lower()

                # 1. Skip ZERO-ARTICLE nouns
                if self.knowledge.should_have_zero_article(word_lower):
                    continue

                # 2. Skip uncountables
                if self.knowledge.is_uncountable_noun(word_lower):
                    continue

                # 3. Skip proper nouns (additional check)
                if token.text[0].isupper() and not self._is_common_noun(token):
                    continue

                # 4. Check for existing determiners
                if self._has_determiner_before(doc, i):
                    continue

                # 5. Already has an article immediately before
                if i - 1 >= 0 and doc[i-1].text.lower() in ["a", "an", "the"]:
                    continue

                # 6. Check if it's part of a compound noun or fixed expression
                if self._is_part_of_compound(doc, i):
                    continue

                # 7. Find the start of the noun phrase (where to insert article)
                insert_pos, phrase_text = self._find_noun_phrase_start(doc, i)
                
                # 8. Skip if we're inserting before something that shouldn't have an article
                if insert_pos < len(doc) and self._should_be_zero_article(doc[insert_pos]):
                    continue
                
                # 9. Suggest correct article
                article = "an" if self._requires_an(doc[insert_pos].text) else "a"
                errors.append({
                    'pos': insert_pos,
                    'message': f"Missing article before '{phrase_text}'",
                    'suggestion': {'type': 'insert', 'index': insert_pos, 'word': article}
                })

        return errors

    def _detect_extra_articles(self, doc):
        """Detect unnecessary articles before proper nouns and other cases."""
        errors = []
        
        for i, token in enumerate(doc):
            if token.text.lower() in ['a', 'an', 'the'] and i + 1 < len(doc):
                next_token = doc[i + 1]
                
                # Check if article is before a proper noun
                if self._is_proper_noun(next_token) and not self._is_exception_case(next_token):
                    errors.append({
                        'pos': i,
                        'message': f"Unnecessary article before proper noun '{next_token.text}'",
                        'suggestion': {'type': 'remove', 'index': i}
                    })
                
                # Check for other zero-article cases
                elif self._should_be_zero_article(next_token):
                    errors.append({
                        'pos': i,
                        'message': f"Unnecessary article before '{next_token.text}'",
                        'suggestion': {'type': 'remove', 'index': i}
                    })
        
        return errors

    def _is_common_noun(self, token):
        """Check if a capitalized word is actually a common noun."""
        word_lower = token.text.lower()
        
        # Words that are often capitalized but are common nouns
        common_nouns_often_capitalized = {
            'president', 'doctor', 'professor', 'captain', 'minister',
            'company', 'corporation', 'association', 'organization'
        }
        
        if word_lower in common_nouns_often_capitalized:
            return True
            
        # Check if it's a title followed by a name
        if token.i + 1 < len(token.doc):
            next_token = token.doc[token.i + 1]
            if self._is_proper_noun(next_token):
                return True  # "President Biden" - "President" is common noun
        
        return False

    def _is_exception_case(self, token):
        """Check for exceptions where proper nouns DO take articles."""
        word_lower = token.text.lower()
        
        # Proper nouns that commonly take articles
        proper_nouns_with_articles = {
            # Rivers
            'nile', 'amazon', 'mississippi', 'thames',
            # Mountain ranges
            'alps', 'andes', 'himalayas', 'rockies',
            # Countries with "the"
            'united states', 'united kingdom', 'netherlands', 'philippines',
            # Oceans and seas
            'pacific', 'atlantic', 'indian', 'mediterranean',
        }
        
        if word_lower in proper_nouns_with_articles:
            return True
            
        # Check for plural proper nouns (often take "the")
        if token.text.endswith('s') and token.text[0].isupper():
            return True
            
        return False

    def _is_part_of_compound(self, doc, index):
        """Check if noun is part of a compound noun or fixed expression."""
        token = doc[index]
        
        # Check for compound nouns like "bus station", "school teacher"
        if index > 0:
            prev_token = doc[index - 1]
            if prev_token.pos_ in ["NOUN", "ADJ"]:
                return True
                
        # Check for fixed expressions
        fixed_expressions = {
            'bus stop', 'train station', 'school bus', 'car park',
            'phone number', 'email address', 'bank account'
        }
        
        if index > 0:
            bigram = f"{doc[index-1].text.lower()} {token.text.lower()}"
            if bigram in fixed_expressions:
                return True
        
        return False

    def _has_determiner_before(self, doc, noun_index):
        """Check if there's already a determiner before the noun."""
        i = noun_index - 1
        while i >= 0:
            token = doc[i]
            # Stop at punctuation or verbs
            if token.pos_ == "PUNCT" or token.pos_ in ["VERB", "AUX"]:
                return False
            
            # Check for determiners, possessives, quantifiers
            if (token.pos_ == "DET" or 
                token.text.lower() in ["my", "your", "his", "her", "its", "our", "their"] or
                token.text.lower() in ["this", "that", "these", "those", "some", "any", "each", "every", "no", "all"]):
                return True
                
            i -= 1
        
        return False

    def _find_noun_phrase_start(self, doc, noun_index):
        """Find where to insert article in noun phrase with adjectives."""
        start = noun_index
        i = noun_index - 1
        
        while i >= 0:
            token = doc[i]
            # Stop at punctuation, verbs, or determiners
            if token.pos_ in ["PUNCT", "VERB", "AUX", "DET", "ADP"]:
                break
            # Include adjectives and nouns in the noun phrase
            if token.pos_ in ["ADJ", "NOUN"]:
                start = i
            else:
                break
            i -= 1
        
        # Build the phrase text for the error message
        phrase_tokens = []
        for j in range(start, noun_index + 1):
            phrase_tokens.append(doc[j].text)
        phrase_text = " ".join(phrase_tokens)
        
        return start, phrase_text