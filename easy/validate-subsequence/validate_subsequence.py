def isValidSubsequence(array, sequence):
    # Write your code here.
	seq_index = 0
	for elem in array:
		if elem == sequence[seq_index]:
			seq_index += 1
		if seq_index == len(sequence):
			return True
	
	return False