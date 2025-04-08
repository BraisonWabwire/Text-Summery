import nltk
from nltk.corpus import wordnet
import random
nltk.download('wordnet')  # Download WordNet if not already installed

def get_synonym(word, pos=None):
    """
    Retrieves a suitable synonym for a word, optionally matching part of speech.
    
    Args:
        word (str): The word to find a synonym for
        pos (str, optional): Part of speech (e.g., 'n' for noun, 'v' for verb)
    
    Returns:
        str: A synonym or the original word if no synonym is found
    """
    synonyms = []
    # Get synsets for the word, optionally filtered by part of speech
    for syn in wordnet.synsets(word, pos=pos):
        for lemma in syn.lemmas():
            synonym = lemma.name().lower()
            # Include single-word synonyms, exclude the original word
            if '_' not in synonym and synonym != word:
                synonyms.append(synonym)
    # Return a random synonym if available, else the original word
    return random.choice(synonyms) if synonyms else word

def expand_to_equivalent_sentence(sentence):
    """
    Creates an equivalent sentence by replacing words with synonyms.
    
    Args:
        sentence (str): The input sentence
    
    Returns:
        str: A new sentence with synonyms, retaining original meaning
    """
    # Split the sentence into words
    words = sentence.lower().split()
    new_sentence = []
    
    for word in words:
        # Simple POS guessing based on common cases (extend as needed)
        pos = None
        if word in ['is', 'are', 'was', 'were', 'run', 'runs', 'running']:
            pos = wordnet.VERB
        elif word in ['car', 'house', 'person', 'dog']:
            pos = wordnet.NOUN
        elif word in ['fast', 'quick', 'smooth', 'big']:
            pos = wordnet.ADJ
        elif word in ['smoothly', 'quickly']:
            pos = wordnet.ADV
        
        # Get a synonym for the word
        synonym = get_synonym(word, pos)
        # Capitalize the first word of the sentence
        if not new_sentence and synonym:
            synonym = synonym.capitalize()
        new_sentence.append(synonym)
    
    # Join words into a sentence, add period if not present
    result = ' '.join(new_sentence)
    if not result.endswith('.'):
        result += '.'
    return result

# Main program
if __name__ == "__main__":
    # Get user input
    user_sentence = input("Enter a sentence: ").strip()
    
    if not user_sentence:
        print("No sentence provided!")
    else:
        print(f"Original sentence: {user_sentence}")
        
        # Generate equivalent sentence
        equivalent = expand_to_equivalent_sentence(user_sentence)
        print(f"Equivalent sentence: {equivalent}")