# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        array = [self.name]
        frontier = self.children.copy()
        
        while frontier != []:
            node = frontier[0]
            array.append(node.name)
            frontier = frontier[1:]
            frontier.extend(node.children)
        
        return array
