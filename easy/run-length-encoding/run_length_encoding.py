def runLengthEncoding(string):
    # Write your code here.
    current_char = string[0]
    char_count = 0
    return_str = ""
    for char in string:
        if char != current_char or char_count == 9:
            return_str += f"{char_count}{current_char}"
            current_char = char
            char_count = 1
        else:
            char_count += 1
    return_str += f"{char_count}{current_char}"
    return return_str