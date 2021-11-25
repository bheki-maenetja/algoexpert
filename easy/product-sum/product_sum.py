def productSum(array, depth = 1):
    # Write your code here.
    item_sum = 0
    for item in array:
        if type(item) == list:
            item_sum += (depth + 1) * productSum(item, depth + 1)
        else:
            item_sum += item
    
    return item_sum