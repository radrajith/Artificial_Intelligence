# implementation of the queue class

class MyQueue:

    def __init__(self):
        #contructor a list name queue
        self.queue = []

    def enqueue(self, node):
        #insert the node at the last position
        self.queue.append(node)

    def dequeue(self):
        #remove the first node
        return self.queue.pop(0)
    def at(self, loc):

        #return the node at the location loc
        return self.queue[loc]
    def size(self):

        #return the size of the queue
        return len(self.queue)
    def isEmpty(self):

        #return a bool on weather the queue list is empty
        return self.queue == []
    def clone(self):

        #make independent copies of the queue
        return list(self.queue)
