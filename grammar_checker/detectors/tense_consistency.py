# tense_consistency.py
from grammar_checker.knowledge import LinguisticKnowledge
import lemminflect
import spacy

class TenseConsistencyDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()
        # Load a small spaCy model for tokenization and POS tagging
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            # Fallback if model not available
            self.nlp = None

    def detect(self, sentence_or_context):
        """Comprehensive tense consistency detection with improved logic."""
        if isinstance(sentence_or_context, dict):
            doc = sentence_or_context.get('doc')
            tokens = sentence_or_context.get('tokens', [])
            if doc is None:
                return []
            return self._analyze_tense_consistency(doc, tokens)
        return []

    def _analyze_tense_consistency(self, doc, tokens):
        """Analyze tense consistency and return detected tense errors."""
        if not tokens:
            return []
        
        # Convert string tokens to proper spaCy tokens if needed
        if tokens and isinstance(tokens[0], str):
            # Re-parse the sentence to get proper tokens
            sentence_text = doc.text if hasattr(doc, 'text') else ' '.join(tokens)
            if self.nlp:
                doc = self.nlp(sentence_text)
                tokens = list(doc)
            else:
                # Fallback: create simple token-like objects
                tokens = self._create_simple_tokens(tokens)
        
        detected_tense = self._detect_sentence_tense(doc, tokens)
        
        # Detect tense errors and SVA errors
        tense_errors = self._detect_tense_errors(doc, detected_tense, tokens)
        sva_errors = self._detect_sva_errors(doc, detected_tense)
        
        # Always return the detected tense as information
        tense_info = {
            'type': 'tense_info',
            'message': f'Detected tense: {detected_tense}',
            'suggestion': None,
            'tense': detected_tense
        }
        
        return [tense_info] + tense_errors + sva_errors

    def _create_simple_tokens(self, token_strings):
        """Create simple token-like objects from strings."""
        class SimpleToken:
            def __init__(self, text, index=0):
                self.text = text
                self.lower_ = text.lower()
                self.pos_ = self._guess_pos(text)
                self.lemma_ = text.lower()  # Simple lemma
                self.idx = index
                self.i = index
                
            def _guess_pos(self, text):
                """Simple POS guessing based on common patterns."""
                text_lower = text.lower()
                
                # Common auxiliaries
                if text_lower in ['is', 'am', 'are', 'was', 'were', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'shall', 'would', 'could', 'should', 'may', 'might', 'must']:
                    return 'AUX'
                
                # Common verbs
                if text_lower in ['go', 'come', 'see', 'look', 'make', 'take', 'give', 'get', 'say', 'know', 'think', 'feel', 'want', 'need', 'like', 'love', 'hate', 'work', 'play', 'read', 'write', 'run', 'walk', 'talk', 'speak', 'listen', 'eat', 'drink', 'sleep', 'live', 'study', 'learn']:
                    return 'VERB'
                
                # Common nouns
                if text_lower in ['i', 'you', 'he', 'she', 'it', 'we', 'they', 'this', 'that', 'these', 'those']:
                    return 'PRON'
                
                # Default to NOUN for unknown words
                return 'NOUN'
        
        return [SimpleToken(token, i) for i, token in enumerate(token_strings)]

    def _detect_sentence_tense(self, doc, tokens):
        """Detect the tense of the sentence with robust logic."""
        sentence_text = doc.text if hasattr(doc, 'text') else ' '.join([t.text for t in tokens])
        
        # Check for tense conflicts first (e.g., future tense with past time marker)
        if self._has_tense_conflict(sentence_text):
            return self._resolve_tense_conflict(sentence_text)
        
        # Step 1: Check from tense markers first (most reliable)
        tense_from_markers = self._get_tense_from_time_markers_comprehensive(sentence_text)
        if tense_from_markers:
            return tense_from_markers
        
        # Step 2: Check for auxiliary verbs
        tense_from_aux = self._get_tense_from_auxiliaries_comprehensive(tokens)
        if tense_from_aux:
            return tense_from_aux
        
        # Step 3: Check main verbs
        tense_from_verbs = self._get_tense_from_verb_patterns_comprehensive(tokens)
        if tense_from_verbs:
            return tense_from_verbs
        
        return "simple_present"

    def _has_tense_conflict(self, sentence_text):
        """Check if there's a conflict between tense markers and verb forms."""
        sentence_lower = sentence_text.lower()
        
        # Future auxiliary with past time marker
        if ('will' in sentence_lower or "'ll" in sentence_lower) and any(marker in sentence_lower for marker in self.knowledge.PAST_TENSE_MARKERS):
            return True
        
        # Past auxiliary with future time marker  
        if any(aux in sentence_lower for aux in ['was', 'were', 'had']) and any(marker in sentence_lower for marker in self.knowledge.FUTURE_TENSE_MARKERS):
            return True
        
        return False

    def _resolve_tense_conflict(self, sentence_text):
        """Resolve tense conflicts - time markers usually win over verb forms."""
        sentence_lower = sentence_text.lower()
        
        # If there are past time markers, use past tense
        if any(marker in sentence_lower for marker in self.knowledge.PAST_TENSE_MARKERS):
            return "simple_past"
        
        # If there are future time markers, use future tense
        if any(marker in sentence_lower for marker in self.knowledge.FUTURE_TENSE_MARKERS):
            return "simple_future"
        
        return "simple_present"

    def _get_tense_from_time_markers_comprehensive(self, sentence_text):
        """Get tense from comprehensive time markers in knowledge base."""
        sentence_lower = sentence_text.lower()
        
        # Check past markers
        if any(marker in sentence_lower for marker in self.knowledge.PAST_TENSE_MARKERS):
            return "simple_past"
        
        # Check future markers  
        if any(marker in sentence_lower for marker in self.knowledge.FUTURE_TENSE_MARKERS):
            return "simple_future"
        
        # Check present markers
        if any(marker in sentence_lower for marker in self.knowledge.PRESENT_TENSE_MARKERS):
            return "simple_present"
        
        return None

    def _get_tense_from_auxiliaries_comprehensive(self, tokens):
        """Comprehensive auxiliary verb tense detection."""
        auxiliaries = [token for token in tokens if hasattr(token, 'pos_') and token.pos_ == 'AUX']
        
        # Check for future tense (will/shall)
        if any(token.text.lower() in ['will', 'shall', "'ll"] for token in auxiliaries):
            return "simple_future"
        
        # Check for perfect tenses (have/has/had)
        have_auxiliaries = [token for token in auxiliaries if token.text.lower() in ['has', 'have', 'had']]
        for aux in have_auxiliaries:
            aux_text = aux.text.lower()
            # Look for past participle in nearby tokens
            for token in tokens:
                if (hasattr(token, 'pos_') and token.pos_ == 'VERB' and 
                    self._is_past_participle_form(token.text.lower(), token)):
                    if aux_text in ['has', 'have']:
                        return "present_perfect"
                    elif aux_text == 'had':
                        return "past_perfect"
        
        # Check for continuous tenses (be + VBG)
        be_auxiliaries = [token for token in auxiliaries if token.text.lower() in ['am', 'is', 'are', 'was', 'were']]
        for aux in be_auxiliaries:
            aux_text = aux.text.lower()
            # Look for -ing form in nearby tokens
            for token in tokens:
                if (hasattr(token, 'pos_') and token.pos_ == 'VERB' and 
                    token.text.lower().endswith('ing')):
                    if aux_text in ['am', 'is', 'are']:
                        return "present_continuous"
                    elif aux_text in ['was', 'were']:
                        return "past_continuous"
        
        # Simple auxiliary detection
        for token in auxiliaries:
            aux_text = token.text.lower()
            if aux_text in ['was', 'were', 'had', 'did']:
                return "simple_past"
            elif aux_text in ['am', 'is', 'are', 'has', 'have', 'do', 'does']:
                return "simple_present"
        
        return None

    def _get_tense_from_verb_patterns_comprehensive(self, tokens):
        """Infer tense from main verb forms with comprehensive analysis."""
        main_verbs = [token for token in tokens if self._is_main_verb(token)]
        if not main_verbs:
            return "simple_present"
        
        # Count verb forms
        past_forms = sum(1 for verb in main_verbs if self._is_past_form(verb))
        third_person_forms = sum(1 for verb in main_verbs if self._is_third_person_singular_verb(verb))
        
        # Decision logic
        if past_forms > 0:
            return "simple_past"
        elif third_person_forms > 0:
            return "simple_present"
        else:
            return "simple_present"

    # ==================== TENSE ERROR DETECTION ====================

    def _detect_tense_errors(self, doc, sentence_tense, tokens):
        """Detect and correct tense inconsistencies with conditional handling."""
        errors = []
        
        # print(f"DEBUG: Starting tense error detection for: {doc.text}")
        # print(f"DEBUG: Detected sentence tense: {sentence_tense}")
        
        # First check if this is a conditional sentence
        if self._is_conditional_sentence(doc):
            # print("DEBUG: This is a conditional sentence")
            return self._detect_conditional_errors(doc, tokens)
        
        # Detect auxiliary verb errors (like "will" with past time markers)
        aux_errors = self._detect_auxiliary_tense_errors(doc, sentence_tense)
        # print(f"DEBUG: Found {len(aux_errors)} auxiliary errors")
        errors.extend(aux_errors)
        
        # If we have auxiliary errors that will change the sentence structure,
        # we need to re-check the main verbs after those changes
        has_auxiliary_changes = any(error['suggestion']['type'] == 'remove' for error in aux_errors)
        
        for token in doc:
            # print(f"DEBUG: Processing token: '{token.text}' (POS: {token.pos_})")
            
            if self._is_main_verb(token):
                # print(f"DEBUG: '{token.text}' is a main verb")
                
                # Skip verbs in correct auxiliary constructions
                if self._is_in_auxiliary_construction(token, doc):
                    # print(f"DEBUG: Skipping '{token.text}' - in auxiliary construction")
                    continue
                    
                # Skip verbs following modals (should stay in base form)
                # BUT if we're removing the modal, don't skip this verb
                follows_modal_to_remove = False
                if self._follows_modal(token, doc):
                    # Check if the modal is going to be removed
                    modal_token = doc[token.i - 1]
                    modal_will_be_removed = any(
                        error['suggestion']['type'] == 'remove' and error['suggestion']['index'] == modal_token.i
                        for error in aux_errors
                    )
                    if modal_will_be_removed:
                        # print(f"DEBUG: '{token.text}' follows modal '{modal_token.text}' that will be removed - NOT skipping")
                        follows_modal_to_remove = True
                    else:
                        # print(f"DEBUG: Skipping '{token.text}' - follows modal")
                        continue
                
                # Skip verbs following "to" (should stay in base form for infinitives)
                if self._follows_to(token, doc):
                    # print(f"DEBUG: Skipping '{token.text}' - follows 'to'")
                    continue
                    
                # Check if verb is in a time clause that should have different tense rules
                if self._is_in_time_clause(token, doc):
                    expected_form = self._get_time_clause_verb_form(token, sentence_tense, doc)
                    # print(f"DEBUG: '{token.text}' is in time clause, expected: {expected_form}")
                else:
                    expected_form = self._get_expected_main_verb_form(token, sentence_tense, doc, tokens)
                    # print(f"DEBUG: '{token.text}' regular case, expected: {expected_form}")
                
                if expected_form and expected_form.lower() != token.text.lower():
                    errors.append({
                        'type': 'tense_error',
                        'message': f"Tense error: should be '{expected_form}'",
                        'suggestion': {'type': 'replace', 'index': token.i, 'word': expected_form},
                        'position': token.idx
                    })
                    # print(f"DEBUG: Added tense error for '{token.text}' -> '{expected_form}'")
        
        # print(f"DEBUG: Total errors found: {len(errors)}")
        return errors

    def _detect_auxiliary_tense_errors(self, doc, sentence_tense):
        """Detect auxiliary verb errors that conflict with the detected tense."""
        errors = []
        
        # print(f"DEBUG: Checking auxiliary errors for tense: {sentence_tense}")
        
        for token in doc:
            if token.pos_ == 'AUX':
                # print(f"DEBUG: Checking auxiliary: '{token.text}'")
                
                # Check for future auxiliary in past context
                if token.text.lower() in ['will', 'shall', "'ll"] and sentence_tense == 'simple_past':
                    # print(f"DEBUG: Found future auxiliary '{token.text}' in past context")
                    if not self._is_auxiliary_in_correct_construction(token, doc, sentence_tense):
                        errors.append({
                            'type': 'auxiliary_error',
                            'message': f"Remove future auxiliary '{token.text}' for past tense",
                            'suggestion': {'type': 'remove', 'index': token.i, 'word': ''},
                            'position': token.idx
                        })
                        # print(f"DEBUG: Added auxiliary error - remove '{token.text}'")
                
                # Check for past auxiliary in future context  
                elif token.text.lower() in ['was', 'were', 'had'] and sentence_tense == 'simple_future':
                    # print(f"DEBUG: Found past auxiliary '{token.text}' in future context")
                    errors.append({
                        'type': 'auxiliary_error', 
                        'message': f"Remove past auxiliary '{token.text}' for future tense",
                        'suggestion': {'type': 'remove', 'index': token.i, 'word': ''},
                        'position': token.idx
                    })
                
                # Check for present auxiliary in past context when not needed
                elif token.text.lower() in ['am', 'is', 'are', 'has', 'have', 'do', 'does'] and sentence_tense == 'simple_past':
                    # print(f"DEBUG: Found present auxiliary '{token.text}' in past context")
                    # Only flag if this auxiliary is creating a tense conflict
                    if not self._is_auxiliary_in_correct_construction(token, doc):
                        errors.append({
                            'type': 'auxiliary_error',
                            'message': f"Remove present auxiliary '{token.text}' for past tense",
                            'suggestion': {'type': 'remove', 'index': token.i, 'word': ''},
                            'position': token.idx
                        })
        
        return errors

    def _is_auxiliary_in_correct_construction(self, token, doc, sentence_tense):
        """Check if auxiliary is part of a correct construction that should be preserved."""
        # print(f"DEBUG: Checking if '{token.text}' is in correct construction for tense: {sentence_tense}")
        
        # If we're in past tense due to conflict, future auxiliaries are NOT correct
        if token.text.lower() in ['will', 'shall', "'ll"] and sentence_tense == 'simple_past':
            # print(f"DEBUG: '{token.text}' is future auxiliary in past tense context - NOT correct")
            return False
        
        # If "will" is followed by base form verb, it's correct ONLY for future tense
        if token.text.lower() in ['will', 'shall', "'ll"] and sentence_tense == 'simple_future':
            for i in range(token.i + 1, min(token.i + 3, len(doc))):
                if hasattr(doc[i], 'pos_') and doc[i].pos_ == 'VERB':
                    # print(f"DEBUG: '{token.text}' followed by verb '{doc[i].text}' - correct for future")
                    return True
        
        # If "have/has" is followed by past participle, it's correct for perfect
        if token.text.lower() in ['has', 'have']:
            for i in range(token.i + 1, min(token.i + 3, len(doc))):
                if (hasattr(doc[i], 'pos_') and doc[i].pos_ == 'VERB' and 
                    self._is_past_participle_form(doc[i].text.lower(), doc[i])):
                    # print(f"DEBUG: '{token.text}' followed by past participle '{doc[i].text}' - correct for perfect")
                    return True
        
        # If "be" is followed by -ing form, it's correct for continuous
        if token.text.lower() in ['am', 'is', 'are', 'was', 'were']:
            for i in range(token.i + 1, min(token.i + 3, len(doc))):
                if (hasattr(doc[i], 'pos_') and doc[i].pos_ == 'VERB' and 
                    doc[i].text.lower().endswith('ing')):
                    # print(f"DEBUG: '{token.text}' followed by -ing form '{doc[i].text}' - correct for continuous")
                    return True
        
        # print(f"DEBUG: '{token.text}' is NOT in correct construction - should be flagged")
        return False

    def _is_conditional_sentence(self, doc):
        """Check if this is a conditional sentence."""
        conditional_markers = {'if', 'unless', 'provided', 'assuming', 'supposing'}
        
        # Look for conditional markers in the sentence
        for token in doc:
            if token.text.lower() in conditional_markers:
                return True
        
        return False

    def _detect_conditional_errors(self, doc, tokens):
        """Detect and correct errors in conditional sentences."""
        errors = []
        
        # Identify the type of conditional
        conditional_type = self._identify_conditional_type(doc)
        
        for token in doc:
            if self._is_main_verb(token):
                # Skip verbs in correct auxiliary constructions
                if self._is_in_auxiliary_construction(token, doc):
                    continue
                    
                # Skip verbs following modals (should stay in base form)
                if self._follows_modal(token, doc):
                    continue
                
                # Skip verbs following "to" (should stay in base form for infinitives)
                if self._follows_to(token, doc):
                    continue
                
                # Get correct form based on conditional type and clause position
                expected_form = self._get_conditional_verb_form_improved(token, conditional_type, doc)
                
                if expected_form and expected_form.lower() != token.text.lower():
                    errors.append({
                        'type': 'tense_error',
                        'message': f"Conditional tense error: should be '{expected_form}'",
                        'suggestion': {'type': 'replace', 'index': token.i, 'word': expected_form},
                        'position': token.idx
                    })
        
        return errors

    def _identify_conditional_type(self, doc):
        """Identify the type of conditional sentence."""
        sentence_text = doc.text.lower()
        
        # Check for Type 3: Past perfect + would have
        if any(marker in sentence_text for marker in ['would have', 'could have', 'might have']):
            return "type3"
        
        # Check for Type 2: Past tense + would
        if any(marker in sentence_text for marker in ['would', 'could', 'might']) and any(verb in sentence_text for verb in ['was', 'were', 'had']):
            return "type2"
        
        # Check for Type 1: Present + will
        if 'will' in sentence_text or "'ll" in sentence_text:
            return "type1"
        
        # Default to Type 0: General truth
        return "type0"

    def _get_conditional_verb_form_improved(self, token, conditional_type, doc):
        """Get correct verb form for conditional clauses with improved logic."""
        base_verb = token.lemma_
        
        # Check if this verb is in the if-clause or main clause
        is_in_if_clause = self._is_in_if_clause(token, doc)
        
        if conditional_type == "type0":  # General truths
            # If + present, present
            return self._get_present_form(base_verb, token.i, doc)
        
        elif conditional_type == "type1":  # Real future
            if is_in_if_clause:
                # If + present
                return self._get_present_form(base_verb, token.i, doc)
            else:
                # Will + base form
                return base_verb
        
        elif conditional_type == "type2":  # Unreal present/future
            if is_in_if_clause:
                # If + past
                return self._get_past_form(base_verb)
            else:
                # Would + base form
                return base_verb
        
        elif conditional_type == "type3":  # Unreal past
            if is_in_if_clause:
                # If + past perfect
                return self._get_past_participle_form(base_verb)
            else:
                # Would have + past participle
                return self._get_past_participle_form(base_verb)
        
        return base_verb

    def _is_in_if_clause(self, token, doc):
        """Check if verb is in the if-clause of a conditional."""
        # Find the "if" token
        if_token = None
        for t in doc:
            if t.text.lower() == 'if':
                if_token = t
                break
        
        if not if_token:
            return False
        
        # Check if there's a comma separating clauses
        comma_token = None
        for t in doc:
            if t.text == ',':
                comma_token = t
                break
        
        if comma_token:
            # If there's a comma, check if token is before the comma (if-clause)
            return token.i < comma_token.i
        else:
            # If no comma, use heuristics - usually first clause is if-clause
            return token.i < len(doc) / 2

    def _follows_to(self, verb_token, doc):
        """Check if verb follows 'to' (infinitive construction)."""
        return (verb_token.i > 0 and 
                hasattr(doc[verb_token.i - 1], 'text') and 
                doc[verb_token.i - 1].text.lower() == 'to')

    def _get_time_clause_verb_form(self, token, main_tense, doc):
        """Get correct verb form for time clauses based on main clause tense."""
        base_verb = token.lemma_
        
        # Special case: "when" clauses with simple present for general truths/habits
        if self._is_when_clause_with_present_meaning(token, doc, main_tense):
            return self._get_present_form(base_verb, token.i, doc)
        
        # Standard time clause rules:
        # - If main clause is past, time clause uses appropriate past form
        # - If main clause is present/future, time clause uses present form
        
        if main_tense in ['simple_past', 'past_continuous', 'past_perfect']:
            # Use simple past for time clauses in past context (not continuous)
            return self._get_past_form(base_verb)
        
        elif main_tense in ['simple_present', 'present_continuous', 'present_perfect', 'simple_future']:
            return self._get_present_form(base_verb, token.i, doc)
        
        else:
            return base_verb

    def _get_expected_main_verb_form(self, verb_token, sentence_tense, doc, tokens):
        """Get correct main verb form with improved tense handling."""
        base_verb = verb_token.lemma_
        
        # Standard tense mapping
        tense_form_map = {
            'simple_present': lambda: self._get_present_form(base_verb, verb_token.i, tokens),
            'simple_past': lambda: self._get_past_form(base_verb),
            'simple_future': lambda: base_verb,
            'present_continuous': lambda: self._get_ing_form(base_verb),
            'past_continuous': lambda: self._get_ing_form(base_verb),
            'present_perfect': lambda: self._get_past_participle_form(base_verb),
            'past_perfect': lambda: self._get_past_participle_form(base_verb),
        }
        
        result = tense_form_map.get(sentence_tense, lambda: base_verb)()
        return result

    # ==================== CONDITIONAL SENTENCE HANDLING ====================

    def _is_in_time_clause(self, token, doc):
        """Check if verb is in a time clause (when, while, as, before, after, until, etc.)."""
        time_conjunctions = {'when', 'while', 'as', 'before', 'after', 'until', 'since', 'once'}
        
        # Look for time conjunctions before this verb
        for i in range(token.i):
            prev_token = doc[i]
            if prev_token.text.lower() in time_conjunctions:
                return True
        
        return False

    def _is_when_clause_with_present_meaning(self, token, doc, main_tense):
        """Check if 'when' clause should use present tense for general truths."""
        # Look for "when" conjunction
        has_when = False
        for i in range(token.i):
            if doc[i].text.lower() == 'when':
                has_when = True
                break
        
        if not has_when:
            return False
        
        # If main clause is past but describes a general truth/habit, use present
        if main_tense in ['simple_past', 'past_continuous']:
            # Heuristic: check if this describes a repeated action or general truth
            sentence_text = doc.text.lower()
            general_truth_indicators = {'always', 'usually', 'often', 'sometimes', 'never', 'every', 'each'}
            if any(indicator in sentence_text for indicator in general_truth_indicators):
                return True
        
        return False

    def _is_continuous_context(self, token, doc):
        """Check if verb should be in continuous form based on context."""
        # Check if there's a "be" auxiliary nearby that suggests continuous
        for i in range(max(0, token.i - 3), token.i):
            if (hasattr(doc[i], 'pos_') and doc[i].pos_ == 'AUX' and 
                doc[i].lemma_ == 'be' and doc[i].text.lower() in ['was', 'were', 'is', 'are']):
                return True
        
        # Check if the action is ongoing (heuristic)
        ongoing_indicators = {'while', 'as', 'when'}
        for i in range(max(0, token.i - 3), token.i):
            if doc[i].text.lower() in ongoing_indicators:
                return True
        
        return False

    def _follows_modal(self, verb_token, doc):
        """Check if verb follows a modal verb."""
        return (verb_token.i > 0 and 
                hasattr(doc[verb_token.i - 1], 'tag_') and 
                doc[verb_token.i - 1].tag_ == 'MD' and 
                doc[verb_token.i - 1].pos_ == 'AUX')

    def _is_in_auxiliary_construction(self, verb_token, doc):
        """Check if verb is part of an auxiliary construction that should be preserved."""
        # Check if this verb is part of continuous aspect (be + VBG)
        if hasattr(verb_token, 'tag_') and verb_token.tag_ == 'VBG':
            if hasattr(verb_token, 'children'):
                for child in verb_token.children:
                    if hasattr(child, 'lemma_') and child.lemma_ == 'be' and child.pos_ == 'AUX':
                        return True
        
        # Check if this verb is part of perfect aspect (have + VBN)
        if hasattr(verb_token, 'tag_') and verb_token.tag_ == 'VBN':
            if hasattr(verb_token, 'children'):
                for child in verb_token.children:
                    if hasattr(child, 'lemma_') and child.lemma_ == 'have' and child.pos_ == 'AUX':
                        return True
        
        return False

    # ==================== SVA DETECTION ====================

    def _detect_sva_errors(self, doc, sentence_tense):
        """Detect subject-verb agreement errors - only for present simple."""
        errors = []
        
        # Only check SVA in present simple tense
        if sentence_tense != 'simple_present':
            return errors
            
        for token in doc:
            if self._is_main_verb(token) and not self._is_modal_or_be(token):
                subject = self._find_subject(token)
                if subject and not self._check_sva_agreement(subject, token):
                    correct_form = self._get_correct_sva_form(token, subject)
                    if correct_form and correct_form.lower() != token.text.lower():
                        errors.append({
                            'type': 'sva_error',
                            'message': f"Subject-verb agreement: '{subject.text}' requires '{correct_form}'",
                            'suggestion': {'type': 'replace', 'index': token.i, 'word': correct_form},
                            'position': token.idx
                        })
        
        return errors

    def _is_main_verb(self, token):
        """Check if token is a main content verb."""
        if not hasattr(token, 'pos_'):
            return False
        
        is_verb = token.pos_ == "VERB"
        is_likely_noun = self._is_likely_noun(token)
        
        return is_verb and not is_likely_noun

    def _is_likely_noun(self, token):
        """Check if verb-tagged word is likely a noun using context clues."""
        if not hasattr(token, 'pos_') or token.pos_ != 'VERB':
            return False
        
        # Use token.doc to access the document
        doc = token.doc
        
        # Check if preceded by articles/determiners (strong noun indicator)
        if hasattr(token, 'i') and token.i > 0:
            prev_token = doc[token.i - 1] if token.i < len(doc) else None
            if prev_token and hasattr(prev_token, 'pos_'):
                if prev_token.pos_ in ['DET', 'ADJ']:  # the, a, an, this, that, etc.
                    return True
                if prev_token.text.lower() in ['to']:  # "to work" - usually verb
                    return False
        
        # Check if followed by objects/prepositions (verb indicator)
        if hasattr(token, 'i') and token.i < len(doc) - 1:
            next_token = doc[token.i + 1] if token.i + 1 < len(doc) else None
            if next_token and hasattr(next_token, 'pos_'):
                if next_token.pos_ in ['ADP']:  # prepositions often follow verbs
                    return False
                if next_token.pos_ in ['ADV']:  # adverbs often follow verbs
                    return False
                if next_token.pos_ in ['DET', 'ADJ']:  # determiners/adjectives often precede nouns
                    return True
        
        # Check dependency relations
        if hasattr(token, 'dep_'):
            # If it's the subject of a sentence, it's likely a noun
            if token.dep_ in ['nsubj', 'nsubjpass']:
                return True
            # If it's the root and has a subject, it's likely a verb
            if token.dep_ == 'ROOT':
                for child in token.children:
                    if hasattr(child, 'dep_') and child.dep_ in ['nsubj', 'nsubjpass']:
                        return False
        
        # Words that are almost always nouns in common usage
        always_nouns = {'news', 'mathematics', 'physics', 'economics', 'politics'}
        if hasattr(token, 'lemma_') and token.lemma_ in always_nouns:
            return True
        
        # Words that can be both but are usually verbs in most contexts
        usually_verbs = {'work', 'play', 'run', 'walk', 'talk', 'sleep', 'rain'}
        if hasattr(token, 'lemma_') and token.lemma_ in usually_verbs:
            return False
        
        # Default: trust the POS tagger
        return False

    def _is_modal_or_be(self, verb_token):
        """Check if verb is modal or form of 'be'."""
        if not hasattr(verb_token, 'lemma_'):
            return False
        modals = {'can', 'could', 'may', 'might', 'shall', 'should', 'will', 'would', 'must'}
        return verb_token.lemma_ in modals or verb_token.lemma_ == 'be'

    def _find_subject(self, verb_token):
        """Find the subject of a verb."""
        if hasattr(verb_token, 'children'):
            for child in verb_token.children:
                if hasattr(child, 'dep_') and child.dep_ in ["nsubj", "nsubjpass"]:
                    return child
        if hasattr(verb_token, 'head') and verb_token.head != verb_token:
            if hasattr(verb_token.head, 'children'):
                for child in verb_token.head.children:
                    if hasattr(child, 'dep_') and child.dep_ in ["nsubj", "nsubjpass"]:
                        return child
        return None

    def _is_third_person_singular(self, subject_token):
        """Check if subject is third person singular."""
        if not hasattr(subject_token, 'text'):
            return False
            
        subject_text = subject_token.text.lower()
        
        if subject_text in {'he', 'she', 'it'}:
            return True
        if subject_text in {'i', 'you', 'we', 'they'}:
            return False
        
        # Indefinite pronouns
        indefinite_singular = {'everyone', 'everybody', 'everything', 'someone', 'somebody', 
                              'something', 'anyone', 'anybody', 'anything', 'no one', 'nobody',
                              'nothing', 'each', 'either', 'neither'}
        if subject_text in indefinite_singular:
            return True
        
        # Collective nouns and academic subjects
        singular_nouns = {'team', 'group', 'family', 'mathematics', 'physics', 'economics'}
        if subject_text in singular_nouns:
            return True
        
        # Default for other nouns
        return not self._is_plural_noun(subject_token)

    def _is_plural_noun(self, noun_token):
        """Check if noun is plural."""
        if not hasattr(noun_token, 'text'):
            return False
            
        text_lower = noun_token.text.lower()
        if (text_lower.endswith('s') and not text_lower.endswith(('ss', 'us', 'is', 'as', 'os'))):
            return True
        irregular_plurals = {'children', 'men', 'women', 'people', 'feet', 'teeth', 'mice'}
        return text_lower in irregular_plurals

    def _is_third_person_singular_verb(self, verb_token):
        """Check if verb is third person singular form."""
        if not hasattr(verb_token, 'text') or not hasattr(verb_token, 'lemma_'):
            return False
            
        verb_text = verb_token.text.lower()
        base_verb = verb_token.lemma_
        forms = lemminflect.getInflection(base_verb, 'VBZ')
        return forms and verb_text == forms[0].lower()

    def _check_sva_agreement(self, subject, verb):
        """Check subject-verb agreement."""
        if self._is_third_person_singular(subject):
            return self._is_third_person_singular_verb(verb)
        else:
            return not self._is_third_person_singular_verb(verb)

    def _get_correct_sva_form(self, verb_token, subject):
        """Get correct SVA form."""
        if not hasattr(verb_token, 'lemma_'):
            return None
            
        base_verb = verb_token.lemma_
        
        if self._is_third_person_singular(subject):
            forms = lemminflect.getInflection(base_verb, 'VBZ')
            return forms[0] if forms else base_verb + 's'
        else:
            return base_verb

    def _is_past_form(self, verb_token):
        """Check if verb is in past tense form."""
        if not hasattr(verb_token, 'text'):
            return False
            
        verb_text = verb_token.text.lower()
        
        # Check irregular past
        if self.knowledge.is_irregular_past_verb(verb_text):
            return True
        
        # Check regular past (-ed)
        if len(verb_text) > 2 and verb_text.endswith(('ed', 'd')):
            if not self._is_common_adjective(verb_text):
                return True
        
        return False

    def _is_past_participle_form(self, word, token=None):
        """Check if word is likely a past participle."""
        # Common past participles
        common_past_participles = {
            'been', 'gone', 'seen', 'done', 'made', 'taken', 'given', 'known',
            'thought', 'found', 'told', 'said', 'come', 'become', 'begun'
        }
        if word in common_past_participles:
            return True
        
        # Regular past participles end with -ed
        if len(word) > 2 and word.endswith(('ed', 'd')):
            if not self._is_common_adjective(word):
                return True
        
        return False

    # ==================== VERB FORM GENERATION ====================

    def _get_present_form(self, base_verb, index, tokens):
        """Get present tense form with SVA consideration."""
        # Check if this verb needs third person -s
        if self._needs_third_person_s(base_verb, index, tokens):
            forms = lemminflect.getInflection(base_verb, 'VBZ')
            return forms[0] if forms else base_verb + 's'
        return base_verb

    def _get_past_form(self, base_verb):
        """Get past tense form."""
        forms = lemminflect.getInflection(base_verb, 'VBD')
        
        if forms:
            return forms[0]
        else:
            # Fallback if lemminflect fails
            if base_verb.endswith('e'):
                return base_verb + 'd'
            else:
                return base_verb + 'ed'

    def _get_ing_form(self, base_verb):
        """Get -ing form."""
        forms = lemminflect.getInflection(base_verb, 'VBG')
        return forms[0] if forms else base_verb + 'ing'

    def _get_past_participle_form(self, base_verb):
        """Get past participle form."""
        forms = lemminflect.getInflection(base_verb, 'VBN')
        return forms[0] if forms else base_verb + 'ed'

    def _needs_third_person_s(self, base_verb, index, tokens):
        """Check if verb needs third person -s in present tense."""
        # Simple heuristic: if the subject is likely third person singular
        if index > 0 and index < len(tokens):
            prev_token = tokens[index - 1]
            prev_text = prev_token.text.lower() if hasattr(prev_token, 'text') else str(prev_token).lower()
            
            # Third person singular subjects
            third_person_subjects = {'he', 'she', 'it', 'someone', 'everyone', 'anyone', 'nobody'}
            if prev_text in third_person_subjects:
                return True
            
            # Singular nouns (simple check)
            if (prev_text.endswith('s') and 
                not prev_text.endswith(('ss', 'us', 'is', 'as', 'os')) and
                prev_text not in {'this', 'his', 'has', 'was', 'is', 'as', 'us'}):
                return True
        
        return False

    def _is_common_adjective(self, word):
        """Check if word is common adjective."""
        common_adjectives = {
            'red', 'bed', 'sad', 'mad', 'bad', 'glad', 'old', 'cold', 'bold',
            'tired', 'bored', 'scared', 'excited', 'interested', 'complicated'
        }
        return word in common_adjectives

    def _is_common_noun(self, word):
        """Check if word is common noun."""
        common_nouns = {
            'this', 'his', 'has', 'was', 'is', 'as', 'us', 'plus', 'bus',
            'class', 'glass', 'mass', 'pass', 'gas', 'news', 'means', 'series'
        }
        return word in common_nouns