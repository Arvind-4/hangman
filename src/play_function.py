from hangman_imgs import display_hangman


def play(word):
    word_lines = "_" * len(word)
    guessed = False
    guessed_letter = []
    tries = 7
    print(display_hangman(tries=tries))
    print(word_lines)
    print()
    while not guessed and tries > 0:
        guess = input("Please Guess a Letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                print(f"You Have Already Guessed the Letter {guess}!")
            elif guess not in word:
                print(f"{guess} not in the Word!")
                tries -= 1
                guessed_letter.append(guess)
                print(guessed_letter)
            else:
                print(f"Nice, {guess} is in the Word!")
                guessed_letter.append(guess)
                word_as_list = list(word_lines)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_lines = "".join(word_as_list)
                if "_" not in word_lines:
                    guessed = True
        else:
            print("Invalid Entry")
        print(display_hangman(tries=tries))
        print(f"Number of Tries Left=> {tries}")
        print(word_lines)
        print()
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Maybe next time!")
