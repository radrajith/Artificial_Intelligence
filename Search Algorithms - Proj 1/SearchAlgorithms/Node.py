#implementation of the tree. Each node has 4 children.

class Node:
    up = 0;
    down = 1;
    left = 2;
    right = 3;
    parent = -1;
    def __init__(self, parent):
        self.node = []
        self.parent = parent
    def addUp(self, child):
        self.node[self.up] = [child, 'up']
    def addDown(self, child):
        self.node[self.down] = [child, 'down']
    def addLeft(self, child):
        self.node[self.left] = [child, 'left']
    def addRight(self, child):
        self.node[self.right] = [child, 'right']
    def getParent(self, parent):
        return self.parent
