
def getCombos(chars, k):

    if k == 0:
        # BASE CASE
        return ['']
    elif chars == '':

        return []

    # RECURSIVE CASE
    combinations = []

    # First part, get the combos that include the head:
    head = chars[:1]
    tail = chars[1:]

    tailCombos = getCombos(tail, k - 1)

    for tailCombo in tailCombos:

        combinations.append(head + tailCombo)

    # Second part, get the combos that don't include the head:

    combinations.extend(getCombos(tail, k))

    return combinations


def fibona(times):
    a, b = 1, 1
    for i in range(1, times):
        a, b = b, a+b
    return a

def fibona_rec(times, a = 1, b = 1):
    #base
    if times == 1:
        return a
    
    a, b = b, a + b
    result = fibona_rec(times - 1, a, b)
    return result



def find_need(needle, hay):
    for i in range(len(hay)):
        if i+len(needle) > len(hay):
            return -1
        if hay[i:i+len(needle)] == needle:
            return i
    return -1

#print(find_need("lol", "well thislolis total lil"))

def find_need_rec(needle, hay, i = 0):

    if i + len(needle) > len(hay):
        return -1
    
    if hay[i:i+len(needle)] == needle:
            return i
    else:
        return find_need_rec(needle, hay, i + 1)

#print(find_need_rec("lol", "well this lilis total lil"))

def expo(number, power):
    if power == 1:
        return number
    
    return number * expo(number, power - 1)

#print(expo(17,10))

def expo_division(number, power):

    if power == 1:
        return number
    
    if power % 2 == 0:
        result = expo_division(number, power / 2)
        return result * result
    else:
        result = expo_division(number, power - 1)
        return result * number

#print(expo_division(17,10))

def awesome(number, power):

    #step one
    steps = []
    while power > 1:
        if power % 2 == 0:
            steps.append("square")
            power = power / 2
        else:
            steps.append("mult")
            power = power - 1


    #step two
    result = number
    while steps:
        op = steps.pop()
        if op == "mult":
            result = result * number
        else:
            result = result * result

    return result

#print(awesome(5, 3))

def sumoflist(list):

    if len(list) == 0:
        return 0

    head = list[0]
    tail = list[1:]
    return head + sumoflist(tail)

#print(sumoflist([8,7,4]))


def rev(strin):

    if strin == "" or len(strin) == 1:
        return strin

    head = strin[0]
    tail = strin[1:]
    return rev(tail) + head

#print(rev("valeraloh"))


def poly(str):

    if len(str) == 0 or len(str) == 1:
        return True

    head = str[0]
    middle = str[1:-1]
    tail = str[-1]

    return head == tail and poly(middle)

#print(poly("zalufaz"))


def ackermann(m, n, indentation=None):
    if indentation is None:
        indentation = 0
    print('%sackermann(%s, %s)' % (' ' * indentation, m, n))

    if m == 0:
        # BASE CASE
        return n + 1
    elif m > 0 and n == 0:
        # RECURSIVE CASE
        return ackermann(m - 1, 1, indentation + 1)
    elif m > 0 and n > 0:
        # RECURSIVE CASE
        return ackermann(m - 1, ackermann(m, n - 1, indentation + 1), indentation + 1)

print('Starting with m = 1, n = 1:')
print(ackermann(1, 1))
print('Starting with m = 2, n = 3:')
print(ackermann(2, 3))