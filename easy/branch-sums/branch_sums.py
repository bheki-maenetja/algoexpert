# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root, branch_sum = 0):
    # Write your code here.
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [branch_sum + root.value]
    else:
        return branchSums(root.left, branch_sum + root.value) + branchSums(root.right, branch_sum + root.value)
	
