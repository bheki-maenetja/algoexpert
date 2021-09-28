def mergeSort(array):
    # Write your code here.
    if len(array) == 1:
        return array
    middle = len(array) // 2
    return merge(mergeSort(array[:middle]), mergeSort(array[middle:]), [])

def merge(left, right, merge_array):
    left_ptr, right_ptr = 0, 0
    left_len, right_len = len(left), len(right)
    
    while left_ptr < left_len or right_ptr < right_len:
        left_item = left[left_ptr] if left_ptr < left_len else None
        right_item = right[right_ptr] if right_ptr < right_len else None

        if left_item is None:
            merge_array.append(right_item)
            right_ptr += 1
        elif right_item is None:
            merge_array.append(left_item)
            left_ptr += 1
        else:
            if right_item < left_item:
                merge_array.append(right_item)
                right_ptr += 1
            else:
                merge_array.append(left_item)
                left_ptr += 1
    
    return merge_array

if __name__ == "__main__":
    print(mergeSort([4, 1, 5, 0, -9, -3, -3, 9, 3, -4, -9, 8, 1, -3, -7, -4, -9, -1, -7, -2, -7, 4]))
    # print(merge([1], [2], []))