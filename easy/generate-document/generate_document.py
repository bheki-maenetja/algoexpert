def generateDocument(characters, document):
    # Write your code here.
    char_counts = {}
    
    for char in characters:
        if char not in char_counts:
            char_counts[char] = [1, 0]
        else:
            char_counts[char][0] += 1
        
    for char in document:
        if char not in char_counts:
            char_counts[char] = [0, 1]
        else:
            char_counts[char][1] += 1
        
        if char_counts[char][1] > char_counts[char][0]:
            return False
    return True