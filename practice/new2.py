characters = ["a", "b", "c", "d"]
pass_lenght = 3

def combinations(chars, nums, current_char = ""):

    if nums == None:
        nums = len(chars)

    results = []

    #base case
    if nums == 0:
        return [current_char]


    for each_char in chars:
        results.extend(combinations(chars, nums - 1, current_char + each_char))
    return results
    
        
print(combinations(characters, pass_lenght))
print(len(combinations(characters, pass_lenght)))
    
