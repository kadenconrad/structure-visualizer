import time
from typing import Optional, Any, Union

ALLOWED_TYPES = ["int", "str", "float", "list", "tuple", "bool", "set", "dict"]
TYPE_MAPPING = {"int": int, "str": str, "float": float, "list": list, "tuple": tuple, "bool": bool, "set": set, "dict": dict}
TYPE_VALUES = {int: 0, str: "", float: 0.00, list: None, tuple: None, bool: None, set: None, dict: None}

class Array:
    def __init__(self, length: int, array_type: str, values: Optional[list]):
        # array_type param validity checks, ends with array_type becoming self.type attribute. `array_type` was originally passed as `type but i changed it when i added the type() func in line 13.
        if not array_type:
            raise ValueError(f"Type not specified. Please specify array type. Allowed types: {', '.join(ALLOWED_TYPES)}")
        if type(array_type) != str:
            raise TypeError(f"Array type must be given as a string. Please use quotation marks as shown here: : {', '.join(ALLOWED_TYPES)}")   
        if array_type.lower().strip() not in ALLOWED_TYPES:
            raise TypeError(f"Type: {array_type} array not permitted. Please use an allowed type: {', '.join(ALLOWED_TYPES)}") 
        self.type = TYPE_MAPPING[array_type.lower().strip()]

        # length param validity checks
        if not length:
            raise ValueError(f"Length not specified. Please specify array length.")    
        try:
            length = int(length)
            if length < 0 or length == 0:
                raise ValueError(f"Array length cannot be negative!")
        except TypeError:
            raise TypeError("Length must be an integer!")
        self.length = length

        # values param validity checks
        if not values:
            self.values = list([TYPE_VALUES[self.type] for i in range(length)])
        elif isinstance(values, list) != True:
            raise TypeError("Values must be list type")
        elif len(values) > length:
            raise TypeError("Values length can't surpass length parameter!")
        
        for i in set(values):
            if isinstance(i, self.type) != True:
                raise TypeError("Array elements must be of the same type!")
        if len(values) < length:
            leftover = length - len(values)
            self.values = values
            for i in range(leftover):
                self.values.append(TYPE_VALUES[self.type])
        self.length = length

    def traverse(self):
        print(f"🟡 traverse debug: current array state – pre-traversal {self.values}")
        for element in self.values:
            time.sleep(0.25)
            print(element)
        print(f"🟡 traverse debug: current array state – post-traversal {self.values}")
        return self.values
    
    def insert(self, element, index):
        if isinstance(index, int) != True:
            raise TypeError("Index must be an integer value")
        if type(element) != self.type:
            if element != None:
                raise TypeError(f"Element must be {self.type} or None type, but it is {type(element)}")
        self.values[index] = element
        return self.values
    
    def delete(self, index):
        self.values[index] = TYPE_VALUES[self.type]
        return self.values

    def search(self, index: Optional[int], value=None):
        if index == None and value == None:
              raise ValueError("Must provide either index or value")
        try:
            if type(index) == int:    
                if index > self.length:
                    raise ValueError("Index out of range")
                elif index < self.length:
                    raise ValueError("Index out of range")
        except TypeError:
             raise ValueError("Index must be an integer value")
        ### I don't wanna decide all this rn

    def display(self):
         print(self.values)
         return self.values
    
# ---LINKED LIST---
class Node:
    def __init__(self, data: Optional[Any], next: Optional['Node']): # Head has no data just pointer
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.tail = Node(data=None, next=None)
        self.head = Node(data=None, next=self.tail)

    def display(self):
        display_val = self.head.next
        while display_val is not self.tail:
            print(display_val.data, end=", ")
            display_val = display_val.next

    def insert_at_beginning(self, value):
        new_node = Node(data=value, next=self.head.next)
        self.head.next = new_node
        print("\nNew List: ", end="")
        self.display()

    def insert_at_position(self, position_value, value):
        check_value = self.head
        while check_value.data is not position_value:
            check_value = check_value.next
            if check_value is self.tail:
                raise ValueError(f"Node with position value: {position_value} not found. Is it the right type? Value provided is: {type(position_value)} type.")
        new_node = Node(value, check_value.next)
        check_value.next = new_node
        print("\nNew List: ", end="")
        self.display()

    def insert_at_end(self, value):
        node = self.head
        while node.next is not self.tail:
            node = node.next      
        new_node = Node(data=value, next=self.tail)
        node.next = new_node
        print("\nNew List: ", end="")
        self.display()

    def deletion_at_beginning(self):
        node_to_delete = self.head.next
        self.head.next = node_to_delete.next
        print("\nNew List: ", end="")
        self.display()

    def deletion_at_end(self):
        node = self.head
        while node.next is not self.tail:
            last = node
            node = node.next
        last.next = self.tail
        print("\nNew List: ", end="")
        self.display()
    
    def deletion_at_position(self, position):
        node = self.head
        while node.next.data is not position:
            node = node.next
            if node is self.tail:
                raise ValueError(f"Node with position value: {node.next} not found. Is it the right type? Value provided is: {type(node.next)} type.")
        position_value = node.next
        new_next = position_value.next
        node.next = new_next
        print("\nNew List: ", end="")
        self.display()

#---DOUBLY LINKED LIST---
class DoublyLinkedNode(Node):
    def __init__(self, data: Optional[Any], prev: Optional['Node'], next: Optional['Node']):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = DoublyLinkedNode(data=None, prev=None, next=None)
        self.tail = DoublyLinkedNode(data=None, prev=self.head, next=None)
        self.head.next = self.tail

    def display(self):
        display_node = self.head
        while display_node is not self.tail:
            print(display_node.data, sep=", ")


    """Doubly Linked Insertion Methods:
        REQUIREMENTS
        * Initiate new node with previous node and next node
            - Insertion position as next unless inserting at beginning
        * Update preceding node's `.next` attribute to new node
        * Update subsequent node's `.prev` attribute to new node
    """
    def insert_at_beginning(self, value):
        current_next = self.head.next
        new_node = DoublyLinkedNode(data=value, prev=self.head, next=current_next)
        self.head.next = new_node
        current_next.prev = new_node

    def insert_at_position(self, position_value: Any, value: Any):
        start_node = self.head
        while start_node.data is not position_value:
            start_node = start_node.next
            current_next = start_node.next
        new_node = DoublyLinkedNode(data=value, prev=start_node, next=current_next)
        start_node.next = new_node
        current_next.prev = new_node


    def insert_at_end(self, value):
        current_prev = self.tail.prev
        new_node = DoublyLinkedNode(data=value, prev=current_prev, next=self.tail)
        self.tail.prev = new_node
        current_prev.next = new_node


    def deletion_at_beginning(self):
        current_next_to_delete = self.head.next
        current_next_to_keep = current_next_to_delete.next
        self.head.next = current_next_to_keep
        current_next_to_keep.prev = self.head
        

if __name__ == "__main__":
    my_LL = LinkedList()
    my_LL.display()
    my_LL.insert_at_beginning(1)
    my_LL.insert_at_position(position_value=1, value=2)
    my_LL.insert_at_end(3)
    my_LL.deletion_at_end()
    my_LL.deletion_at_position(2)
    my_LL.deletion_at_beginning()


    # ---ARRAY---
    # my_array = Array(6, "int", [1, 2, 3, 4])
    # print("Should be [1, 2, 3, 4, 0, 0]")
    # my_array.display()
    # my_array.traverse()
    # my_array.insert(5, 5)
    # print("Should be [1, 2, 3, 4, 0, 5]")
    # my_array.display()
    # my_array.traverse()
    # my_array.delete(0)
    # print("Should be [0, 2, 3, 4, 0, 5]")
    # my_array.display()
    # my_array.traverse()




# -- Terminal Results
# Should be [1, 2, 3, 4, 0, 0]
# [1, 2, 3, 4, 0, 0]
# 🟡 traverse debug: current array state – pre-traversal [1, 2, 3, 4, 0, 0]
# 1
# 2
# 3
# 4
# 0
# 0
# 🟡 traverse debug: current array state – post-traversal [1, 2, 3, 4, 0, 0]
# Should be [1, 2, 3, 4, 0, 5]
# [1, 2, 3, 4, 0, 5]
# 🟡 traverse debug: current array state – pre-traversal [1, 2, 3, 4, 0, 5]
# 1
# 2
# 3
# 4
# 0
# 5
# 🟡 traverse debug: current array state – post-traversal [1, 2, 3, 4, 0, 5]
# Should be [0, 2, 3, 4, 0, 5]
# [0, 2, 3, 4, 0, 5]
# 🟡 traverse debug: current array state – pre-traversal [0, 2, 3, 4, 0, 5]
# 0
# 2
# 3
# 4
# 0
# 5
# 🟡 traverse debug: current array state – post-traversal [0, 2, 3, 4, 0, 5]