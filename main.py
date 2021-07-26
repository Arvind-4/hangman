import random
from words_to_txt import word_to_list
from hangman_imgs import display_hangman
from play_function import play

filename = 'words.txt'

def get_word():
    list_of_words = word_to_list(filename=filename)
    words = random.choice(list_of_words)
    return words

def game():
    word = get_word()
    play(word=word)
    yes_or_no = input('Play Again [y/n]?')
    while yes_or_no.upper == 'Y':
        word = get_word()
        play(word=word)
        
def main():
    game()    

if __name__ == '__main__':
    main()