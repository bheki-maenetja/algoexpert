def twoNumberSum(array, targetSum):
    # Write your code here.
    solutions = {
		elem: targetSum - elem
		for elem in array
	}
	
    for i, elem in enumerate(array):
	    if solutions[elem] in array and solutions[elem] in array[i+1:]:
		    return [elem, solutions[elem]]
	
    return []