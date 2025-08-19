import nltk
from spellchecker import SpellChecker
import string
from nltk.corpus import wordnet

# Download required NLTK resources once
nltk.download('punkt_tab', quiet=True)
nltk.download('words', quiet=True)
nltk.download('wordnet', quiet=True)

_cached_spell = None

def get_spellchecker():
    """
    Returns a cached SpellChecker instance.
    """
    global _cached_spell
    if _cached_spell is None:
        print("Initializing SpellChecker...")
        _cached_spell = SpellChecker()
    return _cached_spell

def is_valid_word(word):
    """
    Returns True if word exists in WordNet OR can be split into valid words (compound)
    """
    if wordnet.synsets(word):
        return True
    
    # Check if word can be split into two valid words
    for i in range(1, len(word)):
        if wordnet.synsets(word[:i]) and wordnet.synsets(word[i:]):
            return True
    
    return False

def vocabulary_score(paragraph: str):
    """
    Returns a vocabulary score (0-2) for a paragraph.
    """
    spell = get_spellchecker()  # Use cached spell checker

    # Remove punctuation
    text = paragraph.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize into words
    words = nltk.word_tokenize(text.lower())
    
    # Check for spelling errors using pyspellchecker
    misspelled = spell.unknown(words)
    
    # Filter out words that are actually valid according to WordNet/compound check
    real_errors = [w for w in misspelled if not is_valid_word(w)]
    num_errors = len(real_errors)
    num_words = len(words) if words else 1

    # Error ratio per 5 words
    errors_per_5_words = (num_errors / num_words) * 5

    # Scoring logic
    if num_errors == 0:
        return {
            "score": 2,
            "message": "Has appropriate choice of words",
            "errors": []
        }
    elif errors_per_5_words <= 3:
        return {
            "score": 1,
            "message": "Contains lexical errors but with no hindrances to communication",
            "errors": real_errors
        }
    else:
        return {
            "score": 0,
            "message": "Has defective word choice which could hinder communication",
            "errors": real_errors
        }

def vocab_score(paragraph: str):
    return vocabulary_score(paragraph)
