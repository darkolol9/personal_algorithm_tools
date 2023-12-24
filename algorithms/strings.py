



def does_word_divide(a, b):
    if not len(a):
        return False
    
    for i in range((len(b) // len(a)) + 1):
        if a * i == b:
            return True
        
    return False

