class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
	    array.append(self.name)
	    frontier = self.children.copy()
		
	    while frontier != []:
		    node = frontier[0]
		    array.append(node.name)
		    frontier = node.children.copy() + frontier[1:]
		
	    return array

    def __repr__(self): 
        return self.name