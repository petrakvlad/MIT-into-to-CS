# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "/mnt/c/Users/Vlad/Documents/GitHub/someproj/birthdays/words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

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

    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
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

    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word1 = my_word.replace(" ", "")
    len1 = len(my_word1)
    len2 = len(other_word)

    if not len1 == len2:
        return False
    
    for let1, let2 in zip(my_word1, other_word):
        if not let1.isalpha():
            continue
        else:
            if not let1 == let2:
                return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    count = 0
    for word in wordlist:
        possible = match_with_gaps(my_word, word)
        if possible == True:
            count = count + 1
            print(word, end = " ")
    if count == 0:
        print("No matches found")
    return 0



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    warn = 3
    lengt = len(secret_word)
    print(f"I have a word that is {lengt} long")
    count = 6
    while count > 0:
        print(f"You have {count} guesses left")
        let = get_available_letters(letters_guessed)
        print(f"Available letters: {let}")
        guess = input("Please guess a letter: ").lower()
        if guess == "*":
            print("Potential words are: ")
            newword1 = get_guessed_word(secret_word, letters_guessed)
            show_possible_matches(newword1)
            print("")
            continue
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



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
