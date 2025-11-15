from dataclasses import dataclass, field
from typing import Dict, List, Set

@dataclass
class LinguisticKnowledge:
    """Comprehensive linguistic knowledge base for advanced grammar correction."""

    # ============================================================
    # 1. ZERO ARTICLE NOUNS (Used without 'a/an/the' in certain contexts)
    # ============================================================
    ZERO_ARTICLE_NOUNS: set = field(default_factory=lambda: {
        # ==================== INSTITUTIONS & PLACES ====================
        # Educational institutions
        'school', 'college', 'university', 'kindergarten', 'preschool', 'nursery', 
        'academy', 'institute', 'campus', 'class', 'lecture', 'seminar', 'workshop',
        
        # Religious institutions
        'church', 'mosque', 'temple', 'synagogue', 'cathedral', 'chapel', 'shrine',
        'monastery', 'abbey', 'pagoda',
        
        # Medical institutions
        'hospital', 'clinic', 'surgery', 'infirmary', 'dispensary', 'asylum',
        'sanatorium', 'health center', 'medical center',
        
        # Legal & Government institutions
        'court', 'jail', 'prison', 'parliament', 'congress', 'senate', 'assembly',
        'legislature', 'council', 'committee', 'cabinet', 'ministry', 'embassy',
        'police station', 'fire station', 'post office', 'town hall',
        
        # Work & Business places
        'work', 'office', 'factory', 'warehouse', 'studio', 'laboratory', 'workshop',
        'headquarters', 'branch', 'outlet', 'store', 'shop', 'market',
        
        # Entertainment & Cultural places
        'cinema', 'theater', 'opera', 'ballet', 'museum', 'gallery', 'library',
        'stadium', 'arena', 'gym', 'pool', 'park', 'zoo', 'circus',
        
        # ==================== MEALS & FOOD ====================
        'breakfast', 'lunch', 'dinner', 'supper', 'brunch', 'tea', 'coffee',
        'appetizer', 'dessert', 'snack', 'supper', 'banquet', 'feast', 'picnic',
        'barbecue', 'buffet', 'reception', 'banquet', 'meal', 'food', 'drink',
        
        # ==================== SPORTS & GAMES ====================
        # Team sports
        'football', 'soccer', 'cricket', 'rugby', 'baseball', 'basketball', 'hockey',
        'volleyball', 'handball', 'water polo', 'netball',
        
        # Individual sports
        'tennis', 'golf', 'boxing', 'wrestling', 'judo', 'karate', 'fencing',
        'archery', 'shooting', 'swimming', 'running', 'jumping', 'cycling',
        
        # Winter sports
        'skiing', 'snowboarding', 'skating', 'curling', 'ice hockey',
        
        # Games & activities
        'chess', 'poker', 'bridge', 'monopoly', 'scrabble', 'bingo', 'darts',
        'billiards', 'bowling', 'dancing', 'singing', 'acting', 'painting',
        
        # ==================== ACADEMIC SUBJECTS ====================
        # Sciences
        'mathematics', 'math', 'physics', 'chemistry', 'biology', 'geology',
        'astronomy', 'meteorology', 'oceanography', 'botany', 'zoology',
        'microbiology', 'genetics', 'ecology',
        
        # Social sciences
        'economics', 'psychology', 'sociology', 'anthropology', 'archaeology',
        'political science', 'international relations', 'development studies',
        
        # Humanities
        'history', 'geography', 'philosophy', 'literature', 'poetry', 'linguistics',
        'theology', 'religious studies', 'classics', 'archaeology',
        
        # Languages
        'english', 'french', 'spanish', 'german', 'italian', 'portuguese',
        'russian', 'chinese', 'japanese', 'arabic', 'hindi', 'sanskrit',
        
        # Arts & creative subjects
        'art', 'music', 'drama', 'theater', 'dance', 'film', 'photography',
        'architecture', 'design', 'fashion', 'culinary arts',
        
        # Professional subjects
        'medicine', 'law', 'business', 'accounting', 'engineering', 'nursing',
        'pharmacy', 'dentistry', 'veterinary science', 'agriculture',
        
        # ==================== TIME & SEASONS ====================
        # Times of day
        'dawn', 'sunrise', 'morning', 'noon', 'afternoon', 'evening', 'dusk',
        'sunset', 'twilight', 'night', 'midnight', 'daybreak', 'nightfall',
        
        # Days & periods
        'day', 'night', 'week', 'month', 'year', 'century', 'millennium',
        'spring', 'summer', 'autumn', 'fall', 'winter', 'season',
        
        # ==================== TRANSPORTATION ====================
        # Public transport
        'bus', 'train', 'subway', 'metro', 'tram', 'ferry', 'taxi', 'cab',
        'airplane', 'plane', 'helicopter', 'ship', 'boat', 'yacht',
        
        # Personal transport
        'car', 'bicycle', 'bike', 'motorcycle', 'scooter', 'rickshaw',
        'walking', 'running', 'cycling', 'driving', 'flying',
        
        # ==================== HEALTH & MEDICINE ====================
        'cancer', 'diabetes', 'flu', 'malaria', 'cholera', 'pneumonia', 'covid',
        'measles', 'smallpox', 'tuberculosis', 'asthma', 'arthritis', 'allergy',
        'headache', 'fever', 'cold', 'cough', 'pain', 'stress', 'anxiety',
        'depression', 'health', 'fitness', 'exercise', 'yoga', 'meditation',
        
        # ==================== NATURE & ENVIRONMENT ====================
        'nature', 'space', 'earth', 'sky', 'sea', 'ocean', 'river', 'lake',
        'mountain', 'forest', 'jungle', 'desert', 'beach', 'island',
        'weather', 'climate', 'rain', 'snow', 'wind', 'sunshine', 'thunder',
        'lightning', 'gravity', 'magnetism', 'electricity',
        
        # ==================== ABSTRACT CONCEPTS ====================
        'life', 'death', 'love', 'hatred', 'peace', 'war', 'justice', 'freedom',
        'democracy', 'capitalism', 'socialism', 'communism', 'religion',
        'science', 'art', 'beauty', 'truth', 'knowledge', 'wisdom', 'ignorance',
        'happiness', 'sadness', 'anger', 'fear', 'courage', 'hope', 'despair',
        'time', 'space', 'energy', 'matter', 'reality', 'fantasy', 'dream',
        'nightmare', 'consciousness', 'subconscious', 'memory', 'imagination',
        
        # ==================== DAILY ACTIVITIES ====================
        'work', 'sleep', 'rest', 'play', 'study', 'reading', 'writing',
        'cooking', 'cleaning', 'shopping', 'banking', 'traveling',
        
        # ==================== SPECIAL CATEGORIES ====================
        'bed', 'home', 'town', 'society', 'heaven', 'hell', 'paradise',
        'purgatory', 'nirvana', 'valhalla', 'utopia', 'market', 'court',
        
        # ==================== MODERN CONCEPTS ====================
        'internet', 'email', 'social media', 'streaming', 'gaming',
        'programming', 'coding', 'design', 'marketing', 'advertising',
        
        # ==================== WEATHER PHENOMENA ====================
        'rain', 'snow', 'hail', 'sleet', 'fog', 'mist', 'dew', 'frost',
        'humidity', 'pressure', 'temperature', 'climate',
        
        # ==================== BODY & HEALTH ====================
        'exercise', 'yoga', 'meditation', 'therapy', 'treatment',
        'recovery', 'rehabilitation', 'fitness', 'wellness',
        
        # ==================== EDUCATION & LEARNING ====================
        'learning', 'teaching', 'training', 'coaching', 'mentoring',
        'research', 'study', 'practice', 'revision',
        
        # ==================== ENTERTAINMENT & LEISURE ====================
        'entertainment', 'leisure', 'recreation', 'amusement', 'fun',
        'pleasure', 'enjoyment', 'relaxation', 'vacation', 'holiday',
        
        # ==================== TECHNOLOGY & DIGITAL ====================
        'computing', 'programming', 'coding', 'design', 'development',
        'engineering', 'analysis', 'testing', 'debugging',
        
        # ==================== BUSINESS & FINANCE ====================
        'business', 'commerce', 'trade', 'finance', 'banking', 'investment',
        'marketing', 'advertising', 'management', 'administration',
        
        # ==================== LEGAL & GOVERNMENT ====================
        'law', 'justice', 'government', 'politics', 'diplomacy',
        'administration', 'bureaucracy', 'legislation',
        
        # ==================== EMOTIONS & STATES ====================
        'happiness', 'sadness', 'anger', 'fear', 'surprise', 'disgust',
        'joy', 'sorrow', 'grief', 'ecstasy', 'bliss', 'misery',
        'confidence', 'doubt', 'certainty', 'uncertainty',
        
        # ==================== SOCIAL CONCEPTS ====================
        'friendship', 'love', 'marriage', 'family', 'community', 'society',
        'culture', 'tradition', 'custom', 'heritage', 'civilization',
        
        # ==================== PHILOSOPHICAL CONCEPTS ====================
        'philosophy', 'ethics', 'morality', 'virtue', 'vice', 'good', 'evil',
        'right', 'wrong', 'truth', 'falsehood', 'reality', 'illusion',
        
        # ==================== RELIGIOUS CONCEPTS ====================
        'religion', 'faith', 'belief', 'worship', 'prayer', 'meditation',
        'salvation', 'redemption', 'sin', 'virtue', 'heaven', 'hell',
        
        # ==================== ACCOMMODATION & LIVING ====================
        'accommodation', 'housing', 'shelter', 'residence', 'dwelling',
        'lodging', 'boarding', 'renting', 'leasing',
        
        # ==================== COMMUNICATION ====================
        'communication', 'conversation', 'discussion', 'debate', 'argument',
        'negotiation', 'persuasion', 'explanation', 'description',
        
        # ==================== MOVEMENT & TRAVEL ====================
        'travel', 'journey', 'voyage', 'expedition', 'tour', 'trip',
        'excursion', 'pilgrimage', 'migration', 'immigration', 'emigration',
        
        # ==================== CONFLICT & PEACE ====================
        'war', 'peace', 'conflict', 'struggle', 'battle', 'fight', 'combat',
        'violence', 'aggression', 'defense', 'protection', 'security',
        
        # ==================== CREATION & DESTRUCTION ====================
        'creation', 'destruction', 'construction', 'demolition',
        'production', 'manufacture', 'assembly', 'disassembly',
        
        # ==================== KNOWLEDGE & INFORMATION ====================
        'knowledge', 'information', 'data', 'wisdom', 'intelligence',
        'understanding', 'comprehension', 'awareness', 'consciousness',
        
        # ==================== ECONOMIC CONCEPTS ====================
        'economy', 'market', 'trade', 'commerce', 'industry', 'business',
        'employment', 'unemployment', 'inflation', 'recession', 'growth',
        
        # ==================== ENVIRONMENTAL CONCEPTS ====================
        'environment', 'ecology', 'conservation', 'preservation',
        'pollution', 'conservation', 'sustainability', 'biodiversity',
    })
    
    # ============================================================
    # 2. UNCOUNTABLE NOUNS
    # ============================================================
    UNCOUNTABLE: set = field(default_factory=lambda: {
        # Abstract Concepts
        'advice', 'information', 'knowledge', 'research', 'evidence', 'progress', 'feedback',
        'education', 'employment', 'poverty', 'wealth', 'health', 'safety', 'violence',
        'happiness', 'sadness', 'anger', 'love', 'hate', 'fear', 'peace', 'freedom',
        'fun', 'leisure', 'luck', 'patience', 'honesty', 'integrity', 'permission', 'respect',
        'access', 'data', 'software', 'hardware', 'intelligence', 'wisdom', 'justice',
        'democracy', 'freedom', 'equality', 'beauty', 'truth', 'time', 'space',

        # Categories and Groups
        'furniture', 'equipment', 'luggage', 'baggage', 'homework', 'housework', 'work',
        'money', 'cash', 'currency', 'mail', 'postage', 'scenery', 'poetry', 'music', 'art',
        'clothing', 'machinery', 'garbage', 'rubbish', 'trash', 'jewelry', 'underwear',
        'stationery', 'cutlery', 'crockery', 'foliage', 'vegetation',

        # Substances / Materials
        'water', 'milk', 'coffee', 'tea', 'juice', 'wine', 'beer', 'blood', 'sweat',
        'rice', 'bread', 'butter', 'sugar', 'salt', 'pepper', 'flour', 'cheese', 'meat', 'pasta',
        'gold', 'silver', 'oil', 'electricity', 'energy', 'gas', 'air', 'oxygen', 'hydrogen',
        'cotton', 'wood', 'plastic', 'steel', 'sand', 'chalk', 'soap', 'glass', 'paper',
        'concrete', 'cement', 'grass', 'hair', 'skin',

        # Natural phenomena
        'weather', 'traffic', 'news', 'transportation', 'accommodation', 'pollution',
        'gravity', 'lightning', 'thunder', 'rain', 'snow', 'fog', 'sunshine', 'darkness',
        'heat', 'cold', 'electricity', 'magnetism',

        # Fields of study (when referring to the subject)
        'mathematics', 'physics', 'chemistry', 'biology', 'economics', 'philosophy',
        'psychology', 'sociology', 'linguistics'
    })

    # ============================================================
    # 3. DEFINITE ARTICLE NOUNS (Usually require 'the')
    # ============================================================
    DEFINITE_ARTICLE_NOUNS: set = field(default_factory=lambda: {
        # Unique Entities
        'sun', 'moon', 'earth', 'sky', 'internet', 'world', 'universe', 'atmosphere',
        'equator', 'north pole', 'south pole', 'horizon', 'solar system', 'milky way',

        # Geographical features
        'ocean', 'sea', 'river', 'mountain', 'desert', 'forest', 'jungle', 'beach',
        'coast', 'shore', 'countryside', 'landscape',

        # Roles / Titles (when specific)
        'president', 'prime minister', 'pope', 'king', 'queen', 'ceo', 'director',
        'manager', 'captain', 'principal',

        # Groups / Institutions
        'government', 'police', 'army', 'navy', 'air force', 'media', 'press', 'judiciary',
        'public', 'population', 'community', 'society',

        # Concepts
        'climate', 'economy', 'environment', 'atmosphere', 'past', 'present', 'future',
        'weather', 'time', 'space',

        # Superlatives
        'best', 'worst', 'first', 'last', 'only', 'same',

        # Musical instruments
        'piano', 'guitar', 'violin', 'drums', 'flute', 'trumpet', 'saxophone',

        # Historical periods/events
        'renaissance', 'middle ages', 'stone age', 'world war', 'great depression'
    })

    # ============================================================
    # 4. ENHANCED PREPOSITION COLLOCATIONS
    # ============================================================
    PREPOSITION_COLLOCATIONS: dict = field(default_factory=lambda: {
        # VERBS WITH PREPOSITIONS (Expanded)
        'go': {
            'to': ['school', 'work', 'bed', 'church', 'market', 'hospital', 'gym', 'university', 'party', 'concert', 'meeting', 'restaurant'],
            'for': ['walk', 'run', 'swim', 'drive', 'meal', 'drink', 'hike', 'ride'],
            'on': ['holiday', 'vacation', 'trip', 'journey', 'cruise', 'adventure', 'date'],
            'through': ['process', 'procedure', 'difficulties', 'trouble'],
            'without': ['food', 'water', 'sleep', 'permission', 'help']
        },
        
        'arrive': {
            'at': ['station', 'airport', 'school', 'work', 'hotel', 'office', 'venue', 'destination', 'meeting point'],
            'in': ['city', 'country', 'town', 'village', 'room', 'building', 'area', 'region'],
            'on': ['time', 'schedule', 'platform', 'scene']
        },
        
        'participate': {
            'in': ['event', 'meeting', 'competition', 'conference', 'discussion', 'program', 'activity', 'survey', 'research']
        },
        
        'depend': {
            'on': ['weather', 'situation', 'context', 'decision', 'person', 'circumstances', 'factors', 'conditions', 'availability'],
            'upon': ['request', 'approval', 'circumstances']
        },
        
        'rely': {
            'on': ['someone', 'something', 'information', 'support', 'help', 'data', 'expertise', 'technology', 'system']
        },
        
        'listen': {
            'to': ['music', 'teacher', 'advice', 'radio', 'podcast', 'lecture', 'instructions', 'news', 'story', 'recording']
        },
        
        'look': {
            'at': ['picture', 'screen', 'person', 'book', 'document', 'photo', 'map', 'statistics', 'results'],
            'for': ['solution', 'key', 'job', 'answer', 'information', 'opportunity', 'way', 'clues', 'evidence'],
            'after': ['child', 'patient', 'pet', 'house', 'garden', 'elderly', 'belongings', 'business'],
            'forward to': ['meeting', 'event', 'holiday', 'weekend', 'celebration', 'vacation', 'results'],
            'into': ['matter', 'issue', 'problem', 'complaint', 'possibility', 'opportunity'],
            'through': ['window', 'documents', 'records', 'proposal', 'contract']
        },
        
        'wait': {
            'for': ['bus', 'train', 'reply', 'signal', 'person', 'results', 'approval', 'decision', 'opportunity']
        },
        
        'search': {
            'for': ['information', 'answer', 'meaning', 'keys', 'truth', 'solution', 'evidence', 'clues', 'opportunities']
        },
        
        'apologize': {
            'for': ['delay', 'mistake', 'rudeness', 'behavior', 'inconvenience', 'error', 'misunderstanding'],
            'to': ['person', 'teacher', 'friend', 'colleague', 'customer', 'audience']
        },
        
        'believe': {
            'in': ['truth', 'god', 'system', 'yourself', 'justice', 'equality', 'fairness', 'miracles', 'destiny']
        },
        
        'agree': {
            'with': ['idea', 'statement', 'person', 'opinion', 'perspective', 'viewpoint', 'assessment'],
            'to': ['plan', 'proposal', 'suggestion', 'terms', 'conditions', 'arrangement', 'compromise'],
            'on': ['price', 'terms', 'date', 'plan', 'strategy', 'approach', 'solution']
        },
        
        'complain': {
            'about': ['service', 'food', 'weather', 'price', 'quality', 'noise', 'delay', 'treatment', 'performance'],
            'to': ['manager', 'person', 'authority', 'supervisor', 'customer service', 'administration']
        },
        
        'talk': {
            'to': ['person', 'friend', 'teacher', 'expert', 'counselor', 'manager'],
            'with': ['person', 'colleague', 'expert', 'partner', 'team', 'family'],
            'about': ['topic', 'problem', 'issue', 'subject', 'future', 'plans', 'feelings', 'experiences']
        },
        
        'think': {
            'about': ['problem', 'future', 'idea', 'solution', 'consequences', 'possibilities', 'options'],
            'of': ['idea', 'person', 'solution', 'answer', 'way', 'method', 'approach'],
            'through': ['problem', 'situation', 'decision', 'consequences', 'implications']
        },
        
        'worry': {
            'about': ['exam', 'money', 'future', 'health', 'safety', 'family', 'career', 'results', 'performance']
        },
        
        'accuse': {
            'of': ['crime', 'theft', 'lying', 'cheating', 'murder', 'fraud', 'corruption', 'misconduct', 'negligence']
        },
        
        'blame': {
            'for': ['problem', 'accident', 'mistake', 'failure', 'delay', 'loss', 'damage'],
            'on': ['person', 'thing', 'circumstance', 'system', 'weather', 'technology']
        },
        
        'congratulate': {
            'on': ['success', 'achievement', 'birthday', 'promotion', 'graduation', 'award', 'accomplishment']
        },
        
        'succeed': {
            'in': ['exam', 'test', 'business', 'endeavor', 'project', 'mission', 'attempt', 'competition']
        },
        
        'invest': {
            'in': ['stock', 'property', 'business', 'education', 'technology', 'research', 'development', 'infrastructure']
        },
        
        'specialize': {
            'in': ['field', 'subject', 'area', 'topic', 'discipline', 'sector', 'industry', 'technology']
        },
        
        # NEW VERBS ADDED
        'apply': {
            'for': ['job', 'position', 'grant', 'loan', 'visa', 'permission', 'scholarship', 'program'],
            'to': ['university', 'college', 'company', 'institution', 'authority']
        },
        
        'consist': {
            'of': ['elements', 'components', 'parts', 'ingredients', 'materials', 'factors']
        },
        
        'contribute': {
            'to': ['project', 'discussion', 'charity', 'research', 'development', 'community', 'society']
        },
        
        'deal': {
            'with': ['problem', 'situation', 'issue', 'challenge', 'crisis', 'customer', 'complaint']
        },
        
        'focus': {
            'on': ['task', 'goal', 'objective', 'problem', 'solution', 'details', 'essentials']
        },
        
        'insist': {
            'on': ['point', 'principle', 'quality', 'standard', 'procedure', 'method']
        },
        
        'refer': {
            'to': ['document', 'manual', 'source', 'expert', 'authority', 'previous case', 'example']
        },
        
        'respond': {
            'to': ['question', 'email', 'request', 'criticism', 'situation', 'emergency', 'invitation']
        },
        
        'suffer': {
            'from': ['disease', 'illness', 'pain', 'stress', 'anxiety', 'depression', 'allergy', 'condition']
        },
        
        'translate': {
            'into': ['language', 'action', 'reality', 'practice', 'results', 'benefits']
        },

        # ADJECTIVES WITH PREPOSITIONS (Expanded)
        'interested': {
            'in': ['art', 'science', 'reading', 'technology', 'sports', 'music', 'history', 'politics', 'culture', 'travel']
        },
        
        'responsible': {
            'for': ['project', 'task', 'accident', 'team', 'work', 'department', 'budget', 'decision', 'outcome']
        },
        
        'afraid': {
            'of': ['dark', 'snakes', 'heights', 'flying', 'failure', 'rejection', 'unknown', 'consequences']
        },
        
        'proud': {
            'of': ['achievement', 'success', 'child', 'work', 'country', 'heritage', 'accomplishment', 'progress']
        },
        
        'capable': {
            'of': ['doing', 'solving', 'managing', 'learning', 'achieving', 'handling', 'completing', 'leading']
        },
        
        'different': {
            'from': ['others', 'previous', 'original', 'what', 'expected', 'usual', 'standard', 'traditional']
        },
        
        'similar': {
            'to': ['this', 'that', 'other', 'mine', 'yours', 'previous', 'original', 'standard']
        },
        
        'good': {
            'at': ['math', 'sports', 'drawing', 'cooking', 'languages', 'communication', 'analysis', 'problem-solving'],
            'for': ['health', 'you', 'environment', 'society', 'business', 'development', 'growth']
        },
        
        'bad': {
            'at': ['swimming', 'public speaking', 'math', 'sports', 'remembering', 'organizing', 'multitasking'],
            'for': ['health', 'you', 'environment', 'reputation', 'business', 'relationship']
        },
        
        'fond': {
            'of': ['music', 'chocolate', 'person', 'animals', 'reading', 'travel', 'cooking', 'gardening']
        },
        
        'tired': {
            'of': ['waiting', 'excuses', 'work', 'routine', 'politics', 'conflict', 'delays', 'inefficiency']
        },
        
        'aware': {
            'of': ['situation', 'problem', 'risk', 'danger', 'fact', 'consequences', 'implications', 'opportunity']
        },
        
        'famous': {
            'for': ['work', 'talent', 'invention', 'discovery', 'writing', 'acting', 'leadership', 'contributions']
        },
        
        'married': {
            'to': ['person', 'partner', 'spouse', 'husband', 'wife']
        },
        
        'allergic': {
            'to': ['peanuts', 'pollen', 'dust', 'cats', 'dogs', 'medication', 'shellfish', 'dairy']
        },
        
        # NEW ADJECTIVES ADDED
        'addicted': {
            'to': ['drugs', 'alcohol', 'gambling', 'shopping', 'social media', 'video games', 'sugar']
        },
        
        'angry': {
            'about': ['situation', 'decision', 'outcome', 'behavior', 'treatment'],
            'with': ['person', 'colleague', 'friend', 'family', 'authority']
        },
        
        'anxious': {
            'about': ['future', 'results', 'performance', 'health', 'safety', 'finances']
        },
        
        'committed': {
            'to': ['goal', 'project', 'relationship', 'cause', 'principle', 'excellence', 'success']
        },
        
        'compatible': {
            'with': ['system', 'software', 'device', 'person', 'partner', 'team', 'philosophy']
        },
        
        'concerned': {
            'about': ['health', 'safety', 'future', 'environment', 'economy', 'education', 'politics']
        },
        
        'connected': {
            'to': ['internet', 'network', 'system', 'person', 'community', 'organization']
        },
        
        'dependent': {
            'on': ['parents', 'technology', 'medication', 'support', 'income', 'resources']
        },
        
        'engaged': {
            'in': ['activity', 'conversation', 'project', 'research', 'discussion', 'learning']
        },
        
        'excited': {
            'about': ['trip', 'opportunity', 'news', 'event', 'future', 'possibilities']
        },
        
        'familiar': {
            'with': ['topic', 'subject', 'area', 'procedure', 'system', 'technology', 'concept']
        },
        
        'full': {
            'of': ['energy', 'ideas', 'potential', 'surprises', 'opportunities', 'challenges']
        },
        
        'guilty': {
            'of': ['crime', 'offense', 'mistake', 'negligence', 'wrongdoing', 'violation']
        },
        
        'happy': {
            'about': ['news', 'result', 'decision', 'outcome', 'achievement', 'progress']
        },
        
        'known': {
            'for': ['expertise', 'work', 'contributions', 'talent', 'innovation', 'discoveries']
        },
        
        'opposed': {
            'to': ['idea', 'plan', 'proposal', 'change', 'policy', 'decision', 'action']
        },
        
        'pleased': {
            'with': ['results', 'performance', 'progress', 'work', 'service', 'outcome']
        },
        
        'prepared': {
            'for': ['exam', 'interview', 'emergency', 'challenge', 'opportunity', 'change']
        },
        
        'satisfied': {
            'with': ['service', 'results', 'performance', 'quality', 'progress', 'outcome']
        },
        
        'suspicious': {
            'of': ['person', 'behavior', 'activity', 'intentions', 'motives', 'situation']
        },
        
        'typical': {
            'of': ['behavior', 'pattern', 'response', 'situation', 'climate', 'region']
        }
    })

    # ============================================================
    # 5. IRREGULAR VERBS (Comprehensive List)
    # ============================================================
    IRREGULAR_VERBS: dict = field(default_factory=lambda: {
        'arise': {'past': 'arose', 'pp': 'arisen', 's': 'arises'},
        'awake': {'past': 'awoke', 'pp': 'awoken', 's': 'awakes'},
        'be': {'past': 'was/were', 'pp': 'been', 's': 'is'},
        'bear': {'past': 'bore', 'pp': 'born/borne', 's': 'bears'},
        'beat': {'past': 'beat', 'pp': 'beaten', 's': 'beats'},
        'become': {'past': 'became', 'pp': 'become', 's': 'becomes'},
        'begin': {'past': 'began', 'pp': 'begun', 's': 'begins'},
        'bend': {'past': 'bent', 'pp': 'bent', 's': 'bends'},
        'bet': {'past': 'bet', 'pp': 'bet', 's': 'bets'},
        'bid': {'past': 'bid', 'pp': 'bid', 's': 'bids'},
        'bite': {'past': 'bit', 'pp': 'bitten', 's': 'bites'},
        'bleed': {'past': 'bled', 'pp': 'bled', 's': 'bleeds'},
        'blow': {'past': 'blew', 'pp': 'blown', 's': 'blows'},
        'break': {'past': 'broke', 'pp': 'broken', 's': 'breaks'},
        'bring': {'past': 'brought', 'pp': 'brought', 's': 'brings'},
        'broadcast': {'past': 'broadcast', 'pp': 'broadcast', 's': 'broadcasts'},
        'build': {'past': 'built', 'pp': 'built', 's': 'builds'},
        'burn': {'past': 'burned/burnt', 'pp': 'burned/burnt', 's': 'burns'},
        'burst': {'past': 'burst', 'pp': 'burst', 's': 'bursts'},
        'buy': {'past': 'bought', 'pp': 'bought', 's': 'buys'},
        'catch': {'past': 'caught', 'pp': 'caught', 's': 'catches'},
        'choose': {'past': 'chose', 'pp': 'chosen', 's': 'chooses'},
        'cling': {'past': 'clung', 'pp': 'clung', 's': 'clings'},
        'come': {'past': 'came', 'pp': 'come', 's': 'comes'},
        'cost': {'past': 'cost', 'pp': 'cost', 's': 'costs'},
        'creep': {'past': 'crept', 'pp': 'crept', 's': 'creeps'},
        'cut': {'past': 'cut', 'pp': 'cut', 's': 'cuts'},
        'deal': {'past': 'dealt', 'pp': 'dealt', 's': 'deals'},
        'dig': {'past': 'dug', 'pp': 'dug', 's': 'digs'},
        'dive': {'past': 'dived/dove', 'pp': 'dived', 's': 'dives'},
        'do': {'past': 'did', 'pp': 'done', 's': 'does'},
        'draw': {'past': 'drew', 'pp': 'drawn', 's': 'draws'},
        'dream': {'past': 'dreamt/dreamed', 'pp': 'dreamt/dreamed', 's': 'dreams'},
        'drink': {'past': 'drank', 'pp': 'drunk', 's': 'drinks'},
        'drive': {'past': 'drove', 'pp': 'driven', 's': 'drives'},
        'dwell': {'past': 'dwelt', 'pp': 'dwelt', 's': 'dwells'},
        'eat': {'past': 'ate', 'pp': 'eaten', 's': 'eats'},
        'fall': {'past': 'fell', 'pp': 'fallen', 's': 'falls'},
        'feed': {'past': 'fed', 'pp': 'fed', 's': 'feeds'},
        'feel': {'past': 'felt', 'pp': 'felt', 's': 'feels'},
        'fight': {'past': 'fought', 'pp': 'fought', 's': 'fights'},
        'find': {'past': 'found', 'pp': 'found', 's': 'finds'},
        'flee': {'past': 'fled', 'pp': 'fled', 's': 'flees'},
        'fling': {'past': 'flung', 'pp': 'flung', 's': 'flings'},
        'fly': {'past': 'flew', 'pp': 'flown', 's': 'flies'},
        'forbid': {'past': 'forbade', 'pp': 'forbidden', 's': 'forbids'},
        'forget': {'past': 'forgot', 'pp': 'forgotten', 's': 'forgets'},
        'forgive': {'past': 'forgave', 'pp': 'forgiven', 's': 'forgives'},
        'freeze': {'past': 'froze', 'pp': 'frozen', 's': 'freezes'},
        'get': {'past': 'got', 'pp': 'got/gotten', 's': 'gets'},
        'give': {'past': 'gave', 'pp': 'given', 's': 'gives'},
        'go': {'past': 'went', 'pp': 'gone', 's': 'goes'},
        'grind': {'past': 'ground', 'pp': 'ground', 's': 'grinds'},
        'grow': {'past': 'grew', 'pp': 'grown', 's': 'grows'},
        'hang': {'past': 'hung', 'pp': 'hung', 's': 'hangs'}, # (object)
        'have': {'past': 'had', 'pp': 'had', 's': 'has'},
        'hear': {'past': 'heard', 'pp': 'heard', 's': 'hears'},
        'hide': {'past': 'hid', 'pp': 'hidden', 's': 'hides'},
        'hit': {'past': 'hit', 'pp': 'hit', 's': 'hits'},
        'hold': {'past': 'held', 'pp': 'held', 's': 'holds'},
        'hurt': {'past': 'hurt', 'pp': 'hurt', 's': 'hurts'},
        'keep': {'past': 'kept', 'pp': 'kept', 's': 'keeps'},
        'kneel': {'past': 'knelt', 'pp': 'knelt', 's': 'kneels'},
        'know': {'past': 'knew', 'pp': 'known', 's': 'knows'},
        'lay': {'past': 'laid', 'pp': 'laid', 's': 'lays'},
        'lead': {'past': 'led', 'pp': 'led', 's': 'leads'},
        'lean': {'past': 'leaned/leant', 'pp': 'leaned/leant', 's': 'leans'},
        'leap': {'past': 'leaped/leapt', 'pp': 'leaped/leapt', 's': 'leaps'},
        'learn': {'past': 'learned/learnt', 'pp': 'learned/learnt', 's': 'learns'},
        'leave': {'past': 'left', 'pp': 'left', 's': 'leaves'},
        'lend': {'past': 'lent', 'pp': 'lent', 's': 'lends'},
        'let': {'past': 'let', 'pp': 'let', 's': 'lets'},
        'lie': {'past': 'lay', 'pp': 'lain', 's': 'lies'}, # (recline)
        'light': {'past': 'lit', 'pp': 'lit', 's': 'lights'},
        'lose': {'past': 'lost', 'pp': 'lost', 's': 'loses'},
        'make': {'past': 'made', 'pp': 'made', 's': 'makes'},
        'mean': {'past': 'meant', 'pp': 'meant', 's': 'means'},
        'meet': {'past': 'met', 'pp': 'met', 's': 'meets'},
        'pay': {'past': 'paid', 'pp': 'paid', 's': 'pays'},
        'put': {'past': 'put', 'pp': 'put', 's': 'puts'},
        'quit': {'past': 'quit', 'pp': 'quit', 's': 'quits'},
        'read': {'past': 'read', 'pp': 'read', 's': 'reads'},
        'ride': {'past': 'rode', 'pp': 'ridden', 's': 'rides'},
        'ring': {'past': 'rang', 'pp': 'rung', 's': 'rings'},
        'rise': {'past': 'rose', 'pp': 'risen', 's': 'rises'},
        'run': {'past': 'ran', 'pp': 'run', 's': 'runs'},
        'say': {'past': 'said', 'pp': 'said', 's': 'says'},
        'see': {'past': 'saw', 'pp': 'seen', 's': 'sees'},
        'seek': {'past': 'sought', 'pp': 'sought', 's': 'seeks'},
        'sell': {'past': 'sold', 'pp': 'sold', 's': 'sells'},
        'send': {'past': 'sent', 'pp': 'sent', 's': 'sends'},
        'set': {'past': 'set', 'pp': 'set', 's': 'sets'},
        'shake': {'past': 'shook', 'pp': 'shaken', 's': 'shakes'},
        'shed': {'past': 'shed', 'pp': 'shed', 's': 'sheds'},
        'shine': {'past': 'shone', 'pp': 'shone', 's': 'shines'},
        'shoot': {'past': 'shot', 'pp': 'shot', 's': 'shoots'},
        'show': {'past': 'showed', 'pp': 'shown', 's': 'shows'},
        'shrink': {'past': 'shrank', 'pp': 'shrunk', 's': 'shrinks'},
        'shut': {'past': 'shut', 'pp': 'shut', 's': 'shuts'},
        'sing': {'past': 'sang', 'pp': 'sung', 's': 'sings'},
        'sink': {'past': 'sank', 'pp': 'sunk', 's': 'sinks'},
        'sit': {'past': 'sat', 'pp': 'sat', 's': 'sits'},
        'sleep': {'past': 'slept', 'pp': 'slept', 's': 'sleeps'},
        'slide': {'past': 'slid', 'pp': 'slid', 's': 'slides'},
        'speak': {'past': 'spoke', 'pp': 'spoken', 's': 'speaks'},
        'speed': {'past': 'sped', 'pp': 'sped', 's': 'speeds'},
        'spend': {'past': 'spent', 'pp': 'spent', 's': 'spends'},
        'spin': {'past': 'spun', 'pp': 'spun', 's': 'spins'},
        'spit': {'past': 'spat', 'pp': 'spat', 's': 'spits'},
        'split': {'past': 'split', 'pp': 'split', 's': 'splits'},
        'spread': {'past': 'spread', 'pp': 'spread', 's': 'spreads'},
        'spring': {'past': 'sprang', 'pp': 'sprung', 's': 'springs'},
        'stand': {'past': 'stood', 'pp': 'stood', 's': 'stands'},
        'steal': {'past': 'stole', 'pp': 'stolen', 's': 'steals'},
        'stick': {'past': 'stuck', 'pp': 'stuck', 's': 'sticks'},
        'sting': {'past': 'stung', 'pp': 'stung', 's': 'stings'},
        'stink': {'past': 'stank', 'pp': 'stunk', 's': 'stinks'},
        'strike': {'past': 'struck', 'pp': 'struck', 's': 'strikes'},
        'swear': {'past': 'swore', 'pp': 'sworn', 's': 'swears'},
        'sweep': {'past': 'swept', 'pp': 'swept', 's': 'sweeps'},
        'swim': {'past': 'swam', 'pp': 'swum', 's': 'swims'},
        'swing': {'past': 'swung', 'pp': 'swung', 's': 'swings'},
        'take': {'past': 'took', 'pp': 'taken', 's': 'takes'},
        'teach': {'past': 'taught', 'pp': 'taught', 's': 'teaches'},
        'tear': {'past': 'tore', 'pp': 'torn', 's': 'tears'},
        'tell': {'past': 'told', 'pp': 'told', 's': 'tells'},
        'think': {'past': 'thought', 'pp': 'thought', 's': 'thinks'},
        'throw': {'past': 'threw', 'pp': 'thrown', 's': 'throws'},
        'understand': {'past': 'understood', 'pp': 'understood', 's': 'understands'},
        'wake': {'past': 'woke', 'pp': 'woken', 's': 'wakes'},
        'wear': {'past': 'wore', 'pp': 'worn', 's': 'wears'},
        'weep': {'past': 'wept', 'pp': 'wept', 's': 'weeps'},
        'win': {'past': 'won', 'pp': 'won', 's': 'wins'},
        'wind': {'past': 'wound', 'pp': 'wound', 's': 'winds'},
        'write': {'past': 'wrote', 'pp': 'written', 's': 'writes'},
    })

    # ============================================================
    # 6. AUXILIARY AND MODAL VERBS
    # ============================================================
    AUXILIARY_VERBS: dict = field(default_factory=lambda: {
        'be': {'present': ['am', 'is', 'are'], 'past': ['was', 'were'], 'pp': 'been', 'ing': 'being'},
        'have': {'present': ['have', 'has'], 'past': ['had'], 'pp': 'had', 'ing': 'having'},
        'do': {'present': ['do', 'does'], 'past': ['did'], 'pp': 'done', 'ing': 'doing'},
        'modals': ['will', 'would', 'can', 'could', 'shall', 'should', 'may', 'might', 'must']
    })
    
    SEMI_MODALS: set = field(default_factory=lambda: {
        'ought to', 'used to', 'need to', 'have to', 'has to', 'had to',
        'be able to', 'be going to', 'be supposed to', 'be about to',
        'be likely to', 'be certain to', 'be bound to'
    })

    # ============================================================
    # 7. TENSE MARKERS
    # ============================================================
    PAST_MARKERS: set = field(default_factory=lambda: {
        'yesterday', 'ago', 'last', 'previous', 'earlier', 'before', 'once', 'already', 'recently',
        'in the past', 'at that time', 'the other day', 'formerly', 'previously',
        'back then', 'in those days', 'once upon a time', 'historically'
    })
    
    PRESENT_MARKERS: set = field(default_factory=lambda: {
        'now', 'currently', 'today', 'nowadays', 'these days', 'at present', 'at the moment',
        'right now', 'as we speak', 'this week', 'this month', 'this year', 'presently',
        'currently', 'always', 'usually', 'often', 'sometimes', 'never'
    })
    
    FUTURE_MARKERS: set = field(default_factory=lambda: {
        'tomorrow', 'next', 'soon', 'later', 'eventually', 'shortly', 'in future', 'in a while',
        'in the future', 'the day after tomorrow', 'this coming week', 'by next year',
        'eventually', 'soon', 'shortly', 'in the near future', 'down the road'
    })

    # ============================================================
    # 8. FREQUENCY ADVERBS
    # ============================================================
    FREQUENCY_ADVERBS: set = field(default_factory=lambda: {
        'always', 'usually', 'often', 'frequently', 'sometimes', 'rarely', 'seldom', 'never',
        'occasionally', 'hardly ever', 'regularly', 'constantly', 'normally', 'generally',
        'daily', 'weekly', 'monthly', 'yearly', 'annually', 'every day', 'most of the time',
        'from time to time', 'once in a while', 'now and then'
    })

    # ============================================================
    # 9. CONFUSION SETS (Expanded)
    # ============================================================
    CONFUSION_SETS: dict = field(default_factory=lambda: {
        'their': ['there', "they're"],
        'there': ['their', "they're"],
        "they're": ['their', 'there'],
        'your': ["you're"],
        "you're": ['your'],
        'its': ["it's"],
        "it's": ['its'],
        'to': ['too', 'two'],
        'too': ['to', 'two'],
        'two': ['to', 'too'],
        'affect': ['effect'],
        'effect': ['affect'],
        'accept': ['except'],
        'except': ['accept'],
        'advise': ['advice'],
        'advice': ['advise'],
        'loose': ['lose'],
        'lose': ['loose'],
        'then': ['than'],
        'than': ['then'],
        'weather': ['whether'],
        'whether': ['weather'],
        'principal': ['principle'],
        'principle': ['principal'],
        'passed': ['past'],
        'past': ['passed'],
        'quiet': ['quite'],
        'quite': ['quiet'],
        'complement': ['compliment'],
        'compliment': ['complement'],
        'lead': ['led'],
        'led': ['lead'],
        'few': ['a few', 'less'],
        'little': ['a little', 'fewer'],
        'farther': ['further'],
        'further': ['farther'],
        'lay': ['lie'],
        'lie': ['lay'],
        'sit': ['set'],
        'set': ['sit'],
        'raise': ['rise'],
        'rise': ['raise'],
        'emigrate': ['immigrate'],
        'immigrate': ['emigrate']
    })

    # ============================================================
    # 10. FUNCTION WORDS
    # ============================================================
    DETERMINERS: set = field(default_factory=lambda: {
        'a', 'an', 'the', 'this', 'that', 'these', 'those',
        'my', 'your', 'his', 'her', 'its', 'our', 'their',
        'some', 'any', 'no', 'each', 'every', 'either', 'neither',
        'all', 'both', 'half', 'many', 'much', 'more', 'most', 'several',
        'few', 'little', 'a few', 'a little', 'what', 'which', 'whose',
        'enough', 'such', 'another', 'other'
    })

    CONJUNCTIONS: set = field(default_factory=lambda: {
        # Coordinating
        'and', 'but', 'or', 'so', 'yet', 'for', 'nor',
        # Subordinating
        'because', 'although', 'though', 'unless', 'while', 'whereas', 'since',
        'before', 'after', 'until', 'if', 'whether', 'as', 'than', 'that',
        'when', 'where', 'why', 'how', 'provided that', 'in case', 'so that',
        # Correlative
        'either...or', 'neither...nor', 'both...and', 'not only...but also'
    })

    PREPOSITIONS: set = field(default_factory=lambda: {
        'in', 'on', 'at', 'by', 'to', 'from', 'with', 'about', 'for', 'of',
        'through', 'under', 'over', 'between', 'among', 'into', 'onto',
        'across', 'beyond', 'during', 'without', 'within', 'above', 'below',
        'behind', 'beside', 'near', 'past', 'since', 'until', 'up', 'down', 
        'upon', 'off', 'out of', 'inside', 'outside', 'along', 'around',
        'against', 'toward', 'towards', 'regarding', 'concerning'
    })

    # ============================================================
    # 11. PRONOUNS
    # ============================================================
    PRONOUNS: dict = field(default_factory=lambda: {
        'subject': ['I', 'you', 'he', 'she', 'it', 'we', 'they'],
        'object': ['me', 'you', 'him', 'her', 'it', 'us', 'them'],
        'possessive_adj': ['my', 'your', 'his', 'her', 'its', 'our', 'their'],
        'possessive_pronoun': ['mine', 'yours', 'his', 'hers', 'its', 'ours', 'theirs'],
        'reflexive': ['myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves'],
        'relative': ['who', 'whom', 'whose', 'which', 'that', 'where', 'when', 'why'],
        'demonstrative': ['this', 'that', 'these', 'those'],
        'interrogative': ['who', 'whom', 'whose', 'which', 'what'],
        'indefinite': [
            'someone', 'anybody', 'everyone', 'everything', 'something', 'anything',
            'nobody', 'no one', 'nothing', 'everybody', 'each', 'either', 'neither',
            'one', 'all', 'some', 'any', 'many', 'few', 'several', 'both', 'other', 'another',
            'anyone', 'someone', 'everyone', 'anything', 'something', 'everything',
            'anybody', 'somebody', 'everybody', 'nobody'
        ]
    })

    # ============================================================
    # 12. DEGREE ADVERBS
    # ============================================================
    DEGREE_ADVERBS: set = field(default_factory=lambda: {
        'very', 'too', 'enough', 'quite', 'almost', 'nearly', 'barely', 'hardly',
        'extremely', 'rather', 'so', 'absolutely', 'completely', 'totally',
        'entirely', 'incredibly', 'awfully', 'just', 'only', 'really', 'slightly', 'somewhat',
        'highly', 'deeply', 'strongly', 'fully', 'perfectly', 'thoroughly'
    })
    
    # ============================================================
    # 13. IRREGULAR PLURALS
    # ============================================================
    IRREGULAR_PLURALS: dict = field(default_factory=lambda: {
        'man': 'men',
        'woman': 'women',
        'child': 'children',
        'person': 'people',
        'foot': 'feet',
        'tooth': 'teeth',
        'goose': 'geese',
        'mouse': 'mice',
        'louse': 'lice',
        'die': 'dice',
        'ox': 'oxen',
        'leaf': 'leaves',
        'wife': 'wives',
        'life': 'lives',
        'knife': 'knives',
        'wolf': 'wolves',
        'half': 'halves',
        'scarf': 'scarves',
        'elf': 'elves',
        'calf': 'calves',
        'shelf': 'shelves',
        'thief': 'thieves',
        'loaf': 'loaves',
        'cactus': 'cacti',
        'focus': 'foci',
        'fungus': 'fungi',
        'nucleus': 'nuclei',
        'syllabus': 'syllabi',
        'analysis': 'analyses',
        'basis': 'bases',
        'crisis': 'crises',
        'diagnosis': 'diagnoses',
        'oasis': 'oases',
        'thesis': 'theses',
        'hypothesis': 'hypotheses',
        'parenthesis': 'parentheses',
        'criterion': 'criteria',
        'phenomenon': 'phenomena',
        'datum': 'data',
        'medium': 'media',
        'curriculum': 'curricula',
        'bacterium': 'bacteria',
        'stratum': 'strata',
        'sheep': 'sheep',
        'fish': 'fish',
        'deer': 'deer',
        'moose': 'moose',
        'aircraft': 'aircraft',
        'species': 'species',
        'series': 'series',
        'means': 'means',
        'offspring': 'offspring'
    })

    # ============================================================
    # 14. COMMON PHRASAL VERBS
    # ============================================================
    PHRASAL_VERBS: dict = field(default_factory=lambda: {
        'get': ['up', 'on', 'off', 'over', 'along', 'away', 'back', 'by', 'down', 'through', 'out', 'in'],
        'put': ['off', 'on', 'up', 'down', 'away', 'out', 'through', 'up with'],
        'take': ['off', 'on', 'after', 'up', 'over', 'down', 'back', 'out', 'in'],
        'look': ['up', 'down', 'for', 'after', 'into', 'forward to', 'out', 'over', 'through'],
        'go': ['on', 'off', 'out', 'over', 'through', 'back', 'ahead', 'with', 'against'],
        'make': ['up', 'out', 'for', 'off', 'do with'],
        'give': ['up', 'in', 'away', 'back', 'out', 'off'],
        'break': ['up', 'down', 'in', 'out', 'through', 'off', 'away'],
        'call': ['off', 'on', 'up', 'back', 'for', 'out'],
        'turn': ['on', 'off', 'up', 'down', 'into', 'out', 'around'],
        'run': ['out', 'into', 'over', 'away', 'through', 'across'],
        'come': ['across', 'up', 'down', 'over', 'through', 'back', 'along'],
        'set': ['up', 'off', 'out', 'about', 'aside'],
        'bring': ['up', 'about', 'out', 'down', 'back', 'along'],
        'carry': ['on', 'out', 'over', 'through'],
        'hold': ['on', 'up', 'back', 'out', 'off'],
        'keep': ['on', 'up', 'down', 'away', 'back', 'off'],
        'let': ['down', 'in', 'out', 'off', 'up'],
        'pick': ['up', 'out', 'on', 'off'],
        'show': ['up', 'off', 'around'],
        'work': ['out', 'on', 'up', 'through'],
        'stand': ['up', 'out', 'for', 'by'],
    })

    # ============================================================
    # 15. COMMON IDIOMS AND EXPRESSIONS
    # ============================================================
    COMMON_IDIOMS: set = field(default_factory=lambda: {
        'piece of cake', 'break a leg', 'hit the nail on the head', 'bite the bullet',
        'cost an arm and a leg', 'cut corners', 'get out of hand', 'go the extra mile',
        'hang in there', 'in a nutshell', 'kill two birds with one stone', 'let the cat out of the bag',
        'miss the boat', 'once in a blue moon', 'pull someone\'s leg', 'speak of the devil',
        'the ball is in your court', 'the best of both worlds', 'under the weather',
        'burn the midnight oil', 'caught between two stools', 'see eye to eye', 'hear it on the grapevine'
    })

    # ============================================================
    # 16. COMMON COLLOCATIONS
    # ============================================================
    COMMON_COLLOCATIONS: dict = field(default_factory=lambda: {
        'make': ['decision', 'mistake', 'progress', 'money', 'effort', 'plan', 'change'],
        'do': ['homework', 'business', 'exercise', 'research', 'favor', 'damage'],
        'take': ['photo', 'shower', 'break', 'chance', 'risk', 'time', 'care'],
        'have': ['breakfast', 'lunch', 'dinner', 'party', 'meeting', 'idea', 'problem'],
        'break': ['law', 'rule', 'promise', 'record', 'news'],
        'catch': ['bus', 'train', 'flight', 'cold', 'thief'],
        'pay': ['attention', 'bill', 'price', 'respect'],
        'keep': ['secret', 'promise', 'peace', 'record'],
        'save': ['time', 'money', 'energy', 'life'],
        'lose': ['weight', 'money', 'time', 'patience'],
        'win': ['prize', 'game', 'race', 'election'],
        'strong': ['coffee', 'wind', 'feeling', 'argument'],
        'heavy': ['rain', 'traffic', 'smoker', 'bag'],
        'light': ['rain', 'traffic', 'breeze', 'meal']
    })

    # ============================================================
    # 17. COMMON SYNTAX PATTERNS
    # ============================================================
    SYNTAX_PATTERNS: dict = field(default_factory=lambda: {
        'question_words': ['what', 'when', 'where', 'why', 'how', 'which', 'who', 'whom'],
        'comparative_adj': ['better', 'worse', 'bigger', 'smaller', 'faster', 'slower'],
        'superlative_adj': ['best', 'worst', 'biggest', 'smallest', 'fastest', 'slowest'],
        'time_expressions': ['always', 'never', 'often', 'sometimes', 'usually', 'rarely'],
        'place_expressions': ['here', 'there', 'everywhere', 'anywhere', 'somewhere', 'nowhere']
    })

    # ============================================================
    # 18. COMMON SPELLING MISTAKES
    # ============================================================
    COMMON_MISSPELLINGS: dict = field(default_factory=lambda: {
        'accommodate': ['acommodate', 'accomodate'],
        'achieve': ['acheive'],
        'argument': ['arguement'],
        'beginning': ['begining'],
        'believe': ['beleive'],
        'calendar': ['calender'],
        'category': ['catagory'],
        'cemetery': ['cemetary'],
        'conscience': ['concience'],
        'conscious': ['concious'],
        'definite': ['definate'],
        'embarrass': ['embarass'],
        'environment': ['enviroment'],
        'existence': ['existance'],
        'foreign': ['foriegn'],
        'government': ['goverment'],
        'grammar': ['grammer'],
        'guarantee': ['garantee'],
        'harass': ['harrass'],
        'immediately': ['immediatly'],
        'independent': ['independant'],
        'intelligence': ['inteligence'],
        'judgment': ['judgement'],
        'knowledge': ['knowlage'],
        'library': ['libary'],
        'license': ['licence'],
        'maintenance': ['maintainance'],
        'necessary': ['neccessary'],
        'occasion': ['occassion'],
        'occurred': ['occured'],
        'privilege': ['priviledge'],
        'receive': ['recieve'],
        'recommend': ['recomend'],
        'restaurant': ['restaraunt'],
        'separate': ['seperate'],
        'successful': ['sucessful'],
        'until': ['untill'],
        'weird': ['wierd']
    })

    # ============================================================
    # 19. FORMAL VS INFORMAL EXPRESSIONS
    # ============================================================
    FORMAL_INFORMAL: dict = field(default_factory=lambda: {
        'kids': 'children',
        'guy': 'man',
        'stuff': 'things',
        'a lot of': 'many',
        'tons of': 'many',
        'get': 'obtain',
        'buy': 'purchase',
        'start': 'commence',
        'end': 'conclude',
        'show': 'demonstrate',
        'tell': 'inform',
        'ask': 'inquire',
        'help': 'assist',
        'need': 'require',
        'want': 'desire',
        'try': 'attempt',
        'use': 'utilize',
        'make sure': 'ensure',
        'find out': 'discover',
        'go up': 'increase',
        'go down': 'decrease',
        'put off': 'postpone',
        'deal with': 'handle'
    })

    # ============================================================
    # 20. COMMON CONTRACTIONS
    # ============================================================
    CONTRACTIONS: dict = field(default_factory=lambda: {
        "i'm": "i am",
        "you're": "you are",
        "he's": "he is",
        "she's": "she is",
        "it's": "it is",
        "we're": "we are",
        "they're": "they are",
        "i've": "i have",
        "you've": "you have",
        "we've": "we have",
        "they've": "they have",
        "i'll": "i will",
        "you'll": "you will",
        "he'll": "he will",
        "she'll": "she will",
        "it'll": "it will",
        "we'll": "we will",
        "they'll": "they will",
        "i'd": "i would",
        "you'd": "you would",
        "he'd": "he would",
        "she'd": "she would",
        "it'd": "it would",
        "we'd": "we would",
        "they'd": "they would",
        "isn't": "is not",
        "aren't": "are not",
        "wasn't": "was not",
        "weren't": "were not",
        "haven't": "have not",
        "hasn't": "has not",
        "hadn't": "had not",
        "won't": "will not",
        "wouldn't": "would not",
        "don't": "do not",
        "doesn't": "does not",
        "didn't": "did not",
        "can't": "cannot",
        "couldn't": "could not",
        "shouldn't": "should not",
        "mightn't": "might not",
        "mustn't": "must not"
    })