def inOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
        return array
    else:
        return inOrderTraverse(tree.left, array) + [tree.value] + inOrderTraverse(tree.right, array)
    
    return array


def preOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
        return array
    else:
        return [tree.value] + preOrderTraverse(tree.left, array) + preOrderTraverse(tree.right, array)
    
    return array


def postOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
        return array
    else:
        return postOrderTraverse(tree.left, array) + postOrderTraverse(tree.right, array) + [tree.value] 
    
    return array