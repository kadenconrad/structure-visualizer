# Data Structures
## Array:
Stores a sequential collection of elements of the same type; with each element being stored in contiguous memory locations.

Elements can be accessed from their index, starting from 0.

### Types:
*Basis of Size*
- **Fixed Size Array**
- **Dynamic Size Array**: When array is lengthened, it's copied and moved to a new memory location, as 

*Basis of Dimension*
- **1D Array**: Elements are stored one after another
- **Multi-dimensional Array**: Array with more than one dimension; 2D, 3D, 4D, so on.
    - **2D Array**: A.K.A Matrix; array of arrays consisting of rows and columns. 
    - **3D Array**: An array of 2D arrays.

### Operations:
**Traversal**:
The process of accessing and processing each each element in an array in the specified order.
    - **Sequential Traversal**: Iterating through the array one element at a time from the first index -> last. Used for printing, searching, or performing calculations.
    - **Reverse Traversal**: Iterating from last element to first.

**Insertion**:
Adding element at specific position while maintaining existing order of elements. Requires shifting existing elements, unless position is end index.
1. Determine where new element should be inserted
2. Shift existing elements one position forward starting from the end
3. Insert new elements
4. Update size (if dynamic array)

    - **Insertion at Beginning**: Every element shifts one position right.
        - Least efficient case. Every element is affected.
    - **Insertion at Specific Index**: Every element after specified index shifts one position right.
    - **Insertion at the End**: No shifting required, only used in dynamic arrays.

**Deletion in Array**:
Removing an element while maintaining the order of remaining elements. Requires shifting elements to fill gap.
1. Identify index of element to be deleted
2. Shift elements that were to the right of the deleted element to the left
3. If it is a dynamic array, update the size

    - **Deletion at Beginning**: Every element shifts left by one position.
        - Least efficient. Affects all elements.
    - **Deletion at Specific Index**: Only elements after the index shift left.
    - **Deletion at End**: Simplest case. No shifting required.

**Searching in Array**:
Two main types of searching techniques in an array.
- **Linear Search**: Simplest search alogorithm.
    1. Traverses array one element at a time, comparing each element with target value.
    2. If match is found, returns index of element.
    3. If element is not found, search continues until end of array.

- **Binary Search**: Efficient for sorted array (inc or dec inclusive)
    1. Find middle element. If target value is equal to middle element, return its index.
    2. If target is less than middle element, search left half.
    3. If target is greater than middle element, search right half.
    4. Repeat until element is found, or search space is empty.


### List:
Ordered collection of elements that can be accessed by index. ADT

---
## Linked List:
Sequence of nodes containing an element and a reference to the next node.

### LINKED LISTS
[Go Deeper](linked_lists.md)

Linear collection of data linked by pointers; instead of a contiguous set of data, linked list nodes contain data values and a pointer to the next node.

*Linked lists can be used to implement various other data structures list stacks, queues, graphs, hash maps, etc*

- The *head* node: points to the first node in a linked list;
- The *tail* node: last node in a linked list; points to null

#### **Singly Linked Lists**
Point to only the next node; traversals are done in only one direction

**Access**: ***Θ(n)***; ***O(n)***
**Search**: ***Θ(n)***; ***O(n)***
**Insertion**: ***Θ(1)***; ***O(1)***
**Deletion**: ***Θ(1)***; ***O(1)***

#### **Doubly Linked List**
Point to both the previous and next node, 3 values in each node; traversals are done in only one direction

**Access**: ***Θ(n)***; ***O(n)***
**Search**: ***Θ(n)***; ***O(n)***
**Insertion**: ***Θ(1)***; ***O(1)***
**Deletion**: ***Θ(1)***; ***O(1)***



## [Binary Tree](./binary_tree.md)
Non-linear, hierarchical data structure where each node has *at most* **two** children: the **left child** and the **right child**. 

The *topmost* node is called the **root**, and the *bottom-most* nodes are called the **leaves**.

## [Hash tables](./hash_tables.md)
Used to quickly insert, look up, and remove elements. *Requires unique elements.* Uses hash function(s) to determine element bucket (similar to index, ish).

Most operations are performed in **O(1)**.
**Search**: ***Θ(1)***; ***O(n)*** *bc collisions*
**Insertion**: ***Θ(1)***; ***O(n)*** *bc collisions*
**Deletion**: ***Θ(1)***; ***O(n)*** *bc guess what.. collisions*


## [Heap](./heap.mp)
Complete binary tree, where for every node, the value of its children is either greater than or equal to its own value or less than or equal to its own value. Heaps usually are used to implement priority queues, where the smallest (min heap) or largest (max heap) element is always at the root of the tree.

**Access**: ***Θ()***; ***O()***
**Search**: ***Θ()***; ***O()***
**Insertion**: ***Θ()***; ***O()***
**Deletion**: ***Θ()***; ***O()***

## [Set](adts.md#set)

Stores a collection of distinct elements; each object *must be unique*. 


## [Graph](./graphs.md)
Non linear data structure that consists of vertices and edges. Vertices can be referred to as nodes.

### Types of Graphs
1. **Null Graph**: Graph with no edges; can have multiple verticies.
2. **Trivial Graph**: Graph with one single vertex; the smallest possible graph.
3. **Undirected Graph**: Graph where edges have no direction; nodes are unordered pairs in every edge.
4. **Directed Graph**: Edges have a direction. Nodes are ordered pairs.
5.  