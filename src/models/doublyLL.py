class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLL:
    """
    Node params can be node or node's value
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if self.head == None:
            print("Nothing to display.")
        else:
            current_node = self.head
            print("\n[", end="")
            while current_node != None:
                print(current_node.data, end="")
                if current_node.next != None:
                    print(", ", end="")
                current_node = current_node.next
            print("]")

    def search(self, target_val):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == target_val:
                return cur_node
            cur_node = cur_node.next
        raise ValueError(f"Value {target_val} not found in list.")

    def append(self, new_val):
        if isinstance(new_val, DLLNode) == False:
            new_val = DLLNode(new_val)

        if self.head is None:
            self.head = new_val
            self.tail = new_val

        else:
            self.tail.next = new_val
            new_val.prev = self.tail
            self.tail = new_val

    def prepend(self, new_val):
        if isinstance(new_val, DLLNode) == False:
            new_val = DLLNode(new_val)

        if self.head is None:
            self.head = new_val
            self.tail = new_val

        else:
            self.head.prev = new_val
            new_val.next = self.head
            self.head = new_val

    def insert_after(self, cur_node, new_val):
        if isinstance(new_val, DLLNode) == False:
            new_val = DLLNode(new_val)

        if isinstance(cur_node, DLLNode) == False and cur_node is not None:
            cur_node = self.search(cur_node)

        if cur_node is None:
            self.head = new_val
            self.tail = new_val

        elif cur_node == self.tail:
            cur_node.next = new_val
            new_val.prev = cur_node
            self.tail = new_val

        else:
            next_node = cur_node.next
            new_val.next = next_node
            new_val.prev = cur_node
            next_node.prev = new_val
            cur_node.next = new_val

    def remove_value(self, cur_node):
        prev_node = cur_node.prev
        next_node = cur_node.next
        cur_node.prev, cur_node.next = None, None  # clean up to reuse (if node was created as variable it won't be garbage collected)
        if next_node is not None:
            next_node.prev = prev_node
        if prev_node is not None:
            prev_node.next = next_node
        if cur_node == self.head:
            self.head = next_node
        if cur_node == self.tail:
            self.tail = prev_node

    def is_empty(self):
        return self.head is None
    
    def size(self):
        if self.head is None:
            return 0
        else:
            cur_node = self.head
            count = 0
            while cur_node is not None:
                count += 1
                cur_node = cur_node.next
            return count