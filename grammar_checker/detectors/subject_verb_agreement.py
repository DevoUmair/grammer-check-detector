# subject_verb_agreement.py
from grammar_checker.knowledge import LinguisticKnowledge
import lemminflect

class SubjectVerbAgreementDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, sentence_or_context):
        """Detect subject-verb agreement errors ONLY in present simple tense."""
        if isinstance(sentence_or_context, dict):
            doc = sentence_or_context.get('doc')
            tokens = sentence_or_context.get('tokens', [])
            if doc is None:
                return []
            return self._detect_present_simple_agreement(doc, tokens)
        return []

    def _detect_present_simple_agreement(self, doc, tokens):
        """Detect agreement errors ONLY in present simple tense."""
        errors = []
        
        # First, check if the sentence is in present simple tense
        if not self._is_present_simple_sentence(doc, tokens):
            return errors
        
        for token in doc:
            if (token.pos_ == "VERB" and 
                token.dep_ in ["ROOT", "conj", "ccomp"] and
                self._is_present_simple_verb(token)):
                
                subject = self._find_subject(token)
                
                if subject and not self._check_agreement(subject, token):
                    correct_form = self._get_correct_verb_form(token, subject)
                    if correct_form and correct_form != token.text:
                        errors.append({
                            'pos': token.i,
                            'message': f"Subject-verb agreement: '{subject.text}' requires '{correct_form}'",
                            'suggestion': {'type': 'replace', 'index': token.i, 'word': correct_form}
                        })
        
        return errors

    def _is_present_simple_sentence(self, doc, tokens):
        """Check if the sentence is in present simple tense."""
        sentence_text = ' '.join(tokens).lower()
        
        # Check for past/future markers that would exclude present simple
        past_markers = {'yesterday', 'ago', 'last', 'previous', 'earlier', 'before'}
        future_markers = {'tomorrow', 'next', 'soon', 'later', 'will', 'shall'}
        
        if any(marker in sentence_text for marker in past_markers):
            return False
        if any(marker in sentence_text for marker in future_markers):
            return False
        
        # Check for continuous/perfect aspects
        for token in doc:
            # If we find "be" + VBG (continuous) or "have" + VBN (perfect), not present simple
            if token.lemma_ == "be" and any(child.tag_ == "VBG" for child in token.children):
                return False
            if token.lemma_ == "have" and any(child.tag_ == "VBN" for child in token.children):
                return False
        
        return True

    def _is_present_simple_verb(self, verb_token):
        """Check if verb is in present simple tense."""
        # Skip if it's a modal verb
        modals = {'can', 'could', 'may', 'might', 'shall', 'should', 'will', 'would', 'must'}
        if verb_token.lemma_ in modals:
            return False
        
        # Skip if it's "be" or "have" as main verbs (they have special rules)
        if verb_token.lemma_ in ['be', 'have']:
            return False
        
        # Check if it's base form or third person singular
        verb_text = verb_token.text.lower()
        base_verb = verb_token.lemma_
        
        # It's present simple if it's base form or third person -s form
        if verb_text == base_verb:
            return True
            
        third_person_forms = lemminflect.getInflection(base_verb, 'VBZ')
        if third_person_forms and verb_text == third_person_forms[0].lower():
            return True
            
        return False

    def _find_subject(self, verb_token):
        """Find the subject of a verb."""
        for child in verb_token.children:
            if child.dep_ in ["nsubj", "nsubjpass"]:
                return child
        return None

    def _check_agreement(self, subject, verb):
        """Check if subject and verb agree in present simple."""
        if self._is_third_person_singular(subject):
            return self._is_third_person_singular_verb(verb)
        else:
            return not self._is_third_person_singular_verb(verb)

    def _is_third_person_singular(self, subject_token):
        """Check if subject is third person singular."""
        if subject_token.morph.get("Person") and subject_token.morph.get("Number"):
            return (str(subject_token.morph.get("Person")[0]) == "3" and 
                    str(subject_token.morph.get("Number")[0]) == "Sing")
        
        # Pronouns
        third_singular_pronouns = {"he", "she", "it"}
        third_plural_pronouns = {"they", "we", "you", "i"}
        
        subject_text = subject_token.text.lower()
        
        if subject_text in third_singular_pronouns:
            return True
        elif subject_text in third_plural_pronouns:
            return False
        
        # Special indefinite pronouns (always singular)
        indefinite_singular = self.knowledge.INDEFINITE_SINGULAR
        
        if subject_text in indefinite_singular:
            return True
        
        # Collective nouns (usually singular in American English)
        collective_nouns = self.knowledge.COLLECTIVE_NOUNS

        if subject_text in collective_nouns:
            return True
        
        # Academic subjects (singular)
        academic_singular = self.knowledge.ACADEMIC_SUBJECTS

        if subject_text in academic_singular:
            return True
        
        # Check for "each of", "every one of" patterns
        if self._is_each_of_pattern(subject_token):
            return True
        
        # Nouns - check if plural
        if subject_token.pos_ in ["NOUN", "PROPN"]:
            return not self._is_plural_noun(subject_token)
        
        return False

    def _is_each_of_pattern(self, subject_token):
        """Check for 'each of', 'every one of' patterns which are singular."""
        # Look for "each" or "every" before the subject
        if subject_token.i > 0:
            prev_token = subject_token.doc[subject_token.i - 1]
            if prev_token.text.lower() in ['each', 'every']:
                return True
        return False

    def _is_plural_noun(self, noun_token):
        """Check if noun is plural."""
        text_lower = noun_token.text.lower()
        
        # Common plural endings
        if (text_lower.endswith('s') and 
            not text_lower.endswith(('ss', 'us', 'is', 'as', 'os')) and
            text_lower not in {
                'news', 'mathematics', 'maths', 'physics', 'economics', 
                'politics', 'ethics', 'linguistics', 'statistics'
            }):
            return True
        
        # Irregular plurals
        irregular_plurals = {
            'children', 'men', 'women', 'people', 'feet', 'teeth', 
            'mice', 'geese', 'oxen', 'data', 'criteria'
        }
        if text_lower in irregular_plurals:
            return True
        
        return False

    def _is_third_person_singular_verb(self, verb_token):
        """Check if verb is third person singular form."""
        verb_text = verb_token.text.lower()
        base_verb = verb_token.lemma_
        
        # Check using lemminflect
        third_person_forms = lemminflect.getInflection(base_verb, 'VBZ')
        if third_person_forms and verb_text == third_person_forms[0].lower():
            return True
            
        return False

    def _get_correct_verb_form(self, verb_token, subject):
        """Get correct verb form for present simple."""
        base_verb = verb_token.lemma_
        
        if self._is_third_person_singular(subject):
            # Get third person singular form
            inflected = lemminflect.getInflection(base_verb, 'VBZ')
            return inflected[0] if inflected else base_verb + 's'
        else:
            # Return base form for plural subjects
            return base_verb