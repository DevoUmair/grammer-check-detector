from dataclasses import dataclass, field


@dataclass
class LinguisticKnowledge:
    """Extensive linguistic knowledge base for context-aware grammar correction."""

    # ============================================================
    # 1. ZERO ARTICLE NOUNS (Used without 'a/an/the')
    # ============================================================
    ZERO_ARTICLE_NOUNS: set = field(default_factory=lambda: {
        'school', 'college', 'university', 'church', 'hospital', 'prison', 'court', 'bed',
        'home', 'work', 'town', 'sea', 'camp', 'class', 'market', 'office', 'parliament',
        'breakfast', 'lunch', 'dinner', 'supper', 'brunch',
        'football', 'cricket', 'tennis', 'basketball', 'soccer', 'chess', 'golf', 'rugby',
        'mathematics', 'physics', 'chemistry', 'biology', 'history', 'geography', 'economics',
        'english', 'french', 'art', 'music', 'literature', 'philosophy', 'poetry', 'politics'
    })

    # ============================================================
    # 2. UNCOUNTABLE NOUNS
    # ============================================================
    UNCOUNTABLE: set = field(default_factory=lambda: {
        'advice', 'information', 'knowledge', 'research', 'evidence', 'progress',
        'furniture', 'equipment', 'luggage', 'baggage', 'homework', 'housework',
        'weather', 'traffic', 'news', 'software', 'hardware', 'work',
        'water', 'milk', 'coffee', 'tea', 'juice', 'rice', 'bread', 'butter', 'sugar',
        'money', 'cash', 'gold', 'silver', 'oil', 'electricity', 'energy', 'gas',
        'happiness', 'sadness', 'anger', 'love', 'hate', 'fear', 'peace', 'freedom', 'health',
        'education', 'transportation', 'employment', 'poverty', 'wealth'
    })

    # ============================================================
    # 3. DEFINITE ARTICLE NOUNS (Usually require 'the')
    # ============================================================
    DEFINITE_ARTICLE_NOUNS: set = field(default_factory=lambda: {
        'sun', 'moon', 'earth', 'sky', 'internet', 'president', 'prime minister', 'world',
        'government', 'universe', 'climate', 'economy', 'police', 'army', 'media'
    })

    # ============================================================
    # 4. PREPOSITION COLLOCATIONS
    # ============================================================
    PREPOSITION_COLLOCATIONS: dict = field(default_factory=lambda: {
        'go': {'to': ['school', 'work', 'bed', 'church', 'market', 'hospital', 'gym', 'university']},
        'arrive': {'at': ['station', 'airport', 'school', 'work'], 'in': ['city', 'country', 'town']},
        'participate': {'in': ['event', 'meeting', 'competition', 'conference']},
        'depend': {'on': ['weather', 'situation', 'context', 'decision']},
        'listen': {'to': ['music', 'teacher', 'advice', 'radio']},
        'look': {'at': ['picture', 'screen'], 'for': ['solution', 'key', 'job'], 'after': ['child', 'patient']},
        'wait': {'for': ['bus', 'train', 'reply', 'signal']},
        'search': {'for': ['information', 'answer', 'meaning']},
        'apologize': {'for': ['delay', 'mistake', 'rudeness']},
        'believe': {'in': ['truth', 'god', 'system', 'yourself']},
        'agree': {'with': ['idea', 'statement', 'person'], 'to': ['plan', 'proposal']},
        'interested': {'in': ['art', 'science', 'reading', 'technology']},
        'responsible': {'for': ['project', 'task', 'accident', 'team']},
        'afraid': {'of': ['dark', 'snakes', 'heights']},
        'proud': {'of': ['achievement', 'success', 'child']},
        'capable': {'of': ['doing', 'solving', 'managing']},
        'different': {'from': ['others', 'previous', 'original']},
        'similar': {'to': ['this', 'that', 'other']}
    })

    # ============================================================
    # 5. IRREGULAR VERBS (Comprehensive List)
    # ============================================================
    IRREGULAR_VERBS: dict = field(default_factory=lambda: {
        'be': {'past': 'was/were', 'pp': 'been', 's': 'is'},
        'have': {'past': 'had', 'pp': 'had', 's': 'has'},
        'do': {'past': 'did', 'pp': 'done', 's': 'does'},
        'go': {'past': 'went', 'pp': 'gone', 's': 'goes'},
        'see': {'past': 'saw', 'pp': 'seen', 's': 'sees'},
        'take': {'past': 'took', 'pp': 'taken', 's': 'takes'},
        'eat': {'past': 'ate', 'pp': 'eaten', 's': 'eats'},
        'come': {'past': 'came', 'pp': 'come', 's': 'comes'},
        'get': {'past': 'got', 'pp': 'got/gotten', 's': 'gets'},
        'make': {'past': 'made', 'pp': 'made', 's': 'makes'},
        'write': {'past': 'wrote', 'pp': 'written', 's': 'writes'},
        'speak': {'past': 'spoke', 'pp': 'spoken', 's': 'speaks'},
        'break': {'past': 'broke', 'pp': 'broken', 's': 'breaks'},
        'fly': {'past': 'flew', 'pp': 'flown', 's': 'flies'},
        'begin': {'past': 'began', 'pp': 'begun', 's': 'begins'},
        'run': {'past': 'ran', 'pp': 'run', 's': 'runs'},
        'buy': {'past': 'bought', 'pp': 'bought', 's': 'buys'},
        'bring': {'past': 'brought', 'pp': 'brought', 's': 'brings'},
        'teach': {'past': 'taught', 'pp': 'taught', 's': 'teaches'},
        'feel': {'past': 'felt', 'pp': 'felt', 's': 'feels'},
        'find': {'past': 'found', 'pp': 'found', 's': 'finds'},
        'think': {'past': 'thought', 'pp': 'thought', 's': 'thinks'},
        'sell': {'past': 'sold', 'pp': 'sold', 's': 'sells'},
        'tell': {'past': 'told', 'pp': 'told', 's': 'tells'},
        'sit': {'past': 'sat', 'pp': 'sat', 's': 'sits'},
        'stand': {'past': 'stood', 'pp': 'stood', 's': 'stands'},
        'sleep': {'past': 'slept', 'pp': 'slept', 's': 'sleeps'},
        'choose': {'past': 'chose', 'pp': 'chosen', 's': 'chooses'},
    })

    # ============================================================
    # 6. AUXILIARY AND MODAL VERBS
    # ============================================================
    AUXILIARY_VERBS: dict = field(default_factory=lambda: {
        'be': {'present': ['am', 'is', 'are'], 'past': ['was', 'were']},
        'have': {'present': ['have', 'has'], 'past': ['had']},
        'do': {'present': ['do', 'does'], 'past': ['did']},
        'modals': ['will', 'would', 'can', 'could', 'shall', 'should', 'may', 'might', 'must']
    })

    # ============================================================
    # 7. TENSE MARKERS
    # ============================================================
    PAST_MARKERS: set = field(default_factory=lambda: {
        'yesterday', 'ago', 'last', 'previous', 'earlier', 'before', 'once', 'already', 'recently'
    })
    PRESENT_MARKERS: set = field(default_factory=lambda: {
        'now', 'currently', 'today', 'nowadays', 'these days', 'at present', 'at the moment'
    })
    FUTURE_MARKERS: set = field(default_factory=lambda: {
        'tomorrow', 'next', 'soon', 'later', 'eventually', 'shortly', 'in future', 'in a while'
    })

    # ============================================================
    # 8. FREQUENCY ADVERBS
    # ============================================================
    FREQUENCY_ADVERBS: set = field(default_factory=lambda: {
        'always', 'usually', 'often', 'frequently', 'sometimes', 'rarely', 'seldom', 'never',
        'occasionally', 'hardly ever', 'regularly', 'constantly', 'daily', 'weekly'
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
        'affect': ['effect'],
        'effect': ['affect'],
        'accept': ['except'],
        'advise': ['advice'],
        'loose': ['lose'],
        'then': ['than'],
        'few': ['a few'],
        'little': ['a little']
    })

    # ============================================================
    # 10. FUNCTION WORDS (Useful for POS and Syntax)
    # ============================================================
    DETERMINERS: set = field(default_factory=lambda: {
        'a', 'an', 'the', 'this', 'that', 'these', 'those', 'my', 'your', 'his',
        'her', 'its', 'our', 'their', 'some', 'any', 'no', 'each', 'every', 'either', 'neither'
    })

    CONJUNCTIONS: set = field(default_factory=lambda: {
        'and', 'but', 'or', 'so', 'yet', 'because', 'although', 'though', 'unless', 'while', 'whereas', 'since', 'before', 'after', 'until'
    })

    PREPOSITIONS: set = field(default_factory=lambda: {
        'in', 'on', 'at', 'by', 'to', 'from', 'with', 'about', 'for', 'of', 'through', 'under', 'over',
        'between', 'among', 'into', 'onto', 'across', 'beyond', 'during', 'without', 'within'
    })

    # ============================================================
    # 11. PRONOUNS
    # ============================================================
    PRONOUNS: dict = field(default_factory=lambda: {
        'subject': ['I', 'you', 'he', 'she', 'it', 'we', 'they'],
        'object': ['me', 'you', 'him', 'her', 'it', 'us', 'them'],
        'possessive': ['my', 'your', 'his', 'her', 'its', 'our', 'their'],
        'reflexive': ['myself', 'yourself', 'himself', 'herself', 'itself', 'ourselves', 'yourselves', 'themselves'],
        'relative': ['who', 'whom', 'whose', 'which', 'that'],
        'demonstrative': ['this', 'that', 'these', 'those']
    })

    # ============================================================
    # 12. DEGREE ADVERBS
    # ============================================================
    DEGREE_ADVERBS: set = field(default_factory=lambda: {
        'very', 'too', 'enough', 'quite', 'almost', 'nearly', 'barely', 'hardly', 'extremely', 'rather', 'so'
    })


# Example usage:
# knowledge = LinguisticKnowledge()
# print(knowledge.IRREGULAR_VERBS['go']['past'])  # Output: went
