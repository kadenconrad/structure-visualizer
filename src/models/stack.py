from .singly_LL import SinglyLL, SLLNode

class Stack:
    def __init__(self):
        self.list = SinglyLL()

    def push(self, new_item):
        new_node = SLLNode(new_item)
        self.list.prepend(new_node)

    def pop(self):
        popped_item = self.list.head.data
        self.list.remove_after(None)
        return popped_item
    
    def peek(self):
        return self.list.head.data
    

