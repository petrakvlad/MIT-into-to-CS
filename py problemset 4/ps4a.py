# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return sequence

    head = sequence[0]
    tail = sequence[1:]

    permutations = []

    newone = get_permutations(tail)

    for each in newone:
        for i in range(len(each) + 1):
            permutations.append(each[:i]+head+each[i:])


    return permutations




    #delete this line and replace with your code here

if __name__ == '__main__':
    print("woo")
#   #EXAMPLE
    example_input = 'aeiou'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    result = get_permutations(example_input)
    count = 0
    for i in result:
        count = count + 1
    print('Actual Output:', result)
    print(count)
    #op = get_permutations(example_input)
    #print(op)