from dataclasses import dataclass, field
from nltk.corpus import wordnet as wn
import lemminflect

@dataclass
class LinguisticKnowledge:
    """Enhanced linguistic knowledge base using NLTK and custom rules."""
    
    # Enhanced tense markers
    PAST_TENSE_MARKERS: set = field(default_factory=lambda: {
        'yesterday', 'ago', 'last', 'previous', 'earlier', 'before', 'once', 
        'already', 'recently', 'formerly', 'last night', 'last week', 
        'last month', 'last year', 'days ago', 'weeks ago', 'months ago', 
        'years ago', 'previously', 'back then', 'in the past', 'formerly',
        'historically', 'once upon a time', 'in ancient times'
    })

    PRESENT_TENSE_MARKERS: set = field(default_factory=lambda: {
        'now', 'currently', 'today', 'nowadays', 'these days', 'at present', 
        'at the moment', 'right now', 'as we speak', 'this week', 'this month',
        'this year', 'always', 'usually', 'often', 'sometimes', 'never',
        'currently', 'presently', 'now and then', 'from time to time'
    })

    FUTURE_TENSE_MARKERS: set = field(default_factory=lambda: {
        'tomorrow', 'next', 'soon', 'later', 'eventually', 'shortly', 
        'in future', 'in a while', 'the day after tomorrow', 'next week', 
        'next month', 'next year', 'in a few days', 'coming', 'upcoming',
        'forthcoming', 'in the future', 'down the road', 'eventually'
    })

    # Conditional markers
    CONDITIONAL_MARKERS: set = field(default_factory=lambda: {
        'if', 'unless', 'provided', 'as long as', 'on condition that',
        'assuming', 'supposing', 'in case'
    })

    # Historical present indicators
    HISTORICAL_PRESENT_MARKERS: set = field(default_factory=lambda: {
        'suddenly', 'then', 'now', 'immediately', 'all of a sudden',
        'without warning', 'just then'
    })

    # Universal truth indicators  
    UNIVERSAL_TRUTH_MARKERS: set = field(default_factory=lambda: {
        'always', 'never', 'every', 'all', 'each', 'any', 'whenever',
        'wherever', 'whoever', 'whatever'
    })

    # Irregular verb forms for better tense detection
    IRREGULAR_PAST_VERBS: set = field(default_factory=lambda: {
        'was', 'were', 'had', 'did', 'went', 'saw', 'came', 'told', 'said',
        'took', 'made', 'knew', 'thought', 'found', 'gave', 'got', 'stood',
        'understood', 'began', 'became', 'broke', 'brought', 'built', 'bought',
        'caught', 'chose', 'came', 'cost', 'cut', 'dug', 'drew', 'drank', 'drove',
        'ate', 'fell', 'felt', 'fought', 'found', 'flew', 'forgot', 'forgave',
        'froze', 'got', 'gave', 'went', 'grew', 'hung', 'had', 'heard', 'hid',
        'hit', 'held', 'hurt', 'kept', 'knew', 'laid', 'led', 'left', 'lent',
        'let', 'lay', 'lost', 'made', 'meant', 'met', 'paid', 'put', 'read',
        'rode', 'rang', 'rose', 'ran', 'said', 'saw', 'sold', 'sent', 'set',
        'shook', 'shone', 'shot', 'showed', 'shut', 'sang', 'sank', 'sat',
        'slept', 'spoke', 'spent', 'stood', 'stole', 'stuck', 'struck',
        'swore', 'swept', 'swam', 'took', 'taught', 'tore', 'told', 'thought',
        'threw', 'understood', 'woke', 'wore', 'won', 'wrote'
    })

    def is_irregular_past_verb(self, word):
        """Check if word is an irregular past tense verb."""
        return word.lower() in self.IRREGULAR_PAST_VERBS

    # Zero article nouns
    ZERO_ARTICLE_NOUNS: set = field(default_factory=lambda: {
        # Institutions & Places (when used for their primary purpose)
        'school', 'college', 'university', 'church', 'temple', 'mosque', 'hospital', 'prison', 'jail', 'court',
        'work', 'home', 'sea', 'bed', 'camp', 'class', 'town', 'city',

        # Meals
        'breakfast', 'lunch', 'dinner', 'supper', 'brunch', 'tea', 'coffee',

        # Sports, Games, & Activities
        'football', 'soccer', 'cricket', 'tennis', 'basketball', 'baseball', 'volleyball', 'hockey', 'golf', 'rugby',
        'chess', 'checkers', 'draughts', 'poker', 'bridge', 'billiards', 'darts', 'badminton', 'cycling', 'jogging',
        'swimming', 'skiing', 'boxing', 'wrestling', 'athletics', 'gymnastics',

        # Academic Subjects & Disciplines
        'mathematics', 'maths', 'math', 'physics', 'chemistry', 'biology', 'history', 'geography', 'economics',
        'english', 'french', 'spanish', 'german', 'chinese', 'art', 'music', 'literature', 'philosophy', 'psychology',
        'sociology', 'engineering', 'computer science', 'programming', 'astronomy', 'geology', 'logic', 'calculus',
        'algebra', 'grammar', 'linguistics',

        # Time & Calendar
        'night', 'day', 'noon', 'midnight', 'dawn', 'dusk', 'sunrise', 'sunset', 'daytime', 'nighttime',
        'yesterday', 'today', 'tomorrow', 'tonight', 'now', 'later', 'ago', 'soon', 'early', 'late',
        'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december',
        'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
        'spring', 'summer', 'autumn', 'fall', 'winter',
        'christmas', 'easter', 'halloween', 'ramadan', 'hanukkah', 'diwali',

        # Transport & Travel ("by" transport)
        'bus', 'train', 'car', 'boat', 'ship', 'plane', 'airplane', 'bicycle', 'bike', 'metro', 'subway', 'tube', 'taxi', 'foot',

        # Other Common Concepts
        'space', 'nature', 'society', 'government', 'parliament', 'congress', 'life', 'death', 'war', 'peace',
        'heaven', 'hell', 'court',

        # Common activities & hobbies
    'shopping', 'swimming', 'dancing', 'singing', 'reading', 'writing', 'painting', 'drawing',
    'cooking', 'baking', 'eating', 'drinking', 'sleeping', 'jogging', 'running', 'walking',
    'cycling', 'hiking', 'climbing', 'traveling', 'travelling', 'driving', 'flying',
    'fishing', 'hunting', 'gardening', 'knitting', 'sewing',

    # General concepts and states
    'learning', 'teaching', 'studying', 'working', 'coding', 'programming',
    'thinking', 'feeling', 'believing', 'understanding', 'knowing',
    'listening', 'speaking', 'talking', 'whispering', 'shouting',
    'laughing', 'crying', 'smiling', 'frowning',
    'waiting', 'standing', 'sitting', 'lying',

    # Sports and games
    'boxing', 'wrestling', 'skiing', 'snowboarding', 'skating', 'surfing', 'sailing', 'canoeing',
    'bowling', 'training', 'coaching', 'competing', 'winning', 'losing',

    # Other common gerunds
    'beginning', 'ending', 'meeting', 'planning', 'building', 'cleaning', 'washing',
    'packing', 'unpacking', 'moving', 'decorating', 'parenting', 'aging', 'ageing', 'dying',
    'raining', 'snowing',
    })

    # Uncountable nouns
    UNCOUNTABLE_NOUNS: set = field(default_factory=lambda: {
        # Abstract Concepts & States
        'advice', 'information', 'knowledge', 'research', 'evidence', 'data', 'intelligence',
        'progress', 'feedback', 'education', 'employment', 'unemployment', 'poverty',
        'wealth', 'health', 'safety', 'violence', 'crime',
        'happiness', 'sadness', 'joy', 'anger', 'love', 'hate', 'fear', 'anxiety', 'stress', 'peace',
        'freedom', 'justice', 'democracy', 'fun', 'leisure', 'time', 'luck', 'patience',
        'honesty', 'integrity', 'confidence', 'courage', 'permission', 'consent', 'respect',

        # Liquids & Gases
        'water', 'milk', 'coffee', 'tea', 'juice', 'wine', 'beer', 'champagne', 'blood', 'oil', 'petrol', 'gasoline',
        'gas', 'air', 'oxygen', 'hydrogen', 'steam', 'smoke',

        # Materials & Substances
        'gold', 'silver', 'iron', 'steel', 'copper', 'wood', 'plastic', 'glass', 'paper', 'cloth', 'cotton', 'wool',
        'sand', 'dirt', 'soil', 'mud', 'dust', 'grass', 'hair', 'fur', 'snow', 'ice', 'fire',

        # Food & Ingredients
        'rice', 'bread', 'butter', 'sugar', 'salt', 'pepper', 'flour', 'cheese', 'meat', 'beef', 'pork', 'chicken',
        'fish', 'fruit', 'pasta', 'spaghetti', 'macaroni', 'soup', 'vinegar', 'chocolate',

        # Collective Categories
        'furniture', 'equipment', 'machinery', 'technology', 'software', 'hardware',
        'luggage', 'baggage', 'clothing', 'underwear', 'jewelry', 'jewellery',
        'homework', 'housework', 'work',

        # Other
        'money', 'cash', 'currency', 'credit', 'debt',
        'mail', 'postage', 'email',
        'scenery', 'poetry', 'music', 'art', 'dance',
        'garbage', 'rubbish', 'trash', 'pollution',
        'weather', 'thunder', 'lightning', 'rain', 'snow', 'sleet', 'wind', 'fog', 'sunshine',
        'traffic', 'transportation', 'accommodation',
        'news', 'help', 'weight', 'strength', 'length', 'height', 'width', 'depth',
    })

    CONFUSION_SETS: dict = field(default_factory=lambda: {
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
        'device': ['devise'],
        'devise': ['device'],
        
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
        
        # Ensure vs insure vs assure
        'ensure': ['insure', 'assure'],
        'insure': ['ensure', 'assure'],
        'assure': ['ensure', 'insure'],
        
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
        
        # Born vs borne
        'born': ['borne'],
        'borne': ['born'],
        
        # Canvas vs canvass
        'canvas': ['canvass'],
        'canvass': ['canvas'],
        
        # Cereal vs serial
        'cereal': ['serial'],
        'serial': ['cereal'],
        
        # Current vs currant
        'current': ['currant'],
        'currant': ['current'],
    })

    # Preposition collocations
    PREPOSITION_COLLOCATIONS: dict = field(default_factory=lambda: {
        'go': {'to': ['school', 'work', 'bed', 'church', 'hospital']},
        'arrive': {'at': ['station', 'airport'], 'in': ['city', 'country']},
        'look': {'at': ['picture'], 'for': ['keys'], 'after': ['children']},
        'good': {'at': ['math', 'sports'], 'for': ['health']},
        'interested': {'in': ['art', 'science']},
        'depend': {'on': ['weather']},
        'apologize': {'for': ['mistake'], 'to': ['person']},
        'believe': {'in': ['truth']},
        'agree': {'with': ['person'], 'to': ['plan']}
    })

    # Helping verb errors
    HELPING_VERB_ERRORS: dict = field(default_factory=lambda: {
        'could of': 'could have',
        'would of': 'would have', 
        'should of': 'should have',
        'might of': 'might have',
        'must of': 'must have'
    })
    # Context patterns for confusion words
    CONFUSION_CONTEXTS: dict = field(default_factory=lambda: {
        'their': {'possession': True, 'requires_noun': True},
        'there': {'location': True, 'often_before_verb': True},
        "they're": {'contraction': True, 'requires_verb': True},
        'your': {'possession': True, 'requires_noun': True},
        "you're": {'contraction': True, 'requires_verb': True},
        'affect': {'verb': True, 'action': True},
        'effect': {'noun': True, 'result': True},
        'then': {'time': True, 'sequence': True},
        'than': {'comparison': True},
    })

    def get_confusion_context_rules(self, word):
        """Get context rules for confusion words."""
        return self.CONFUSION_CONTEXTS.get(word.lower(), {})
    
    def detect_tense_from_markers(self, sentence):
        """Detect tense based on time markers."""
        sentence_lower = sentence.lower()
        
        if any(marker in sentence_lower for marker in self.PAST_TENSE_MARKERS):
            return "past"
        elif any(marker in sentence_lower for marker in self.FUTURE_TENSE_MARKERS):
            return "future"
        elif any(marker in sentence_lower for marker in self.PRESENT_TENSE_MARKERS):
            return "present"
        return None

    def should_have_zero_article(self, noun, context=None):
        """Check if noun should be used without article."""
        noun_lower = noun.lower()
        
        if (noun_lower in self.ZERO_ARTICLE_NOUNS or 
            noun_lower in self.UNCOUNTABLE_NOUNS):
            return True
            
        # Check WordNet for uncountable nouns
        try:
            synsets = wn.synsets(noun_lower, pos=wn.NOUN)
            for synset in synsets:
                if any('mass' in lemma.name().lower() for lemma in synset.lemmas()):
                    return True
        except:
            pass
            
        return False

    def is_uncountable_noun(self, word):
        """Check if noun is uncountable."""
        return word.lower() in self.UNCOUNTABLE_NOUNS

    def get_confusion_alternatives(self, word):
        """Get confusion word alternatives."""
        return self.CONFUSION_SETS.get(word.lower(), [])
    
    SILENT_H_WORDS: set = field(default_factory=lambda: {
        'honor', 'honest', 'hour', 'heir', 'honorable', 'honorary'
    })

    Y_SOUND_WORDS: set = field(default_factory=lambda: {
        'university', 'european', 'unique', 'one', 'once', 'user', 'ukulele'
    })

    ACRONYM_VOWEL_SOUNDS: set = field(default_factory=lambda: set("AEFHI" ))
    # A (ay), E (ee), F (ef), H (aitch), I (eye)
