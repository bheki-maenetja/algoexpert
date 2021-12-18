def spiralTraverse(array):
    # Write your code here.
    output_array = []
    
    while len(array) != 0:
        output_array.extend(array.pop(0))
        if array == []: return output_array
    
        for i in range(0, len(array)):
            if array[i]:
                output_array.append(array[i].pop())
                
        output_array.extend(array.pop()[::-1])
        if array == []: return output_array
    
        for i in range(len(array) - 1, -1, -1):
            if array[i]:
                output_array.append(array[i].pop(0))
    
    return output_array