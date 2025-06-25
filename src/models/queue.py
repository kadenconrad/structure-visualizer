from .singly_LL import SLLNode, SinglyLL


class Queue:
    def __init__(self):
        self.list = SinglyLL()

    def enqueue(self, new_item):
        new_node = SLLNode(new_item)
        self.list.prepend(new_node)
        return new_node.data

    def dequeue(self):
        dequeued_node = self.list.head.data
        self.list.remove_after(None)
        return dequeued_node

    def peek(self):
        return self.list.head.data

    def is_empty(self):
        return self.list.is_empty()

    def size(self):
        return self.list.size()
