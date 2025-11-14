# from dataclasses import dataclass, field


# @dataclass
# class LinguisticKnowledge:
#     """Extensive linguistic knowledge base for context-aware grammar correction."""

#     # ============================================================
#     # 1. ZERO ARTICLE NOUNS (Used without 'a/an/the')
#     # ============================================================
#     ZERO_ARTICLE_NOUNS: set = field(default_factory=lambda: {
#         'school', 'college', 'university', 'church', 'hospital', 'prison', 'court', 'bed',
#         'home', 'work', 'town', 'sea', 'camp', 'class', 'market', 'office', 'parliament',
#         'breakfast', 'lunch', 'dinner', 'supper', 'brunch',
#         'football', 'cricket', 'tennis', 'basketball', 'soccer', 'chess', 'golf', 'rugby',
#         'mathematics', 'physics', 'chemistry', 'biology', 'history', 'geography', 'economics',
#         'english', 'french', 'art', 'music', 'literature', 'philosophy', 'poetry', 'politics'
#     })

#     # ============================================================
#     # 2. UNCOUNTABLE NOUNS
#     # ============================================================
#     UNCOUNTABLE: set = field(default_factory=lambda: {
#         'advice', 'information', 'knowledge', 'research', 'evidence', 'progress',
#         'furniture', 'equipment', 'luggage', 'baggage', 'homework', 'housework',
#         'weather', 'traffic', 'news', 'software', 'hardware', 'work',
#         'water', 'milk', 'coffee', 'tea', 'juice', 'rice', 'bread', 'butter', 'sugar',
#         'money', 'cash', 'gold', 'silver', 'oil', 'electricity', 'energy', 'gas',
#         'happiness', 'sadness', 'anger', 'love', 'hate', 'fear', 'peace', 'freedom', 'health',
#         'education', 'transportation', 'employment', 'poverty', 'wealth'
#     })

#     # ============================================================
#     # 3. DEFINITE ARTICLE NOUNS (Usually require 'the')
#     # ============================================================
#     DEFINITE_ARTICLE_NOUNS: set = field(default_factory=lambda: {
#         'sun', 'moon', 'earth', 'sky', 'internet', 'president', 'prime minister', 'world',
#         'government', 'universe', 'climate', 'economy', 'police', 'army', 'media'
#     })

#     # ============================================================
#     # 4. PREPOSITION COLLOCATIONS
#     # ============================================================
#     PREPOSITION_COLLOCATIONS: dict = field(default_factory=lambda: {
#         'go': {'to': ['school', 'work', 'bed', 'church', 'market', 'hospital', 'gym', 'university']},
#         'arrive': {'at': ['station', 'airport', 'school', 'work'], 'in': ['city', 'country', 'town']},
#         'participate': {'in': ['event', 'meeting', 'competition', 'conference']},
#         'depend': {'on': ['weather', 'situation', 'context', 'decision']},
#         'listen': {'to': ['music', 'teacher', 'advice', 'radio']},
#         'look': {'at': ['picture', 'screen'], 'for': ['solution', 'key', 'job'], 'after': ['child', 'patient']},
#         'wait': {'for': ['bus', 'train', 'reply', 'signal']},
#         'search': {'for': ['information', 'answer', 'meaning']},
#         'apologize': {'for': ['delay', 'mistake', 'rudeness']},
#         'believe': {'in': ['truth', 'god', 'system', 'yourself']},
#         'agree': {'with': ['idea', 'statement', 'person'], 'to': ['plan', 'proposal']},
#         'interested': {'in': ['art', 'science', 'reading', 'technology']},
#         'responsible': {'for': ['project', 'task', 'accident', 'team']},
#         'afraid': {'of': ['dark', 'snakes', 'heights']},
#         'proud': {'of': ['achievement', 'success', 'child']},
#         'capable': {'of': ['doing', 'solving', 'managing']},
#         'different': {'from': ['others', 'previous', 'original']},
#         'similar': {'to': ['this', 'that', 'other']}
#     })

#     # ============================================================
#     # 5. IRREGULAR VERBS (Comprehensive List)
#     # ============================================================
#     IRREGULAR_VERBS: dict = field(default_factory=lambda: {
#         'be': {'past': 'was/were', 'pp': 'been', 's': 'is'},
#         'have': {'past': 'had', 'pp': 'had', 's': 'has'},
#         'do': {'past': 'did', 'pp': 'done', 's': 'does'},
#         'go': {'past': 'went', 'pp': 'gone', 's': 'goes'},
#         'see': {'past': 'saw', 'pp': 'seen', 's': 'sees'},
#         'take': {'past': 'took', 'pp': 'taken', 's': 'takes'},
#         'eat': {'past': 'ate', 'pp': 'eaten', 's': 'eats'},
#         'come': {'past': 'came', 'pp': 'come', 's': 'comes'},
#         'get': {'past': 'got', 'pp': 'got/gotten', 's': 'gets'},
#         'make': {'past': 'made', 'pp': 'made', 's': 'makes'},
#         'write': {'past': 'wrote', 'pp': 'written', 's': 'writes'},
#         'speak': {'past': 'spoke', 'pp': 'spoken', 's': 'speaks'},
#         'break': {'past': 'broke', 'pp': 'broken', 's': 'breaks'},
#         'fly': {'past': 'flew', 'pp': 'flown', 's': 'flies'},
#         'begin': {'past': 'began', 'pp': 'begun', 's': 'begins'},
#         'run': {'past': 'ran', 'pp': 'run', 's': 'runs'},
#         'buy': {'past': 'bought', 'pp': 'bought', 's': 'buys'},
#         'bring': {'past': 'brought', 'pp': 'brought', 's': 'brings'},
#         'teach': {'past': 'taught', 'pp': 'taught', 's': 'teaches'},
#         'feel': {'past': 'felt', 'pp': 'felt', 's': 'feels'},
#         'find': {'past': 'found', 'pp': 'found', 's': 'finds'},
#         'think': {'past': 'thought', 'pp': 'thought', 's': 'thinks'},
#         'sell': {'past': 'sold', 'pp': 'sold', 's': 'sells'},
#         'tell': {'past': 'told', 'pp': 'told', 's': 'tells'},
#         'sit': {'past': 'sat', 'pp': 'sat', 's': 'sits'},
#         'stand': {'past': 'stood', 'pp': 'stood', 's': 'stands'},
#         'sleep': {'past': 'slept', 'pp': 'slept', 's': 'sleeps'},
#         'choose': {'past': 'chose', 'pp': 'chosen', 's': 'chooses'},
#     })

#     # ============================================================
#     # 6. AUXILIARY AND MODAL VERBS
#     # ============================================================
#     AUXILIARY_VERBS: dict = field(default_factory=lambda: {
#         'be': {'present': ['am', 'is', 'are'], 'past': ['was', 'were']},
#         'have': {'present': ['have', 'has'], 'past': ['had']},
#         'do': {'present': ['do', 'does'], 'past': ['did']},
#         'modals': ['will', 'would', 'can', 'could', 'shall', 'should', 'may', 'might', 'must']
#     })

#     # ============================================================
#     # 7. TENSE MARKERS
#     # ============================================================
#     PAST_MARKERS: set = field(default_factory=lambda: {
#         'yesterday', 'ago', 'last', 'previous', 'earlier', 'before', 'once', 'already', 'recently'
#     })
#     PRESENT_MARKERS: set = field(default_factory=lambda: {
#         'now', 'currently', 'today', 'nowadays', 'these days', 'at present', 'at the moment'
#     })
#     FUTURE_MARKERS: set = field(default_factory=lambda: {
#         'tomorrow', 'next', 'soon', 'later', 'eventually', 'shortly', 'in future', 'in a while'
#     })

#     # ============================================================
#     # 8. FREQUENCY ADVERBS
#     # ============================================================
#     FREQUENCY_ADVERBS: set = field(default_factory=lambda: {
#         'always', 'usually', 'often', 'frequently', 'sometimes', 'rarely', 'seldom', 'never',
#         'occasionally', 'hardly ever', 'regularly', 'constantly', 'daily', 'weekly'
#     })

#     # ============================================================
#     # 9. CONFUSION SETS
#     # ============================================================
#     CONFUSION_SETS: dict = field(default_factory=lambda: {
#         'their': ['there', "they're"],
#         'there': ['their', "they're"],
#         "they're": ['their', 'there'],
#         'your': ["you're"],
#         "you're": ['your'],
#         'its': ["it's"],
#         "it's": ['its'],
#         'affect': ['effect'],
#         'effect': ['affect'],
#         'accept': ['except'],
#         'advise': ['advice'],
#         'loose': ['lose'],
#         'then': ['than'],
#         'few': ['a few'],
#         'little': ['a little']
#     })

#     # ============================================================
#     # 10. FUNCTION WORDS (Useful for POS and Syntax)
#     # ============================================================
#     DETERMINERS: set = field(default_factory=lambda: {
#         'a', 'an', 'the', 'this', 'that', 'these', 'those', 'my', 'your', 'his',
#         'her', 'its', 'our', 'their', 'some', 'any', 'no', 'each', 'every', 'either', 'neither'
#     })

#     CONJUNCTIONS: set = field(default_factory=lambda: {
#         'and', 'but', 'or', 'so', 'yet', 'because', 'although', 'though', 'unless', 'while', 'whereas', 'since', 'before', 'after', 'until'
#     })

#     PREPOSITIONS: set = field(default_factory=lambda: {
#         'in', 'on', 'at', 'by', 'to', 'from', 'with', 'about', 'for', 'of', 'through', 'under', 'over',
#         'between', 'among', 'into', 'onto', 'across', 'beyond', 'during', 'without', 'within'
#     })

#     # ============================================================
#     # 11. PRONOUNS
#     # ============================================================
#     PRONOUNS: dict = field(default_factory=lambda: {
#         'subject': ['I', 'you', 'he', 'she', 'it', 'we', 'they'],
#         'object': ['me', 'you', 'him', 'her', 'it', 'us', 'them'],
#         'possessive': ['my', 'your', 'his', 'her', 'its', 'our', 'their'],
#         'reflexive': ['myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves'],
#         'relative': ['who', 'whom', 'whose', 'which', 'that'],
#         'demonstrative': ['this', 'that', 'these', 'those']
#     })

#     # ============================================================
#     # 12. DEGREE ADVERBS
#     # ============================================================
#     DEGREE_ADVERBS: set = field(default_factory=lambda: {
#         'very', 'too', 'enough', 'quite', 'almost', 'nearly', 'barely', 'hardly', 'extremely', 'rather', 'so'
#     })


# # Example usage:
# # knowledge = LinguisticKnowledge()
# # print(knowledge.IRREGULAR_VERBS['go']['past'])  # Output: went
from dataclasses import dataclass, field


@dataclass
class LinguisticKnowledge:
    """Extensive linguistic knowledge base for context-aware grammar correction."""

    # ============================================================
    # 1. ZERO ARTICLE NOUNS (Used without 'a/an/the' in certain contexts)
    # ============================================================
    ZERO_ARTICLE_NOUNS: set = field(default_factory=lambda: {
        # Institutions
        'school', 'college', 'university', 'church', 'hospital', 'prison', 'court', 'jail',
        'camp', 'class', 'office', 'parliament',
        
        # Location / Abstract
        'home', 'work', 'town', 'sea', 'nature', 'space', 'society', 'heaven', 'hell',
        'life', 'death', 'paradise',

        # Meals
        'breakfast', 'lunch', 'dinner', 'supper', 'brunch', 'tea',

        # Sports
        'football', 'cricket', 'tennis', 'basketball', 'soccer', 'chess', 'golf', 'rugby',
        'baseball', 'hockey', 'volleyball', 'badminton', 'boxing', 'wrestling',

        # Subjects / Fields
        'mathematics', 'physics', 'chemistry', 'biology', 'history', 'geography', 'economics',
        'english', 'french', 'art', 'music', 'literature', 'philosophy', 'poetry', 'politics',
        'linguistics', 'psychology', 'sociology', 'engineering', 'medicine', 'law',

        # Time
        'night', 'day', 'noon', 'midnight', 'dawn', 'dusk'
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
        'access', 'data', 'software', 'hardware',

        # Categories
        'furniture', 'equipment', 'luggage', 'baggage', 'homework', 'housework', 'work',
        'money', 'cash', 'currency', 'mail', 'postage', 'scenery', 'poetry', 'music', 'art',
        'clothing', 'machinery', 'garbage', 'rubbish', 'trash',

        # Substances / Materials
        'water', 'milk', 'coffee', 'tea', 'juice', 'wine', 'beer', 'blood',
        'rice', 'bread', 'butter', 'sugar', 'salt', 'pepper', 'flour', 'cheese', 'meat', 'pasta',
        'gold', 'silver', 'oil', 'electricity', 'energy', 'gas', 'air', 'oxygen',
        'cotton', 'wood', 'plastic', 'steel', 'sand', 'chalk', 'soap',

        # General
        'weather', 'traffic', 'news', 'transportation', 'accommodation'
    })

    # ============================================================
    # 3. DEFINITE ARTICLE NOUNS (Usually require 'the')
    # ============================================================
    DEFINITE_ARTICLE_NOUNS: set = field(default_factory=lambda: {
        # Unique Entities
        'sun', 'moon', 'earth', 'sky', 'internet', 'world', 'universe',
        'equator', 'north pole', 'south pole', 'horizon',

        # Roles / Titles
        'president', 'prime minister', 'pope', 'king', 'queen', 'ceo',

        # Groups / Institutions
        'government', 'police', 'army', 'navy', 'air force', 'media', 'press', 'judiciary',

        # Concepts
        'climate', 'economy', 'environment', 'atmosphere', 'past', 'present', 'future', 'ocean'
    })

    # ============================================================
    # 4. PREPOSITION COLLOCATIONS
    # ============================================================
    PREPOSITION_COLLOCATIONS: dict = field(default_factory=lambda: {
        # Verbs
        'go': {'to': ['school', 'work', 'bed', 'church', 'market', 'hospital', 'gym', 'university']},
        'arrive': {'at': ['station', 'airport', 'school', 'work'], 'in': ['city', 'country', 'town']},
        'participate': {'in': ['event', 'meeting', 'competition', 'conference']},
        'depend': {'on': ['weather', 'situation', 'context', 'decision', 'person']},
        'rely': {'on': ['someone', 'something', 'information']},
        'listen': {'to': ['music', 'teacher', 'advice', 'radio', 'podcast']},
        'look': {'at': ['picture', 'screen', 'person'], 'for': ['solution', 'key', 'job'], 'after': ['child', 'patient', 'pet']},
        'wait': {'for': ['bus', 'train', 'reply', 'signal', 'person']},
        'search': {'for': ['information', 'answer', 'meaning', 'keys']},
        'apologize': {'for': ['delay', 'mistake', 'rudeness'], 'to': ['person']},
        'believe': {'in': ['truth', 'god', 'system', 'yourself']},
        'agree': {'with': ['idea', 'statement', 'person'], 'to': ['plan', 'proposal'], 'on': ['price', 'terms']},
        'complain': {'about': ['service', 'food', 'weather'], 'to': ['manager', 'person']},
        'talk': {'to': ['person'], 'with': ['person'], 'about': ['topic', 'problem']},
        'think': {'about': ['problem', 'future'], 'of': ['idea', 'person']},
        'worry': {'about': ['exam', 'money', 'future']},
        'accuse': {'of': ['crime', 'theft', 'lying']},
        'blame': {'for': ['problem', 'accident'], 'on': ['person', 'thing']},
        'congratulate': {'on': ['success', 'achievement', 'birthday']},

        # Adjectives
        'interested': {'in': ['art', 'science', 'reading', 'technology', 'sports']},
        'responsible': {'for': ['project', 'task', 'accident', 'team']},
        'afraid': {'of': ['dark', 'snakes', 'heights', 'flying']},
        'proud': {'of': ['achievement', 'success', 'child', 'work']},
        'capable': {'of': ['doing', 'solving', 'managing', 'learning']},
        'different': {'from': ['others', 'previous', 'original', 'what']},
        'similar': {'to': ['this', 'that', 'other', 'mine']},
        'good': {'at': ['math', 'sports', 'drawing'], 'for': ['health', 'you']},
        'bad': {'at': ['swimming', 'public speaking'], 'for': ['health', 'you']},
        'fond': {'of': ['music', 'chocolate', 'person']},
        'tired': {'of': ['waiting', 'excuses', 'work']},
        'aware': {'of': ['situation', 'problem', 'risk']},
        'famous': {'for': ['work', 'talent', 'invention']}
    })

    # ============================================================
    # 5. IRREGULAR VERBS (Comprehensive List)
    # ============================================================
    # 's' form is the 3rd person singular present (he/she/it)
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
        'bite': {'past': 'bit', 'pp': 'bitten', 's': 'bites'},
        'bleed': {'past': 'bled', 'pp': 'bled', 's': 'bleeds'},
        'blow': {'past': 'blew', 'pp': 'blown', 's': 'blows'},
        'break': {'past': 'broke', 'pp': 'broken', 's': 'breaks'},
        'bring': {'past': 'brought', 'pp': 'brought', 's': 'brings'},
        'broadcast': {'past': 'broadcast', 'pp': 'broadcast', 's': 'broadcasts'},
        'build': {'past': 'built', 'pp': 'built', 's': 'builds'},
        'buy': {'past': 'bought', 'pp': 'bought', 's': 'buys'},
        'catch': {'past': 'caught', 'pp': 'caught', 's': 'catches'},
        'choose': {'past': 'chose', 'pp': 'chosen', 's': 'chooses'},
        'come': {'past': 'came', 'pp': 'come', 's': 'comes'},
        'cost': {'past': 'cost', 'pp': 'cost', 's': 'costs'},
        'cut': {'past': 'cut', 'pp': 'cut', 's': 'cuts'},
        'deal': {'past': 'dealt', 'pp': 'dealt', 's': 'deals'},
        'dig': {'past': 'dug', 'pp': 'dug', 's': 'digs'},
        'do': {'past': 'did', 'pp': 'done', 's': 'does'},
        'draw': {'past': 'drew', 'pp': 'drawn', 's': 'draws'},
        'dream': {'past': 'dreamt/dreamed', 'pp': 'dreamt/dreamed', 's': 'dreams'},
        'drink': {'past': 'drank', 'pp': 'drunk', 's': 'drinks'},
        'drive': {'past': 'drove', 'pp': 'driven', 's': 'drives'},
        'eat': {'past': 'ate', 'pp': 'eaten', 's': 'eats'},
        'fall': {'past': 'fell', 'pp': 'fallen', 's': 'falls'},
        'feed': {'past': 'fed', 'pp': 'fed', 's': 'feeds'},
        'feel': {'past': 'felt', 'pp': 'felt', 's': 'feels'},
        'fight': {'past': 'fought', 'pp': 'fought', 's': 'fights'},
        'find': {'past': 'found', 'pp': 'found', 's': 'finds'},
        'flee': {'past': 'fled', 'pp': 'fled', 's': 'flees'},
        'fly': {'past': 'flew', 'pp': 'flown', 's': 'flies'},
        'forget': {'past': 'forgot', 'pp': 'forgotten', 's': 'forgets'},
        'forgive': {'past': 'forgave', 'pp': 'forgiven', 's': 'forgives'},
        'freeze': {'past': 'froze', 'pp': 'frozen', 's': 'freezes'},
        'get': {'past': 'got', 'pp': 'got/gotten', 's': 'gets'},
        'give': {'past': 'gave', 'pp': 'given', 's': 'gives'},
        'go': {'past': 'went', 'pp': 'gone', 's': 'goes'},
        'grow': {'past': 'grew', 'pp': 'grown', 's': 'grows'},
        'hang': {'past': 'hung', 'pp': 'hung', 's': 'hangs'}, # (object)
        'have': {'past': 'had', 'pp': 'had', 's': 'has'},
        'hear': {'past': 'heard', 'pp': 'heard', 's': 'hears'},
        'hide': {'past': 'hid', 'pp': 'hidden', 's': 'hides'},
        'hit': {'past': 'hit', 'pp': 'hit', 's': 'hits'},
        'hold': {'past': 'held', 'pp': 'held', 's': 'holds'},
        'hurt': {'past': 'hurt', 'pp': 'hurt', 's': 'hurts'},
        'keep': {'past': 'kept', 'pp': 'kept', 's': 'keeps'},
        'know': {'past': 'knew', 'pp': 'known', 's': 'knows'},
        'lay': {'past': 'laid', 'pp': 'laid', 's': 'lays'},
        'lead': {'past': 'led', 'pp': 'led', 's': 'leads'},
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
        'shine': {'past': 'shone', 'pp': 'shone', 's': 'shines'},
        'shoot': {'past': 'shot', 'pp': 'shot', 's': 'shoots'},
        'show': {'past': 'showed', 'pp': 'shown', 's': 'shows'},
        'shut': {'past': 'shut', 'pp': 'shut', 's': 'shuts'},
        'sing': {'past': 'sang', 'pp': 'sung', 's': 'sings'},
        'sink': {'past': 'sank', 'pp': 'sunk', 's': 'sinks'},
        'sit': {'past': 'sat', 'pp': 'sat', 's': 'sits'},
        'sleep': {'past': 'slept', 'pp': 'slept', 's': 'sleeps'},
        'speak': {'past': 'spoke', 'pp': 'spoken', 's': 'speaks'},
        'spend': {'past': 'spent', 'pp': 'spent', 's': 'spends'},
        'spread': {'past': 'spread', 'pp': 'spread', 's': 'spreads'},
        'stand': {'past': 'stood', 'pp': 'stood', 's': 'stands'},
        'steal': {'past': 'stole', 'pp': 'stolen', 's': 'steals'},
        'stick': {'past': 'stuck', 'pp': 'stuck', 's': 'sticks'},
        'swim': {'past': 'swam', 'pp': 'swum', 's': 'swims'},
        'take': {'past': 'took', 'pp': 'taken', 's': 'takes'},
        'teach': {'past': 'taught', 'pp': 'taught', 's': 'teaches'},
        'tear': {'past': 'tore', 'pp': 'torn', 's': 'tears'},
        'tell': {'past': 'told', 'pp': 'told', 's': 'tells'},
        'think': {'past': 'thought', 'pp': 'thought', 's': 'thinks'},
        'throw': {'past': 'threw', 'pp': 'thrown', 's': 'throws'},
        'understand': {'past': 'understood', 'pp': 'understood', 's': 'understands'},
        'wake': {'past': 'woke', 'pp': 'woken', 's': 'wakes'},
        'wear': {'past': 'wore', 'pp': 'worn', 's': 'wears'},
        'win': {'past': 'won', 'pp': 'won', 's': 'wins'},
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
    
    # NEW CATEGORY
    SEMI_MODALS: set = field(default_factory=lambda: {
        'ought to', 'used to', 'need to', 'have to', 'has to', 'had to',
        'be able to', 'be going to', 'be supposed to'
    })

    # ============================================================
    # 7. TENSE MARKERS
    # ============================================================
    PAST_MARKERS: set = field(default_factory=lambda: {
        'yesterday', 'ago', 'last', 'previous', 'earlier', 'before', 'once', 'already', 'recently',
        'in the past', 'at that time', 'the other day', 'formerly'
    })
    PRESENT_MARKERS: set = field(default_factory=lambda: {
        'now', 'currently', 'today', 'nowadays', 'these days', 'at present', 'at the moment',
        'right now', 'as we speak', 'this week', 'this month'
    })
    FUTURE_MARKERS: set = field(default_factory=lambda: {
        'tomorrow', 'next', 'soon', 'later', 'eventually', 'shortly', 'in future', 'in a while',
        'in the future', 'the day after tomorrow', 'this coming week', 'by next year'
    })

    # ============================================================
    # 8. FREQUENCY ADVERBS
    # ============================================================
    FREQUENCY_ADVERBS: set = field(default_factory=lambda: {
        'always', 'usually', 'often', 'frequently', 'sometimes', 'rarely', 'seldom', 'never',
        'occasionally', 'hardly ever', 'regularly', 'constantly', 'normally', 'generally',
        'daily', 'weekly', 'monthly', 'yearly', 'annually', 'every day'
    })

    # ============================================================
    # 9. CONFUSION SETS
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
        'lead': ['led'], # (leed vs led)
        'led': ['lead'],
        'few': ['a few', 'less'],
        'little': ['a little', 'fewer']
    })

    # ============================================================
    # 10. FUNCTION WORDS (Useful for POS and Syntax)
    # ============================================================
    DETERMINERS: set = field(default_factory=lambda: {
        'a', 'an', 'the', 'this', 'that', 'these', 'those',
        'my', 'your', 'his', 'her', 'its', 'our', 'their',
        'some', 'any', 'no', 'each', 'every', 'either', 'neither',
        'all', 'both', 'half', 'many', 'much', 'more', 'most', 'several',
        'few', 'little', 'a few', 'a little', 'what', 'which', 'whose'
    })

    CONJUNCTIONS: set = field(default_factory=lambda: {
        # Coordinating
        'and', 'but', 'or', 'so', 'yet', 'for', 'nor',
        # Subordinating
        'because', 'although', 'though', 'unless', 'while', 'whereas', 'since',
        'before', 'after', 'until', 'if', 'whether', 'as', 'than', 'that',
        'when', 'where', 'why', 'how'
    })

    PREPOSITIONS: set = field(default_factory=lambda: {
        'in', 'on', 'at', 'by', 'to', 'from', 'with', 'about', 'for', 'of',
        'through', 'under', 'over', 'between', 'among', 'into', 'onto',
        'across', 'beyond', 'during', 'without', 'within', 'above', 'below',
        'behind', 'beside', 'near', 'past', 'since', 'until', 'up', 'down', 'upon', 'off', 'out of'
    })

    # ============================================================
    # 11. PRONOUNS (Restructured for clarity)
    # ============================================================
    PRONOUNS: dict = field(default_factory=lambda: {
        'subject': ['I', 'you', 'he', 'she', 'it', 'we', 'they'],
        'object': ['me', 'you', 'him', 'her', 'it', 'us', 'them'],
        'possessive_adj': ['my', 'your', 'his', 'her', 'its', 'our', 'their'], # (Determiners)
        'possessive_pronoun': ['mine', 'yours', 'his', 'hers', 'its', 'ours', 'theirs'], # (Stand-alone)
        'reflexive': ['myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves'],
        'relative': ['who', 'whom', 'whose', 'which', 'that', 'where', 'when'],
        'demonstrative': ['this', 'that', 'these', 'those'],
        'interrogative': ['who', 'whom', 'whose', 'which', 'what'],
        'indefinite': [
            'someone', 'anybody', 'everyone', 'everything', 'something', 'anything',
            'nobody', 'no one', 'nothing', 'everybody', 'each', 'either', 'neither',
            'one', 'all', 'some', 'any', 'many', 'few', 'several', 'both', 'other', 'another'
        ]
    })

    # ============================================================
    # 12. DEGREE ADVERBS
    # ============================================================
    DEGREE_ADVERBS: set = field(default_factory=lambda: {
        'very', 'too', 'enough', 'quite', 'almost', 'nearly', 'barely', 'hardly',
        'extremely', 'rather', 'so', 'absolutely', 'completely', 'totally',
        'entirely', 'incredibly', 'awfully', 'just', 'only', 'really', 'slightly', 'somewhat'
    })
    
    # ============================================================
    # 13. IRREGULAR PLURALS (NEW CATEGORY)
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
        'criterion': 'criteria',
        'phenomenon': 'phenomena',
        'datum': 'data',
        'medium': 'media',
        'curriculum': 'curricula',
        'sheep': 'sheep',
        'fish': 'fish', # (or fishes)
        'deer': 'deer',
        'moose': 'moose',
        'aircraft': 'aircraft',
        'species': 'species',
        'series': 'series',
    })

    # ============================================================
    # 14. COMMON PHRASAL VERBS (NEW CATEGORY)
    # ============================================================
    # Structure: verb: [common particles]
    PHRASAL_VERBS: dict = field(default_factory=lambda: {
        'get': ['up', 'on', 'off', 'over', 'along', 'away', 'back', 'by', 'down', 'through'],
        'put': ['off', 'on', 'up', 'down', 'away', 'out', 'through', 'up with'],
        'take': ['off', 'on', 'after', 'up', 'over', 'down', 'back', 'out'],
        'look': ['up', 'down', 'for', 'after', 'into', 'forward to', 'out'],
        'go': ['on', 'off', 'out', 'over', 'through', 'back', 'ahead', 'with'],
        'make': ['up', 'out', 'for'],
        'give': ['up', 'in', 'away', 'back', 'out'],
        'break': ['up', 'down', 'in', 'out', 'through'],
        'call': ['off', 'on', 'up', 'back', 'for'],
        'turn': ['on', 'off', 'up', 'down', 'into', 'out'],
        'run': ['out', 'into', 'over', 'away', 'through'],
    })