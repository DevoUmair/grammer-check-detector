from grammar_checker.knowledge import LinguisticKnowledge
import re
from collections import defaultdict

class ConfusionSetDetector:
    def __init__(self):
        self.knowledge = LinguisticKnowledge()
        self.CONFUSION_SETS = self._build_comprehensive_confusion_sets()
        self._build_context_patterns()
        
    def _build_comprehensive_confusion_sets(self):
        """Build comprehensive confusion sets with semantic groupings."""
        return {
            # Possessive vs contraction vs location
            'their': ['there', "they're"],
            'there': ['their', "they're"], 
            "they're": ['their', 'there'],
            
            # Possessive vs contraction
            'your': ["you're"],
            "you're": ['your'],
            'its': ["it's"],
            "it's": ['its'],
            'whose': ["who's"],
            "who's": ['whose'],
            
            # Verb vs noun confusion
            'affect': ['effect'],
            'effect': ['affect'],
            'advice': ['advise'],
            'advise': ['advice'],
            'practice': ['practise'],
            'practise': ['practice'],
            'license': ['licence'],
            'licence': ['license'],
            
            # Time vs comparison
            'then': ['than'],
            'than': ['then'],
            
            # Acceptance vs exclusion
            'accept': ['except'],
            'except': ['accept'],
            
            # Loose vs lose
            'loose': ['lose'],
            'lose': ['loose'],
            
            # Principal vs principle
            'principal': ['principle'],
            'principle': ['principal'],
            
            # Stationary vs stationery
            'stationary': ['stationery'],
            'stationery': ['stationary'],
            
            # Complement vs compliment
            'complement': ['compliment'],
            'compliment': ['complement'],
            
            # Desert vs dessert
            'desert': ['dessert'],
            'dessert': ['desert'],
            
            # Eminent vs imminent
            'eminent': ['imminent'],
            'imminent': ['eminent'],
            
            # Ensure vs insure
            'ensure': ['insure'],
            'insure': ['ensure'],
            
            # Weather vs whether
            'weather': ['whether'],
            'whether': ['weather'],
            
            # Capital vs capitol
            'capital': ['capitol'],
            'capitol': ['capital'],
            
            # Cite vs site vs sight
            'cite': ['site', 'sight'],
            'site': ['cite', 'sight'],
            'sight': ['cite', 'site'],
            
            # Coarse vs course
            'coarse': ['course'],
            'course': ['coarse'],
            
            # Dual vs duel
            'dual': ['duel'],
            'duel': ['dual'],
            
            # Peace vs piece
            'peace': ['piece'],
            'piece': ['peace'],
            
            # Plain vs plane
            'plain': ['plane'],
            'plane': ['plain'],
            
            # Right vs write vs rite
            'right': ['write', 'rite'],
            'write': ['right', 'rite'],
            'rite': ['right', 'write'],
            
            # Waist vs waste
            'waist': ['waste'],
            'waste': ['waist'],
            
            # Weak vs week
            'weak': ['week'],
            'week': ['weak'],
            
            # Which vs witch
            'which': ['witch'],
            'witch': ['which'],
        }
    
    def _build_context_patterns(self):
        """Build context-based decision patterns for confusion words."""
        self.context_patterns = {
            'their': {
                'follows': ['they', 'people', 'students', 'children', 'parents', 'workers'],
                'precedes': ['house', 'car', 'home', 'family', 'friends', 'children', 'parents', 'job', 'work'],
                'patterns': [r'their\s+\w+ing', r'their\s+own', r'their\s+first', r'their\s+new']
            },
            'there': {
                'follows': ['is', 'are', 'was', 'were', 'has', 'have', 'had', 'seems', 'appears'],
                'precedes': ['is', 'are', 'was', 'were', 'has', 'have', 'had', 'seems', 'appears', 'should', 'could'],
                'patterns': [r'there\s+is', r'there\s+are', r'there\s+was', r'there\s+were', r'over\s+there', r'right\s+there']
            },
            "they're": {
                'follows': ['that', 'because', 'when', 'while', 'although'],
                'precedes': ['going', 'coming', 'waiting', 'working', 'studying', 'trying', 'planning'],
                'patterns': [r"they're\s+\w+ing", r"they're\s+going", r"they're\s+not", r"they're\s+very"]
            },
            'your': {
                'follows': ['this', 'that', 'these', 'those', 'for', 'with', 'about'],
                'precedes': ['name', 'house', 'car', 'family', 'friends', 'work', 'job', 'home', 'phone'],
                'patterns': [r'your\s+\w+', r'for\s+your', r'with\s+your', r'about\s+your']
            },
            "you're": {
                'follows': ['that', 'because', 'when', 'if', 'although'],
                'precedes': ['going', 'coming', 'waiting', 'working', 'right', 'welcome', 'sure'],
                'patterns': [r"you're\s+\w+ing", r"you're\s+going", r"you're\s+not", r"you're\s+the"]
            },
            'affect': {
                'follows': ['will', 'can', 'may', 'might', 'could', 'would', 'should', 'to'],
                'precedes': ['the', 'our', 'their', 'your', 'my', 'outcome', 'result', 'decision'],
                'patterns': [r'to\s+affect', r'will\s+affect', r'can\s+affect', r'negatively\s+affect']
            },
            'effect': {
                'follows': ['the', 'an', 'this', 'that', 'no', 'side', 'adverse'],
                'precedes': ['on', 'of', 'was', 'is', 'are', 'were'],
                'patterns': [r'the\s+effect', r'have\s+an\s+effect', r'no\s+effect', r'side\s+effect']
            },
            'then': {
                'follows': ['and', 'but', 'since', 'until', 'before', 'after'],
                'precedes': ['we', 'they', 'I', 'you', 'he', 'she', 'it', 'the'],
                'patterns': [r'and\s+then', r'but\s+then', r'since\s+then', r'until\s+then']
            },
            'than': {
                'follows': ['more', 'less', 'better', 'worse', 'bigger', 'smaller', 'rather', 'other'],
                'precedes': ['I', 'you', 'he', 'she', 'it', 'we', 'they', 'the', 'that'],
                'patterns': [r'more\s+than', r'less\s+than', r'better\s+than', r'rather\s+than']
            }
        }

    def detect(self, sentence_or_context):
        """Enhanced confusion word detection with comprehensive analysis."""
        if isinstance(sentence_or_context, dict):
            tokens = sentence_or_context.get('tokens', [])
            pos_tags = sentence_or_context.get('pos', [])
            doc = sentence_or_context.get('doc')
        else:
            tokens = sentence_or_context or []
            pos_tags = []
            doc = None

        errors = []
        
        for i, word in enumerate(tokens):
            lw = word.lower()
            
            if lw in self.CONFUSION_SETS:
                correct_word = self._analyze_context(i, tokens, pos_tags, doc)
                if correct_word and correct_word != lw:
                    errors.append(self._create_error(i, word, correct_word, tokens))
                        
        return errors

    def _analyze_context(self, index, tokens, pos_tags, doc):
        """Comprehensive context analysis to determine correct word."""
        word = tokens[index].lower()
        alternatives = self.CONFUSION_SETS[word]
        
        # Method 1: Check context patterns first
        pattern_match = self._check_context_patterns(word, index, tokens)
        if pattern_match:
            return pattern_match
        
        # Method 2: POS-based analysis
        pos_match = self._pos_based_analysis(word, index, tokens, pos_tags)
        if pos_match:
            return pos_match
            
        # Method 3: Semantic analysis
        semantic_match = self._semantic_analysis(word, alternatives, index, tokens)
        if semantic_match:
            return semantic_match
            
        # Method 4: Collocation analysis
        collocation_match = self._collocation_analysis(word, alternatives, index, tokens)
        if collocation_match:
            return collocation_match
            
        # If still uncertain, return None (no correction suggested)
        return None

    def _check_context_patterns(self, word, index, tokens):
        """Check context patterns for the given word."""
        if word not in self.context_patterns:
            return None
            
        patterns = self.context_patterns[word]
        context_text = ' '.join(tokens[max(0, index-2):min(len(tokens), index+3)]).lower()
        
        # Check preceding words
        if index > 0:
            prev_word = tokens[index-1].lower()
            if prev_word in patterns.get('follows', []):
                return word  # Context suggests current word is correct
        
        # Check following words  
        if index < len(tokens) - 1:
            next_word = tokens[index+1].lower()
            if next_word in patterns.get('precedes', []):
                return word  # Context suggests current word is correct
        
        # Check regex patterns
        for pattern in patterns.get('patterns', []):
            if re.search(pattern, context_text, re.IGNORECASE):
                return word  # Pattern matches current word
        
        # Check if alternative might be better
        for alternative in self.CONFUSION_SETS[word]:
            if alternative in self.context_patterns:
                alt_patterns = self.context_patterns[alternative]
                for pattern in alt_patterns.get('patterns', []):
                    if re.search(pattern, context_text, re.IGNORECASE):
                        return alternative
        
        return None

    def _pos_based_analysis(self, word, index, tokens, pos_tags):
        """POS-based analysis for confusion words."""
        if not pos_tags or index >= len(pos_tags):
            return None
            
        current_pos = pos_tags[index] if index < len(pos_tags) else None
        
        # Their (possessive) vs There (adverb) vs They're (contraction + verb)
        if word == 'their' and current_pos in ['PRON', 'DET']:
            return 'their'
        elif word == 'there' and current_pos in ['ADV']:
            return 'there'
        elif word == "they're" and current_pos in ['VERB', 'AUX']:
            return "they're"
            
        # Your (possessive) vs You're (contraction + verb)
        elif word == 'your' and current_pos in ['PRON', 'DET']:
            return 'your'
        elif word == "you're" and current_pos in ['VERB', 'AUX']:
            return "you're"
            
        # Its (possessive) vs It's (contraction + verb)
        elif word == 'its' and current_pos in ['PRON', 'DET']:
            return 'its'
        elif word == "it's" and current_pos in ['VERB', 'AUX']:
            return "it's"
            
        # Affect (verb) vs Effect (noun)
        elif word == 'affect' and current_pos in ['VERB']:
            return 'affect'
        elif word == 'effect' and current_pos in ['NOUN']:
            return 'effect'
            
        # Then (adverb) vs Than (conjunction)
        elif word == 'then' and current_pos in ['ADV']:
            return 'then'
        elif word == 'than' and current_pos in ['CONJ', 'ADP']:
            return 'than'
            
        return None

    def _semantic_analysis(self, word, alternatives, index, tokens):
        """Enhanced semantic analysis using context."""
        context_words = self._get_extended_context(index, tokens)
        
        # Specialized semantic rules for common confusion pairs
        if word in ['their', 'there', "they're"]:
            return self._analyze_their_there_theyre(word, context_words)
        elif word in ['your', "you're"]:
            return self._analyze_your_youre(word, context_words)
        elif word in ['affect', 'effect']:
            return self._analyze_affect_effect(word, context_words)
        elif word in ['then', 'than']:
            return self._analyze_then_than(word, context_words)
        elif word in ['accept', 'except']:
            return self._analyze_accept_except(word, context_words)
            
        return None

    def _collocation_analysis(self, word, alternatives, index, tokens):
        """Analyze word collocations to determine correct usage."""
        context_text = ' '.join(tokens[max(0, index-3):min(len(tokens), index+4)]).lower()
        
        collocation_scores = {}
        for alternative in [word] + alternatives:
            collocation_scores[alternative] = self._calculate_collocation_score(alternative, context_text)
        
        best_match = max(collocation_scores.items(), key=lambda x: x[1])
        if best_match[1] > 0.5:  # Confidence threshold
            return best_match[0]
            
        return None

    def _calculate_collocation_score(self, word, context):
        """Calculate collocation score for a word in context."""
        common_collocations = {
            'their': ['friend', 'house', 'car', 'family', 'home', 'child', 'parent', 'job', 'work', 'own'],
            'there': ['is', 'are', 'was', 'were', 'has', 'have', 'had', 'here', 'over', 'right', 'up'],
            "they're": ['going', 'coming', 'waiting', 'working', 'studying', 'trying', 'planning', 'here'],
            'your': ['name', 'house', 'car', 'family', 'friend', 'home', 'phone', 'email', 'address'],
            "you're": ['going', 'coming', 'waiting', 'working', 'welcome', 'right', 'sure', 'here'],
            'affect': ['will', 'can', 'may', 'might', 'could', 'would', 'negatively', 'positively', 'directly'],
            'effect': ['the', 'on', 'of', 'side', 'adverse', 'positive', 'negative', 'significant'],
            'then': ['and', 'but', 'since', 'until', 'before', 'after', 'now', 'back', 'right'],
            'than': ['more', 'less', 'better', 'worse', 'bigger', 'smaller', 'rather', 'other', 'ever']
        }
        
        if word not in common_collocations:
            return 0
            
        score = 0
        for collocate in common_collocations[word]:
            if collocate in context:
                score += 1
                
        return score / len(common_collocations[word])

    def _analyze_their_there_theyre(self, word, context_words):
        """Specialized analysis for their/there/they're confusion."""
        has_verb = any(w in ['is', 'are', 'was', 'were', 'has', 'have', 'had'] for w in context_words)
        has_noun = any(w in ['house', 'car', 'home', 'family', 'friend'] for w in context_words)
        has_ing = any(w.endswith('ing') for w in context_words)
        
        if has_verb and not has_noun:
            return 'there'
        elif has_noun and not has_verb:
            return 'their'
        elif has_ing:
            return "they're"
            
        return None

    def _analyze_your_youre(self, word, context_words):
        """Specialized analysis for your/you're confusion."""
        has_verb = any(w in ['are', 'were'] for w in context_words)
        has_noun = any(w in ['house', 'car', 'home', 'family', 'friend'] for w in context_words)
        has_ing = any(w.endswith('ing') for w in context_words)
        
        if has_verb or has_ing:
            return "you're"
        elif has_noun:
            return 'your'
            
        return None

    def _analyze_affect_effect(self, word, context_words):
        """Specialized analysis for affect/effect confusion."""
        has_determiner = any(w in ['the', 'an', 'this', 'that'] for w in context_words)
        has_modal = any(w in ['will', 'can', 'may', 'might', 'could'] for w in context_words)
        
        if has_determiner:
            return 'effect'
        elif has_modal:
            return 'affect'
            
        return None

    def _analyze_then_than(self, word, context_words):
        """Specialized analysis for then/than confusion."""
        has_comparative = any(w in ['more', 'less', 'better', 'worse', 'bigger', 'smaller'] for w in context_words)
        has_sequence = any(w in ['first', 'next', 'after', 'before', 'finally'] for w in context_words)
        
        if has_comparative:
            return 'than'
        elif has_sequence:
            return 'then'
            
        return None

    def _analyze_accept_except(self, word, context_words):
        """Specialized analysis for accept/except confusion."""
        has_inclusion = any(w in ['all', 'every', 'everything', 'everyone'] for w in context_words)
        has_offer = any(w in ['offer', 'invitation', 'proposal', 'apology'] for w in context_words)
        
        if has_inclusion:
            return 'except'
        elif has_offer:
            return 'accept'
            
        return None

    def _get_extended_context(self, index, tokens, window=5):
        """Get extended context around the target word."""
        start = max(0, index - window)
        end = min(len(tokens), index + window + 1)
        return [tokens[i].lower() for i in range(start, end) if i != index]

    def _create_error(self, index, original_word, correct_word, tokens):
        """Create an error dictionary with enhanced messaging."""
        explanations = {
            'their': "shows possession (belonging to them)",
            'there': "refers to a place or existence",
            "they're": "is a contraction of 'they are'",
            'your': "shows possession (belonging to you)", 
            "you're": "is a contraction of 'you are'",
            'its': "shows possession (belonging to it)",
            "it's": "is a contraction of 'it is' or 'it has'",
            'affect': "is usually a verb meaning to influence",
            'effect': "is usually a noun meaning a result",
            'then': "refers to time or sequence",
            'than': "is used for comparisons"
        }
        
        explanation = explanations.get(correct_word, "")
        message = f"Confused word: '{original_word}'. Did you mean '{correct_word}'? {explanation}"
        
        return {
            'pos': index,
            'message': message,
            'suggestion': {
                'type': 'replace', 
                'index': index, 
                'word': correct_word,
                'original': original_word,
                'confidence': 'high'
            }
        }