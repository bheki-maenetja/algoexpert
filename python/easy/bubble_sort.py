def bubbleSort(array):
    # Write your code here.
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                is_sorted = False
                array[i], array[i+1] = array[i+1], array[i]
    
    return array

if __name__ == '__main__':
    bubbleSort([8,5,2,9,5,6,3])