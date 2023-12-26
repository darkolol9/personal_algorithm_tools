



def does_word_divide(a, b):
    """
    Check if a word divides another word.

    Args:
        a (str): The word to check if it divides another word.
        b (str): The word to check if it is divisible by the other word.

    Returns:
        bool: True if the word `a` divides the word `b`, False otherwise.
    """
    if not len(a):
        return False
    
    for i in range((len(b) // len(a)) + 1):
        if a * i == b:
            return True
        
    return False

