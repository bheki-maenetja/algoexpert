def nodeDepths(root):
    # Write your code here.
	frontier = []
	if root.left: frontier.append(root.left)
	if root.right: frontier.append(root.right)
	
	depth_level = 0
	depth_sum = 0
	while frontier != []:
		depth_level += 1
		depth_sum += depth_level * len(frontier)
		
		new_frontier = []
		for node in frontier:
			if node.left: new_frontier.append(node.left)
			if node.right: new_frontier.append(node.right)
		frontier = new_frontier
	
	return depth_sum

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None