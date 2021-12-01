class MinMaxStack:
    def __init__(self):
        self.stack = []
    
    def peek(self):
        # Write your code here.
        return self.stack[-1]

    def pop(self):
        # Write your code here.
        return self.stack.pop()

    def push(self, number):
        # Write your code here.
        self.stack.append(number)

    def getMin(self):
        # Write your code here.
        return min(self.stack)

    def getMax(self):
        # Write your code here.
        return max(self.stack)