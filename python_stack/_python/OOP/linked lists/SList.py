from SLNode import SLNode
class SList:
    def __init__(self):
        self.head = None

    def addToFront(self,value):
        #create node to hold the val
        new_node = SLNode(value)
        #set the new node's next to the current head
        new_node.next = self.head
        #set the list's head to the new node
        self.head = new_node