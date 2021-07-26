def word_to_list(filename):
    with open(filename) as f:
        word_list = f.read().upper().split()    
    return word_list