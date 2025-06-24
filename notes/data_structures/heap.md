# Heap
## Max Heap
A tree, most often a binary tree, that maintains the property that a node's key is greater than or equal to the node's children keys.

The root must have the maximum value.

Children have no relation. 

**Height**: logN
**Insert**: O(logN)
**Node Removal**: O(logN)

## Min Heap

A tree, also most often a binary tree, that maintains the property that a node's key is less than or equal to the node's children keys. 

The root must have the minimum value.

Children have no relation. 


### Heap Sort
Repeatedly removes the max and builds a sorted array in reverse order. Array must first be converted into a heap using heapify operation. 

#### Heapify
Starts on internal node with largest index and continues down to the root node at index 0. The largest internal node index is [N / 2] - 1
