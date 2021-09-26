def bubbleSort(array):
    # Write your code here.
    while True:
        swaps = 0
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                swaps += 1
                array[i], array[i+1] = array[i+1], array[i]
        
        if swaps == 0:
            break

    return array

if __name__ == '__main__':
    bubbleSort([8,5,2,9,5,6,3])