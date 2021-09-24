def findClosestValueInBst(tree, target):
    # Write your code here.
	currentNode = tree
	closestValue = tree.value

	while currentNode != None:
		if abs(target - currentNode.value) < abs(target - closestValue):
			closestValue = currentNode.value
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			break

	return closestValue


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
