# Abstract Data Types (ADTs)
### What
Abstract Data Types, or ADTs, are data structures that are defined for their *behavior*, rather than their *implementation* or internal structure.

ADTs are *encapsulated* and *abstracted* (ok OOP) from users

### List:
Holds ordered data, indexed, can hold different types.

**Underlying Data Structure**: Array or Linked List

**Operations**: append, remove, search, print, insert, length, sort.


### Dynamic Array:
Will dynamically allocate memory for array as needed. 

**Underlyizing Data Structure**: Array
**Operations**:
    - `.prepend`: inserts a new items at the start of the list and all existing array elements are moved up by 1 position.

### Stack
Last In, First Out. Items are inserted or removed from the top. Not indexed. 
**Underlyizing Data Structure**: Linked list, Array
    - Array-based stacks must also declare allocationSize and length

**Unbounded stack**: A stack with no upper limit on length; length can increase indefinitely, so array allocation size must also be able to increase indefinitely (assuming its an array-based stack). This can be implemented with memory reallocation techniques, i.e., if length == allocationSize, the array is copied (new memory allocated) and allocationSize is doubled.

**Bounded stack**: A stack with a length that does not exceed a maximum value. 

**Operations**: 
    - `.pop`: Remove last element
    - `.push`: Add new element to stack
    - `.peek`: Look at last element
    - `.isEmpty`: Boolean value reflecting if stack is/is not empty
    - `getLength`: Returns number of items in a stack. 

### Queue
First In, First Out. Like standing in a line
**Underlyizing Data Structure**: Linked List

**Operations**:
    - `.enqueue`: Add someone to the end of the list
    - .`dequeue`: Remove from the front of the list
    - .`peek`

### Deque "deck"
Double-ended queue. Can be inserted and removed at both the front and back. 

**Underlyizing Data Structure**: Linked List
**Operations**:
    - `pushFront`
    - `pushBack`
    - `popFront`
    - `popBack`
    - `peekFront`
    - `peekBack`
    - `isEmpty`
    - `getLength`

### Bag
Useful for storing unordered items; duplicate items are allowed.
**Underlyizing Data Structure**: Array or Linked List

### Set
Unordered (or ordered) collection of non-duplicated items
**Underlyizing Data Structure**: Hash table (Python, Java, Javascript), binary search tree (C++)

Implemented differently in different languages, but there are two most common implementations:
1. **Hash-based Set**: Represented as a hash table, where each element in the set is stored in a bucket based on its hash code.
2. **Tree-based Set**: Represented as a binary search tree, where each node represents an element in the set.

### Types of Set Data Structures
1. **Unordered Set**: Unordered associative container implemented using a hash table. *All operations on the unordered set take constant time **O(1)** on average, but can go up to linear time **O(n)** worst case*.

2. **Ordered Set**: Implemented using balanced binary search trees and supports **O(log n)** lookups, insertions, and deletion operations.



### Priority Queue
Queue where each item has a priority and items with a higher priority are closer to the front
**Underlyizing Data Structure**: Heap
**Operation**:
    - `enqueue`
    - `dequeue`
    - `isEmpty`
    - `getLength`

### Dictionary (or Map)
Contain references to key value pairs
**Underlyizing Data Structure**: Hash table, binary tree
**Operations**: 