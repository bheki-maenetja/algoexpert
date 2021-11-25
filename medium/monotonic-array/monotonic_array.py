def isMonotonic(array):
    # Write your code here.
    if len(array) < 3:
        return True
    
    if array[0] <= array[1] <= array[2]:
        isIncreasing = True
    elif array[0] >= array[1] >= array[2]:
        isIncreasing = False
    else:
        return False
    
    for i in range(2, len(array) - 1):
        if isIncreasing:
            if array[i] > array[i+1]: return False
        else:
            if array[i] < array[i+1]: return False
    
    return True