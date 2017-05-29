#Implementation of the Stack Datastructure using the lists

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, node):
        #insert the node at the start of the list
        self.stack.insert(0,node)
    def pop(self):
        #remove the first item from the list
        return self.stack.pop(0)
    def at(self, loc):
        #return the item at location loc
        return self.stack[loc]
    def isEmpty(self):
        return self.stack == []
    def size(self):
        return len(self.stack)
    def clone(self):
        return list(self.stack)
