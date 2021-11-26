def firstNonRepeatingCharacter(string):
    # Write your code here.
    hash_table = {}
    for c in string:
        if not hash_table.get(c):
            hash_table[c] = 1
        else:
            hash_table[c] += 1
    
    for i in range(len(string)):
        if hash_table[string[i]] == 1:
            return i
    return -1