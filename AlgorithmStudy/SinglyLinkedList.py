class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = None

    def add(self, data):
        if(self.curNode == None):
            self.head = Node(data)
            self.curNode = self.head
        else:
            self.curNode.next = Node(data)
            self.curNode = self.curNode.next
    
    def remove(self, node):
        if node != None:
            pass
