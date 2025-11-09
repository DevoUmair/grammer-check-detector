from dataclasses import dataclass, field

@dataclass
class LinguisticKnowledge:
    """Comprehensive linguistic knowledge base for grammar checking"""

    # Nouns that usually do not require an article
    ZERO_ARTICLE_NOUNS: set = field(default_factory=lambda: {
        'school', 'college', 'university', 'church', 'hospital', 'prison', 'court',
        'breakfast', 'lunch', 'dinner', 'brunch', 'supper',
        'home', 'work', 'bed', 'town', 'sea',
        'football', 'cricket', 'tennis', 'basketball', 'chess', 'soccer',
        'mathematics', 'physics', 'chemistry', 'history', 'english',
        'music', 'art', 'literature', 'poetry',
    })

    # Uncountable nouns
    UNCOUNTABLE: set = field(default_factory=lambda: {
        'information', 'advice', 'knowledge', 'research', 'evidence', 'progress',
        'furniture', 'equipment', 'luggage', 'baggage', 'homework', 'housework',
        'weather', 'traffic', 'news', 'software', 'hardware',
        'water', 'milk', 'coffee', 'tea', 'rice', 'bread', 'butter', 'cheese',
        'money', 'cash', 'gold', 'silver',
        'happiness', 'anger', 'love', 'hate', 'fear', 'courage',
    })

    # Preposition collocations for verbs and adjectives
    PREPOSITION_COLLOCATIONS: dict = field(default_factory=lambda: {
        'go': {'to': ['school', 'college', 'university', 'work', 'bed', 'market', 'cinema', 'hospital']},
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
        'good': {'at': ['playing', 'singing', 'dancing', 'math', 'sports']},
        'bad': {'at': ['playing', 'singing', 'dancing', 'math', 'sports']},
        'interested': {'in': ['subject', 'topic', 'field', 'activity']},
        'responsible': {'for': ['task', 'project', 'work', 'mistake']},
        'afraid': {'of': ['dark', 'heights', 'spiders', 'failure']},
        'proud': {'of': ['achievement', 'success', 'child', 'work']},
        'capable': {'of': ['doing', 'achieving', 'handling']},
        'familiar': {'with': ['concept', 'system', 'process', 'area']},
        'different': {'from': ['other', 'previous', 'original']},
        'similar': {'to': ['other', 'previous', 'original']},
    })

    # Irregular verbs
    IRREGULAR_VERBS: dict = field(default_factory=lambda: {
        'be': {'past': 'was/were', 'past_participle': 'been', 'present_3sg': 'is'},
        'have': {'past': 'had', 'past_participle': 'had', 'present_3sg': 'has'},
        'do': {'past': 'did', 'past_participle': 'done', 'present_3sg': 'does'},
        'go': {'past': 'went', 'past_participle': 'gone', 'present_3sg': 'goes'},
        'see': {'past': 'saw', 'past_participle': 'seen', 'present_3sg': 'sees'},
        'eat': {'past': 'ate', 'past_participle': 'eaten', 'present_3sg': 'eats'},
        'take': {'past': 'took', 'past_participle': 'taken', 'present_3sg': 'takes'},
        'give': {'past': 'gave', 'past_participle': 'given', 'present_3sg': 'gives'},
        'make': {'past': 'made', 'past_participle': 'made', 'present_3sg': 'makes'},
        'know': {'past': 'knew', 'past_participle': 'known', 'present_3sg': 'knows'},
        'get': {'past': 'got', 'past_participle': 'got/gotten', 'present_3sg': 'gets'},
        'come': {'past': 'came', 'past_participle': 'come', 'present_3sg': 'comes'},
        'think': {'past': 'thought', 'past_participle': 'thought', 'present_3sg': 'thinks'},
        'say': {'past': 'said', 'past_participle': 'said', 'present_3sg': 'says'},
        'find': {'past': 'found', 'past_participle': 'found', 'present_3sg': 'finds'},
        'write': {'past': 'wrote', 'past_participle': 'written', 'present_3sg': 'writes'},
        'buy': {'past': 'bought', 'past_participle': 'bought', 'present_3sg': 'buys'},
        'run': {'past': 'ran', 'past_participle': 'run', 'present_3sg': 'runs'},
        'bring': {'past': 'brought', 'past_participle': 'brought', 'present_3sg': 'brings'},
        'teach': {'past': 'taught', 'past_participle': 'taught', 'present_3sg': 'teaches'},
        'catch': {'past': 'caught', 'past_participle': 'caught', 'present_3sg': 'catches'},
        'send': {'past': 'sent', 'past_participle': 'sent', 'present_3sg': 'sends'},
    })

    # Regular verb suffixes for 3rd person singular
    REGULAR_VERB_SUFFIXES: dict = field(default_factory=lambda: {
        'present_3sg': 's'
    })

    # Auxiliary verbs
    AUXILIARY_VERBS: dict = field(default_factory=lambda: {
        'be': {'present': ['am', 'is', 'are'], 'past': ['was', 'were']},
        'have': {'present': ['has', 'have'], 'past': ['had']},
        'do': {'present': ['does', 'do'], 'past': ['did']}
    })

    # Temporal markers
    PAST_MARKERS: set = field(default_factory=lambda: {
        'yesterday', 'ago', 'last', 'previous', 'earlier', 'before', 'once', 'already', 'recently', 'earlier today'
    })
    PRESENT_MARKERS: set = field(default_factory=lambda: {
        'now', 'currently', 'today', 'nowadays', 'presently', 'at the moment', 'this week', 'these days'
    })
    FUTURE_MARKERS: set = field(default_factory=lambda: {
        'tomorrow', 'next', 'soon', 'later', 'will', 'shall', 'going to', 'in a week', 'later today', 'soon after'
    })

    # Frequency adverbs
    FREQUENCY_ADVERBS: set = field(default_factory=lambda: {
        'always', 'usually', 'often', 'sometimes', 'rarely', 'never', 'seldom',
        'frequently', 'occasionally', 'regularly', 'daily', 'weekly', 'monthly'
    })

    # Confusion sets
    CONFUSION_SETS: dict = field(default_factory=lambda: {
        'their': ['there', "they're"],
        'there': ['their', "they're"],
        "they're": ['their', 'there'],
        'your': ["you're"],
        "you're": ['your'],
        'its': ["it's"],
        "it's": ['its'],
        'affect': ['effect'],
        'effect': ['affect'],
    })

    # Definite article exceptions
    DEFINITE_ARTICLE_NOUNS: set = field(default_factory=lambda: {
        'sun', 'moon', 'earth', 'president', 'prime minister', 'internet'
    })

    # Indefinite article exceptions (silent 'h')
    INDEFINITE_ARTICLE_EXCEPTIONS: set = field(default_factory=lambda: {
        'honest', 'hour', 'heir'
    })

    # Adjective-preposition pairs
    ADJECTIVE_PREPOSITIONS: dict = field(default_factory=lambda: {
        'interested': 'in',
        'afraid': 'of',
        'responsible': 'for',
        'similar': 'to',
        'different': 'from',
        'good': 'at',
        'bad': 'at',
        'proud': 'of',
        'capable': 'of',
        'familiar': 'with',
    })
