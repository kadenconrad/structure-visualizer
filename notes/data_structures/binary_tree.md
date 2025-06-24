# Binary Tree
In a binary tree, each node has UP TO **two** children: a *left child* and a *right child*. 

A node that has NO children, is called a **leaf**. A node with at LEAST one child is called an **internal node** and it is said to be that child's **parent**. If it's child has child nodes, it is said to be it's **anscestor**, as are it's parents and anscestor nodes. The top node, the one without a parent, is called the **root**.

A node's **depth** is the number of **edges** *(NOT nodes)* on the path from the *root* to the *node*, i.e, the root node has a depth of 0 and it's children have a depth of 1. All node's with the same depth form a tree **level**.

A tree's **height** is the largest depth of any node.

If every node on a binary tree contains 0 OR 2 children, it is **full**.

If all levels *except for the last level* on the binary tree contain two nodes and all nodes in the last level are left nodes, it is **complete**.

If all internal nodes have two children and all leaf nodes are at the same level, the tree is **perfect**. 


## Applications of trees
### File Systems
*Not a binary tree -- root has 3 children*
```
|-- /root # depth 0
    |-- /user1 # depth 1
        |-- data.json # depth 2
        |-- index.html 
    |-- /user2
        |-- /text_files
            |-- sample1.txt # depth 3
            |-- sample2.txt
        |-- /image_files
            |-- mountains.jpg
            |-- beach.jpg
    |-- /user3
        |-- /downloads
            |-- /research
```

- Files are always going to be leaf nodes, they do not hold any other files
- Folders can be leaf or internal nodes; an empty folder will be a leaf node (ex: `/research`) and an in-use folder will be an internal node (ex: `/user2`).

### Binary space partitioning
Repeatedly separating a region of space into 2 parts and cataloging objects contained within the regions. Created for graphics processing. Root node contains all objects, all objects that live on left side go in left child, all objects in right side go in right child, this can be repeated. This is to optimize performance.

### Binary Search Tree O(log n) !!!
Left children MUST be LESS than the parent; right children MUST be GREATER than the parent. Subtrees of left children, **must** follow the same rule as their parent relating to the relevant ancestor node *regardless of whether they are left or right children of their parent*. 

For ex:
```
        200
      /     \
    100     300
   /   \   /   \
  50  150 250  400 

        200
      / 
    100    
   /   \   
  50  150 # 150 MUST be <= 200; 
  it may be the right child of 100, it's still a LEFT subtree of 200, regardless of how it appears visually.

        200
            \
            300
           /   \
          250  400 
        # 250 must be >= 200
```

**Searching**: 
- First check if the current node (starts as root) is the key
- Then if the key is < than the current node, search left node
- If the key is > than the current node, search right node

In the worst case, the node does not exist or is a leaf and the algorithm will traverse all levels of the tree, making for a worst case number of comparisons for a non-perfect tree N + 1 and for a perfect tree $log_2N + 1$ (+ 1 to account for root node). N in this case stands for the height, not the number of nodes. 

### Successors and Predecessors
BST defines its order from smallest to largest.

A node's **successor** is its right subtree's leftmost child. Follow the left children until reaching a node with no left child. If it has no right subtree, its sucessor is the first ancestor that has this node in this left subtree. BASICALLY the successor is the next larger item idk why the first explanation was so convoluted ^ i feel like it leaves out a lot of info.

The largest item has no successor

A node's **predecessor** is more confusing but basically it just goes in descending order I'm pretty sure.

This sounds really confusing lol but it makes sense

```
        200
      /     \
    100     300
   /   \   /   \
  50  150 250  400 

  50 is the smallest, 100 is the second smallest, then 150, then 200, then 250, then 300, then 400.

  200's successor is 250 (right subtree's leftmost child), 250's successor is 300, 

```

### BST inorder traversal
A tree traversal algorithm visits all nodes in the tree once and performs an operation on each node. An **inorder traversal** visits all nodes in a BST from smallest to largest. 

### BST Insertion Order

Minimum N-node binary tree height is $h = log(N)$ and the maximum is $N - 1$ (because the root is at level 0). 

Inserting nodes in **random order** yields closer to minimum height, while inserting nodes in **sorted order** yields closer to maximum height. This is because inserting nodes in sorted order leads nodes to stack on the right side (or left if sorted in descending order). 

## AVL tree: Balanced BST
A BST with a height balance property and specific operations to rebalance the tree when a node is inserted or removed. 

These balancing operations keep the search **O(log n)**

A BST is **height balanced** if for any node the heights of the left and right subtrees differ by only 0 or 1. 

A node's **balance factor** is the left subtree height munus the right subtree height. 

### Balancing
**Height**: 
- If we have a null node, the height is -1
- If we have a single node, we have a height of 0
- Once we start adding nodes, H(n) = max(H(subtreeL), H(subtreeR))

***HEIGHT VALUES REQUIRES CHILD NODE HEIGHTS TO BE UPDATED SO WHEN A NEW NODE IS ADDED, THEY MUST BE UPDATED IN BOTTOM UP ORDER, STARTING AT THE NODE'S PARENT AND MOVING UP TO THE ROOT***

Balance Factor = Height of left subtree - height of right subtree or B(n) = H(L) - H(R)

AVL Tree = | B(n) | <= 1 (Balance factor must be less than or equal to 1)

```
            200 (h = 2) *b = -1*
          /     \
 (h= 0) 100     300 (h = 1) *b = 0 - (-1) = -1*
   *b = 0*     /   
             250 (h = 0) *b = -1 - -1 = 0*
```
*All leaf nodes have a balance factor of 0*

**Rotations**: Operations meant to fix imbalances; move nodes over to the other side of the tree. If tree is left-heavy, we do right rotation or **left-right** rotation. If tree is right-heavy, we do **left** rotation or **right-left** rotation.

Rotation is done *at* a node and occurs when one of the root child node's is shifted to become the root ndoe. 

### Red-Black Tree
Weakly balanced binary search tree. Ensures that thte longest path from a root to a leaf node is no more than twice as long as the shortest path. Reduces the number of rotations needed, but it is less balanced than an AVL tree.

BST with two node types, red and black, which supports operations that ensure the tree is balanced when a node is inserted or removed. 

- Root node must be black
- Red nodes must have no children
- All paths from a node to null leaves must have the same number of black nodes
- Must be a valid BST

