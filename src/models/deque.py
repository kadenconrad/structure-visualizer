from .doublyLL import DoublyLL, DLLNode

class Deque:
    def __init__(self):
        self.list = DoublyLL()

    def push_front(self, new_item):
        new_node = DLLNode(new_item)
        self.list.prepend(new_node)

    def push_back(self, new_item):
        new_node = DLLNode(new_item)
        self.list.append(new_node)

    def pop_front(self):
        popped_item = self.list.head.data
        self.list.remove_value(self.list.head)
        return popped_item
    
    def pop_back(self):
        popped_item = self.list.tail.data
        self.list.remove_value(self.list.tail)
        return popped_item
    
    def peek_front(self):
        return self.list.head.data
    
    def peek_back(self):
        return self.list.tail.data