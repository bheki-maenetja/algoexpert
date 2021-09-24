# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
	sum_array = []
    current_branch = [root]
	branch_sum = root.value
	frontier = [node for node in (root.left, root.right) if node != None]
	
	while frontier != []:
		node = frontier[0]
		current_branch.append(node)
		children = [child for child in (node.left, node.right) if child != None]
		if children == []:
			sum_array.append(sum(n.value for n in current_branch))
			while not (current_branch[-1].left or current_branch[-1].right):
				current_branch.pop()
		frontier = children + frontier[1:]
	
	return sum_array
