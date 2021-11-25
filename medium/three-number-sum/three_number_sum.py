def threeNumberSum(array, targetSum):
    # Write your code here.
	triples = []
	array.sort()
	
	for i in range(len(array) - 2):
		left_ptr, right_ptr = i+1, len(array) - 1
		while left_ptr < right_ptr:
			current_sum = array[i] + array[left_ptr] + array[right_ptr]
			if current_sum == targetSum:
				triples.append([array[i], array[left_ptr], array[right_ptr]])
				left_ptr += 1
				right_ptr -= 1
			elif current_sum < targetSum:
				left_ptr += 1
			else:
				right_ptr -= 1
    				  
	return triples