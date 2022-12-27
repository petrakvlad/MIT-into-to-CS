# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    '*': 0, 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "/mnt/c/Users/Vlad/Documents/GitHub/someproj/py problemset 3/words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()
    points_inword = 0
    for letter in word:
        points_inword = points_inword + SCRABBLE_LETTER_VALUES[letter]
    one_option = 7 * len(word) - 3 * (n - len(word))
    right_hand_side = one_option if one_option > 1 else 1
    total = points_inword * right_hand_side
    return total
    # TO DO... Remove this line when you implement this function

#print(get_word_score("weed", 6))
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    hand["*"] = hand.get("*", 0) + 1
    
    return hand
#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand_copy = hand.copy()
    word = word.lower()
    for letter in word:
        if letter in hand_copy.keys():
            if hand_copy[letter] == 0:
                continue
            else:
                hand_copy[letter] = hand_copy[letter] - 1
    return hand_copy

    # TO DO... Remove this line when you implement this function
#print(update_hand({"a": 1, "b": 2, "c": 1, "d": 1}, "Abcc"))
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    handcopy = hand.copy()
    word = word.lower()
    any = 0
    if "*" in word:
        for letter in VOWELS:
            wordcopy = word.replace("*", letter)
            if wordcopy in word_list:
                any = any + 1
        if any == 0:
            return False
    else:
        if word not in word_list:
            return False

    for letter in word:
        if letter in handcopy.keys():
            if handcopy[letter] == 0:
                return False
            else:
                handcopy[letter] = handcopy[letter] - 1
        else:
            return False
    return True

# TO DO... Remove this line when you implement this function
#wordlist = load_words()
#print(is_valid_word("Ab*le", {"a": 1, "b": 2, "e": 2, "l": 1, "*": 1}, wordlist))
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    count = 0
    allkeys = hand.keys()
    for each in allkeys:
        if hand[each] != 0:
            count = count + 1
    return count
    # TO DO... Remove this line when you implement this function

#calculate_handlen({"a": 1, "b": 2, "e": 2, "l": 1})

def play_hand(hand, word_list):

    #def get_word_score(word, n):
    #def display_hand(hand):
    #def deal_hand(n):
    #def update_hand(hand, word):
    #def is_valid_word(word, hand, word_list):
    #def calculate_handlen(hand):
    """
    hand_copy = hand.copy()
    total_points = 0
    print("Current hand: ", end = "")
    display_hand(hand)
    hand_leng = calculate_handlen(hand_copy)

    user_input = input("Enter word: ")
    while user_input != "!!":
        word_valid = is_valid_word(user_input, hand_copy, word_list)
        if word_valid == False:
            print("That is not a valid word. Please choose another word.")
            hand_copy = update_hand(hand_copy, user_input)
            hand_leng = calculate_handlen(hand_copy)
        else:
            word_score = get_word_score(user_input, hand_leng)
            total_points = total_points + word_score
            hand_copy = update_hand(hand_copy, user_input)
            hand_leng = calculate_handlen(hand_copy)
            print("\"", user_input, "\"", " earned ", word_score, "points. Total: ", total_points, " points.")
        if hand_leng == 0:
            print("Ran out of letters. Total score: ", total_points)
            break
        else:
            print("Current hand: ", end = "")
            display_hand(hand_copy)
            user_input = input("Enter word: ")
    print("Total score: ", total_points)
    return total_points
    """
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    hand_copy = hand.copy()
    hand_leng = calculate_handlen(hand_copy)
    # Keep track of the total score
    total_points = 0
    # As long as there are still letters left in the hand:
    while hand_leng != 0:
        # Display the hand
        print("Current hand: ", end = "")
        display_hand(hand_copy)
        # Ask user for input
        user_input = input("Enter word: ")
        # If the input is two exclamation points:
        if user_input == "!!":
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(user_input, hand_copy, word_list):
                # Tell the user how many points the word earned,
                word_score = get_word_score(user_input, hand_leng)
                total_points = total_points + word_score
                print("\"", user_input, "\"", " earned ", word_score, "points. Total: ", total_points, " points.")
                # and the updated total score
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("That is not a valid word. Please choose another word.")
                
            # update the user's hand by removing the letters of their inputted word
            hand_copy = update_hand(hand_copy, user_input)
            hand_leng = calculate_handlen(hand_copy)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print("Total score: ", total_points)
    return total_points
    # Return the total score as result of function

#play_hand({"a": 1, "i": 1, "c": 1, "f": 1, "*": 1, "t": 1, "x": 1}, load_words())

#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.
    
    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    letter_not_to_include = ''.join(list(hand.keys()))
    hand_copy = hand.copy()

    if letter not in letter_not_to_include:
        return hand_copy


    copy_vowels = VOWELS
    copy_conson = CONSONANTS

    for letterr in letter_not_to_include:
        copy_vowels = copy_vowels.replace(letterr, "")
    for letterr in letter_not_to_include:
        copy_conson = copy_conson.replace(letterr, "")


    
    number_of_occurences = hand[letter]
    num_rand = random.random()

    if num_rand > 0.5:
        new_letter = random.choice(copy_vowels)
    else:
        new_letter = random.choice(copy_conson)

    hand_copy.pop(letter)
    hand_copy[new_letter] = number_of_occurences

    return hand_copy




    # TO DO... Remove this line when you implement this function
#print(substitute_hand({"a": 2, "c": 1, "f": 1, "*": 1, "t": 1, "x": 1}, "m"))
    
def play_game(word_list):
    """
    Allow the user to play a series of hands
    
    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    total_with_replays = 0
    substitute_options = 1
    replay_option = 1
    num_hands = int(input("Enter total number of hands: "))
    total_score_all = 0
    for sets in range(num_hands):
        hand_new = deal_hand(HAND_SIZE)
        print("Current hand: ", end = "")
        display_hand(hand_new)
        if substitute_options != 0:
            substit = input("Would you like to substitute a letter? ")
            if substit == "yes":
                substitute_options = 0
                letter_sub = input("Which letter would you like to replace: ")
                hand_new = substitute_hand(hand_new, letter_sub)
        first_hand_play = play_hand(hand_new, word_list)
        if replay_option != 0:
            replays = input("Would you like to replay hand? ")
            if replays == "yes":
                replay_option = 0
                second_hand_play = play_hand(hand_new, word_list)
            else:
                second_hand_play = 0
        if first_hand_play > second_hand_play: 
            total_with_replays = first_hand_play
        else:
            total_with_replays = second_hand_play
        print("Total for the hand is: ", total_with_replays)
        total_score_all = total_score_all + total_with_replays
    print("Total for the game is ", total_score_all)

    # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
