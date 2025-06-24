# Graphs
## Adjacency and paths
Two vertices are **adjacent** if they are connected by an edge

**Path**: a sequence of edges leading from a source vertex to a destination vertex. The path length is the # of edges in the path.

**Distance**: The number of edges on the SHORTEST path between the vertices. 

## Applications of Graphs

- Maps and navigation
- Product recommendations
- Social and professional networks

## Adjacency lists
Vertex: [Adjacent, Vertices]

A *key advantage* is that each vertex appears at once and each edge appears twice; size of O(V + E). 

HOWEVER, determining whether two vertices are adjacent is O(V) because one vertex's adjacency list must be traversed looking for the other vertex. In most applications though, this isn't an issue because vertices are only adjacent to a small fraction of the other existing vertices, yielding a **sparse graph** (*a graph with far fewer edges than the maximum possible*.)


## Adjacency matrices
Each vertex is assign to a matrix row and column and a matrix element is 1 if the corresponding two vertices have an edge or is 0 otherwise. 

## Breadth-first search
Traversal that visits a starting vertex, then all vertices of distance 1 from that vertex, then distance 2, and so on, without revisiting a vertex.

*Visiting order of same distance doesn't matter, i.e., BFS traversal is NOT unique.*

### BFS Algorithm
Enques the starting vertex in a queue, while the queue is not empty, the algorithm dequeues a vertex from the queu, visits the dequeued vertex, enqueues that vertex's adjacent vertices, and repeats. 

When a vertex is encountered it has been **discovered** and the vertices in the queue are called the **frontier**.

## Depth-first search
Visits a starting vertex and then every vertex along each path starting from that vertex to the path's end before backtracking.

*Visiting order is not unique*

### DFS Algorithm
Pushes the starting vertex to a stack. While the stack is not empty, the algorithm pops the vertex from the top of the stack, if the vertex has not already been visited, the algorithm visits the vertex and pushes the adjacent vertices to the stack. 

## Types of Graphs
- **Directed Graphs**: *(Aka Digraph)* consists of vertices connected by directed edges
    - **Directed Edge**: A connection between a starting vertex and a terminating vertex.
    - *Adjacency only applies in one direction, flowing opposite of the graph*
- **Weighted Graphs**: Associates a *weight*, or *cost* with each edge, i.e., a flight cost between airports or connection speed between computers. 
    - **Path Length**: The sum of the edge weights in the path
    - **Negative Edge Weight Cycle**: Has a cycle length less than 0; a shortest path does not exist because each loop decreases cycle length further.