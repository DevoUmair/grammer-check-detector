from dataclasses import dataclass, field

@dataclass
class LinguisticKnowledge:
    ZERO_ARTICLE_NOUNS: set = field(default_factory=lambda: {
        'school', 'college', 'university', 'church', 'hospital', 'prison', 'court',
        'breakfast', 'lunch', 'dinner', 'brunch', 'supper',
        'home', 'work', 'bed', 'town', 'sea',
        'football', 'cricket', 'tennis', 'basketball', 'chess', 'soccer',
        'mathematics', 'physics', 'chemistry', 'history', 'english',
        'music', 'art', 'literature', 'poetry',
    })

    UNCOUNTABLE_NOUNS: set = field(default_factory=lambda: {
        'information', 'advice', 'knowledge', 'research', 'evidence', 'progress',
        'furniture', 'equipment', 'luggage', 'baggage', 'homework', 'housework',
        'weather', 'traffic', 'news', 'software', 'hardware',
        'water', 'milk', 'coffee', 'tea', 'rice', 'bread', 'butter', 'cheese',
        'money', 'cash', 'gold', 'silver',
        'happiness', 'anger', 'love', 'hate', 'fear', 'courage',
    })

    PREPOSITION_COLLOCATIONS: dict = field(default_factory=lambda: {
        'arrive': {'at': ['school', 'work', 'home', 'station'], 'in': ['city', 'country', 'town']},
        'participate': {'in': ['activity', 'event', 'competition', 'discussion']},
        'consist': {'of': ['parts', 'elements', 'components']},
        'depend': {'on': ['factors', 'circumstances', 'conditions']},
        'listen': {'to': ['music', 'radio', 'advice', 'teacher']},
        'look': {'at': ['picture', 'screen', 'board'], 'for': ['job', 'house', 'solution']},
        'wait': {'for': ['bus', 'train', 'person', 'reply']},
        'search': {'for': ['information', 'answer', 'solution']},
        'apologize': {'for': ['mistake', 'delay', 'inconvenience']},
        'congratulate': {'on': ['success', 'achievement', 'victory']},
    })

    IRREGULAR_VERBS: dict = field(default_factory=lambda: {
        'be': {'past': 'was/were', 'past_participle': 'been', 'present_3sg': 'is'},
        'have': {'past': 'had', 'past_participle': 'had', 'present_3sg': 'has'},
        'do': {'past': 'did', 'past_participle': 'done', 'present_3sg': 'does'},
        'go': {'past': 'went', 'past_participle': 'gone', 'present_3sg': 'goes'},
        'see': {'past': 'saw', 'past_participle': 'seen', 'present_3sg': 'sees'},
        'eat': {'past': 'ate', 'past_participle': 'eaten', 'present_3sg': 'eats'},
        'take': {'past': 'took', 'past_participle': 'taken', 'present_3sg': 'takes'},
    })

    COMMON_MISS_SPELLINGS: dict = field(default_factory=lambda: {
        'recieve': 'receive',
        'acheive': 'achieve',
        'definately': 'definitely',
        'seperate': 'separate',
        'occured': 'occurred',
        'untill': 'until',
        'begining': 'beginning',
        'environement': 'environment',
        'goverment': 'government',
        'alot': 'a lot',
        'thier': 'their',
        'tommorrow': 'tomorrow',
        'tounge': 'tongue',
        'truely': 'truly',
        'wierd': 'weird',
    })

    PAST_MARKERS: set = field(default_factory=lambda: {
        'yesterday', 'ago', 'last', 'previous', 'earlier', 'before', 'once', 
        'already', 'recently'
    })

    FUTURE_MARKERS: set = field(default_factory=lambda: {
        'tomorrow', 'next', 'soon', 'later', 'will', 'shall', 'going'
    })