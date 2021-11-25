def binarySearch(array, target):
    # Write your code here.
    left_ptr, right_ptr = 0, len(array) - 1
    
    while left_ptr <= right_ptr:
        middle = (left_ptr + right_ptr) // 2
        current_item = array[middle]
        if current_item < target:
            left_ptr = middle + 1
        elif current_item > target:
            right_ptr = middle - 1
        else:
            return middle

    return -1

if __name__ == "__main__":
    binarySearch([0,1,21,33,45,45,61,71,72,73], 34)