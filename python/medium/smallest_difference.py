def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    
    current_pair = [arrayOne[0], arrayTwo[0]]
    dist = abs(arrayOne[0] - arrayTwo[0])
    
    while arrayOne != [] and arrayTwo != []:
        new_dist = abs(arrayOne[0] - arrayTwo[0])
        if new_dist < dist:
            dist = new_dist
            current_pair[0], current_pair[1] = arrayOne[0], arrayTwo[0]
        if arrayOne[0] < arrayTwo[0]:
            arrayOne = arrayOne[1:]
        elif arrayOne[0] > arrayTwo[0]:
            arrayTwo = arrayTwo[1:]
        else:
            break
    
    return current_pair