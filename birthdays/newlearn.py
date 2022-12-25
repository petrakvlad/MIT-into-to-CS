def matching(my_word, other_word):
    count = 0
    for letter in my_word:
        if letter.isalpha():
            count = count +1
        else:
            count = count + 0.5
    len1 = int(count)
    len2 = len(other_word)
    if not len1 == len2:
        return False

    count1 = 0
    checker = 0
    for letter in other_word:
        if my_word[count1].isalpha():
            if my_word[count1] == letter:
                checker = checker + 1
                count1 = count1 + 1
                continue
            else:
                return False
        else:
            count1 = count1 + 2
            continue
    if checker == 0:
        return False
    else:
        return True




#print(matching("_ pp_ e", "apple"))

list = ["epplo", "opplo", "appleee", "apple"]


def matching_better(my_word, other_word):
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

#print(matching_better("_ pp_ e", "apple"))


def show_possible_matches(my_word):
    count = 0
    for word in list:
        possible = matching_better(my_word, word)
        if possible == True:
            count = count + 1
            print(word, end = " ")
    if count == 0:
        print("No matches found")
    return 0

print(show_possible_matches("_ pp_ i"))


