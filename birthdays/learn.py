import string

secret_word = "apple"
letters_guessed = []

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    check = True
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
      if letter in letters_guessed:
        continue
      else:
        check = False
    return check

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    str = ""
    for letter in secret_word:
      if letter in letters_guessed:
        str = str + letter
      else:
        str = str + "_ "
    return str

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = string.ascii_lowercase
    for letter in letters_guessed:
      alphabet = alphabet.replace(letter, "")
    return alphabet


def mymain(letters_guessed):
    warn = 3
    lengt = len(secret_word)
    print(f"I have a word that is {lengt} long")
    count = 6
    while count > 0:
        print(f"You have {count} guesses left")
        let = get_available_letters(letters_guessed)
        print(f"Available letters: {let}")
        guess = input("Please guess a letter: ").lower()
        if not str.isalpha(guess):
            if not warn == 0:
                warn = warn - 1
                print(f"Only use alphabetic letters. you have {warn} warnings left")
                continue
            else:
                print(f"Only use alphabetic letters. you have no warnings left")
                count = count - 1
                continue
        if guess in letters_guessed:
            if not warn == 0:
                warn = warn - 1
                print(f"Seems you have already guessed it. you have {warn} warnings left")
                continue
            else:
                print(f"Seems you have already guessed it. you have no warnings left")
                if guess in "aeiou":
                    count = count - 2
                else:
                    count = count - 1
                continue
        letters_guessed.append(guess)
        newword = get_guessed_word(secret_word, letters_guessed)
        checkforguess = is_word_guessed(secret_word, letters_guessed)
        if guess in secret_word:
            print(f"Good guess: {newword}")
            if checkforguess == True:
                char_seen = []
                for char in secret_word:
                    if char not in char_seen:
                        char_seen.append(char)
                unique_len = len(char_seen)
                points = unique_len * count
                print(f"You have got {points} points")
                print("word guessed")
                return 1
            continue
        else:
            print(f"Ops, the letter is not in my word: {newword}")
        if checkforguess == True:
            char_seen = []
            for char in secret_word:
                if char not in char_seen:
                    char_seen.append(char)
            unique_len = len(char_seen)
            points = unique_len * count
            print(f"You have got {points} points")
            print("word guessed")
            return 1
        if guess in "aeiou":
            count = count - 2
        else:
            count = count - 1
    
    print("Sorry you did not guess")
    print("Word was " + secret_word)
    return 0

mymain(letters_guessed)
