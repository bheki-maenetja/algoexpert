def moveElementToEnd(array, toMove):
    # Write your code here.
    if toMove not in array:
        return array
    
    current_ptr = 0
    target_ptr = len(array) - 1
    for i in range(len(array) - 1, -1, -1):
        if array[i] != toMove:
            target_ptr = i
            break
    else:
        return array
            
    while target_ptr >= current_ptr:
        if array[current_ptr] == toMove:
            array[current_ptr] = array[target_ptr]
            array[target_ptr] = toMove
            while array[target_ptr] == toMove:
                target_ptr -= 1
        current_ptr += 1
    
    return array