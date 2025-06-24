class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLL:
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

    def append(self, value):
        if isinstance(value, SLLNode) != True:
            new_node = SLLNode(value)
        else:
            new_node = value

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        if isinstance(value, SLLNode) != True:
            new_node = SLLNode(value)
        else:
            new_node = value

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def search(self, target_val):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == target_val:
                return cur_node
            cur_node = cur_node.next
        raise ValueError(f"Value {target_val} not found in list.")

    def insert_after(self, target, new_node):
        if isinstance(new_node, SLLNode) == False:
            new_node = SLLNode(new_node)
        if isinstance(target, SLLNode) == False and target is not None:
            target_node = self.search(target)
        else:
            target_node = target

        if self.head == None:
            self.head = new_node
            self.tail = new_node

        elif self.tail == target_node:
            self.tail.next = new_node
            self.tail = new_node

        else:
            new_node.next = target_node.next
            target_node.next = new_node

    def remove_after(self, target):
        if isinstance(target, SLLNode) == False and target is not None:
            target_node = self.search(target)
        else:
            target_node = target

        if target_node is None: # remove head
            next_node = self.head.next
            cur_next = self.head
            self.head.next = None
            self.head = next_node

            if next_node == None:
                self.tail = None
        else:
            if target_node.next is not None:
                next_node = target_node.next.next
                cur_next = target_node.next
                cur_next.next = None
                target_node.next = next_node

            if next_node is None:
                self.tail = target_node

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