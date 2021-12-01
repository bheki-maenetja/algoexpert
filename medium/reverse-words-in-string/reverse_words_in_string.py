def reverseWordsInString(string):
    # Write your code here.
    if not string: return string
    
    word_list = []
    current_word = string[0]
    for i in range(1, len(string)):
        char = string[i]
        if (char == " " and char != current_word[-1]) or (char != " " and current_word[-1] == " "):
            word_list.insert(0, current_word)
            current_word = char
        else:
            current_word += char

    word_list.insert(0, current_word)
    return "".join(word_list)