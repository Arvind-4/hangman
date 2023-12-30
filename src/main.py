import random
import pathlib

from play_function import play
from words_to_txt import word_to_list

BASE_DIR = pathlib.Path(__file__).parent.parent
filename = BASE_DIR / "words" / "list.txt"


def get_word():
    list_of_words = word_to_list(filename=filename)
    return random.choice(list_of_words)


def game():
    word = get_word()
    print("Welcome to Hangman!")
    print("The Word has been chosen, Good Luck!")
    print("The Word has {} letters".format(len(word)))
    play(word=word)
    yes_or_no = input("Play Again [y/n]?")
    while yes_or_no.upper == "Y":
        word = get_word()
        play(word=word)


if __name__ == "__main__":
    game()
