# Linked Lists
Linear data structure holding a collection of elements called **nodes** which each contain a *data value* and a *pointer* to the next value. **Doubly Linked Lists** also contain a pointer to the previous value.

## Terms
**Head**: In most implementations, the *true* head is just a *pointer* to the **first** node.

**Head Node**: The *first* node; *not the same object as the head pointer, since the first node can change.*

**Tail**: Just a *pointer* to the **last** node.

**Tail Node**: The *last* node; *not the same object as the tail pointer, since the last node can change.* Points to null. 

```python
class Node
    def __init__(self, value):
        self.value = value
        self.next = None
```

## Singly Linked Lists Operations
### Append
Inserts new node at the **end** of the list as the *last* node. 

- **If list is empty**: Both tail and head pointers update to point at new node.
- **If list not empty**: Current tail node's `next` pointer and tail pointer update to point at new node.

```python
def append(self, value):
    if self.head == None:
        self.head = newNode
        self.tail = newNode
    else:
        self.tail.next = newNode
        self.tail = newNode
```

### Prepend
Inserts new node at the **beginning** of the list as the *first* node.

- **If list is empty**: Updates both tail node and head node
- **If list not empty**: Only head node needs to be updated

```python
def prepend(self, value):
    newNode = Node(value)
    if self.head is None:
        self.head = newNode
        self.tail = newNode
    else:
        newNode.next = self.head
        self.head = newNode
```

### Insert
Inserts new node **after** a provided existing list node, which takes the current node (e.g., `curNode`), and the new value.

- **Insert at list's first node**: If *the head pointer is null*, the **head** and **tail** **pointers** should be pointed to new node.
- **Insert after list's tail node**: If the *head pointer is not null* and the *current node points to the tail node*, the **tail node's next** and **tail pointer points** to new node.
- **Insert in middle of list**: If the *head pointer is not null* and the c*urrent code does not point to the tail node*, the **new node's next** should be pointed to the **current node's next** and the **current node's next** should be points to **new node**. 

```python
def insert(self, cur_node, new_node):
    if isinstance(new_node, Node) != True:
        new_node = Node(new_node)
    if self.head == None:
        self.head = new_node
        self.tail = new_node
    elif cur_node == self.tail:
        self.tail.next = new_node
        self.tail = new_node
    else:
        new_node.next = cur_node.next
        cur_node.next = new_node
```

### RemoveAfter
Removes a specified existing node in a singly linked list. If the existing node is null, this operation removes the head node.

- **If current node is null**: Initialize a `next_node` from the *current* **head node's** *next* node. Set the head node to the new next_node. 

    - If next_node is null, *we removed the only node*. Set the tail to null.

- **Remove node after current node**: If the current node's next node *is not null*, initiate a `next_node` as the current_node's next-next node (skipping over a node–the node to be deleted). Set current_node's next node to next_node. *If next_node is null, the tail node was removed; set the tail node to the current node.*

```python
def removeAfter(self, cur_node):
    if cur_node is None:
        if self.head.next is not None:
            next_node = self.head.next
            self.head = next_node

        if next_node is None:
            self.tail = None
    else:
        if cur_node.next is not None:
            next_node = cur_node.next.next
            cur_node.next = next_node

        if next_node is None:
            self.tail = cur_node
```


### Search
Given a key, returns the **first node with matching data**, or **null** if no match was found. 

Checks the current node, initially the head node, and returns if match; else pointing to next and repeat until match is found or current node points to null.

**Time Complexity**: O(n)

```python
def search(self, target_val):
    current_node = self.head
    while current_node is not None:
        if current_node.value == target_val:
            return current_node
        current_node = current_node.next
```

---

## Doubly Linked List Operations
### Append
Inserts a new node after a lists tail node.