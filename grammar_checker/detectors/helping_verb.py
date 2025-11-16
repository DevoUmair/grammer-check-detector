from grammar_checker.knowledge import LinguisticKnowledge
import lemminflect

class HelpingVerbDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()

    def detect(self, sentence_or_context):
        """Detect helping verb errors."""
        if isinstance(sentence_or_context, dict):
            doc = sentence_or_context.get('doc')
            tokens = sentence_or_context.get('tokens', [])
            if doc is None:
                return self._detect_simple(tokens)
            return self._detect_with_context(doc, tokens)
        return []

    def _detect_with_context(self, doc, tokens):
        """Detect helping verb errors using context."""
        errors = []
        
        # Check for "could of" type errors
        sentence_text = ' '.join(tokens).lower()
        for wrong, correct in self.knowledge.HELPING_VERB_ERRORS.items():
            if wrong in sentence_text:
                # Find the exact position of the error
                start_idx = sentence_text.find(wrong)
                words_before = len(sentence_text[:start_idx].split())
                
                # Replace "of" with "have"
                of_position = words_before + 1  # Position of "of" in the wrong phrase
                if of_position < len(tokens) and tokens[of_position].lower() == 'of':
                    errors.append({
                        'pos': of_position,
                        'message': f"Use 'have' instead of 'of' after '{wrong.split()[0]}'",
                        'suggestion': {'type': 'replace', 'index': of_position, 'word': 'have'}
                    })
        
        # Check helping verb agreement for all auxiliary verbs
        for token in doc:
            if token.pos_ == "AUX" and token.lemma_ in ['be', 'have', 'do']:
                subject = self._find_subject(token)
                if subject:
                    correct_form = self._get_correct_helping_verb(token, subject)
                    if correct_form and correct_form.lower() != token.text.lower():
                        errors.append({
                            'pos': token.i,
                            'message': f"Helping verb agreement: '{subject.text}' requires '{correct_form}'",
                            'suggestion': {'type': 'replace', 'index': token.i, 'word': correct_form}
                        })
        
        # Check main verb "have" for agreement
        for token in doc:
            if (token.pos_ == "VERB" and token.lemma_ == 'have' and 
                token.dep_ in ["ROOT", "conj"]):
                subject = self._find_subject(token)
                if subject and not self._check_have_agreement(token, subject):
                    correct_form = self._get_correct_have_form(subject)
                    if correct_form and correct_form.lower() != token.text.lower():
                        errors.append({
                            'pos': token.i,
                            'message': f"Verb agreement: '{subject.text}' requires '{correct_form}'",
                            'suggestion': {'type': 'replace', 'index': token.i, 'word': correct_form}
                        })
        
        return errors

    def _find_subject(self, verb_token):
        """Find the subject of a verb."""
        # Look for subjects in children
        for child in verb_token.children:
            if child.dep_ in ["nsubj", "nsubjpass"]:
                return child
        
        # If no subject found in children, look for the head's subject
        if verb_token.head != verb_token:
            for child in verb_token.head.children:
                if child.dep_ in ["nsubj", "nsubjpass"]:
                    return child
        
        return None

    def _get_correct_helping_verb(self, aux_token, subject):
        """Get correct helping verb form with robust subject detection."""
        base_verb = aux_token.lemma_
        current_text = aux_token.text.lower()
        is_past = self._is_past_tense(aux_token)
        
        if base_verb == 'be':
            return self._get_correct_be_form(subject, is_past, current_text)
        
        elif base_verb == 'have':
            return self._get_correct_have_form(subject, current_text)
        
        elif base_verb == 'do':
            return self._get_correct_do_form(subject, is_past, current_text)
        
        return None

    def _get_correct_be_form(self, subject, is_past, current_form):
        """Get correct form of 'be' verb."""
        subject_text = subject.text.lower()
        
        if is_past:
            # Past tense forms
            if subject_text == 'i':
                return 'was' if current_form != 'was' else None
            elif self._is_third_person_singular(subject):
                return 'was' if current_form != 'was' else None
            else:
                return 'were' if current_form != 'were' else None
        else:
            # Present tense forms
            if subject_text == 'i':
                return 'am' if current_form != 'am' else None
            elif self._is_third_person_singular(subject):
                return 'is' if current_form != 'is' else None
            else:
                return 'are' if current_form != 'are' else None

    def _get_correct_have_form(self, subject, current_form=None):
        """Get correct form of 'have' verb."""
        if self._is_third_person_singular(subject):
            return 'has' if not current_form or current_form != 'has' else None
        else:
            return 'have' if not current_form or current_form != 'have' else None

    def _get_correct_do_form(self, subject, is_past, current_form):
        """Get correct form of 'do' verb."""
        if is_past:
            return 'did' if current_form != 'did' else None
        else:
            if self._is_third_person_singular(subject):
                return 'does' if current_form != 'does' else None
            else:
                return 'do' if current_form != 'do' else None

    def _check_have_agreement(self, have_token, subject):
        """Check if 'have' as main verb agrees with subject."""
        if self._is_third_person_singular(subject):
            return have_token.text.lower() == 'has'
        else:
            return have_token.text.lower() == 'have'

    def _is_third_person_singular(self, subject_token):
        """Robust check if subject is third person singular."""
        subject_text = subject_text = subject_token.text.lower()
        
        # Basic pronouns
        third_singular_pronouns = {"he", "she", "it"}
        if subject_text in third_singular_pronouns:
            return True
            
        # First/second person pronouns
        non_third_singular = {"i", "you", "we", "they"}
        if subject_text in non_third_singular:
            return False
        
        # Indefinite pronouns (singular)
        indefinite_singular = {
            'everyone', 'everybody', 'everything', 'someone', 'somebody', 
            'something', 'anyone', 'anybody', 'anything', 'no one', 'nobody',
            'nothing', 'each', 'either', 'neither'
        }
        if subject_text in indefinite_singular:
            return True
        
        # Collective nouns (usually singular)
        collective_nouns = {
            'team', 'group', 'family', 'class', 'committee', 'jury', 'staff',
            'government', 'company', 'organization', 'audience', 'band'
        }
        if subject_text in collective_nouns:
            return True
        
        # Academic subjects (singular)
        academic_singular = {
            'mathematics', 'math', 'physics', 'economics', 'news', 'politics'
        }
        if subject_text in academic_singular:
            return True
        
        # Check noun plurality
        if subject_token.pos_ in ["NOUN", "PROPN"]:
            return not self._is_plural_noun(subject_token)
        
        # Default to singular for unknown cases
        return True

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
            'mice', 'geese', 'oxen'
        }
        if text_lower in irregular_plurals:
            return True
        
        return False

    def _is_past_tense(self, verb_token):
        """Check if verb is past tense."""
        if verb_token.morph.get("Tense"):
            return str(verb_token.morph.get("Tense")[0]) == "Past"
        
        past_forms = {'was', 'were', 'had', 'did', 'been'}
        return verb_token.text.lower() in past_forms

    def _detect_simple(self, tokens):
        """Simple helping verb detection for 'could of' type errors."""
        errors = []
        sentence_text = ' '.join(tokens).lower()
        
        for wrong, correct in self.knowledge.HELPING_VERB_ERRORS.items():
            if wrong in sentence_text:
                # Find the position of "of" in the phrase
                words = sentence_text.split()
                for i, word in enumerate(words):
                    if word == 'of' and i > 0 and words[i-1] in ['could', 'would', 'should', 'might', 'must']:
                        # Find the actual position in original tokens
                        of_count = 0
                        for j, token in enumerate(tokens):
                            if token.lower() == 'of':
                                of_count += 1
                                if of_count == (words[:i+1].count('of')):
                                    errors.append({
                                        'pos': j,
                                        'message': f"Use 'have' instead of 'of' after '{words[i-1]}'",
                                        'suggestion': {'type': 'replace', 'index': j, 'word': 'have'}
                                    })
                                    break
                        break
        
        return errors