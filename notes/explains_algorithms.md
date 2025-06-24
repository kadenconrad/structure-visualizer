# Explains Algorithms
**Algorithm**: A terminible set of instructions that executes in a specific order to perform a particular task
- Takes *input*
- Processes input through terminible list of steps
- Returns *output*

### Characteristics of an Algorithm
- **Unambiguity**: Algorithms must be concise an specific
- **Finiteness**: Algorithms must know when to stop.
- **Well-defined inputs**: Garbage in, garbage out.
**Language Independent**: Algorithms should be able to be written in multiple languages.
**Effectiveness and feasibility**: Will it be more complicated to write the algorithm than to do the job one time? Is it possible?
**Well-defined Output**: There should be a defined output that you are looking for.

### Factors of an Algorithm
**Modularity**: Broken down into small steps
**Correctness**: Given the inputs, does it produce the desired output?
**Maintainability**: No significant changes are required when redefining the algorithm
**Functionality**: Uses the logical steps to solve a real-world problem.
**Robustness**: Ability to define problem clearly
**User-friendly**: Easily explained
**Simplicity**: Simple to understand
**Extensibility**: Extensibile for other designers/programmers to use.

### Pros & Cons of Algorithms
**Pros**
- Efficiency; streamlines processes
- Reproducibility
- Problem-solving
- Scalability
- Automation

**Cons**
- Complex; time consuming and challenging
- Limitations; may not have efficient solutions
- Resource intensive
- Inaccuracy
- Maintenance

### Example Algorithms
- **Brute Force Algorithms**: Guess every possible combination until guessing the right password
- **Searching Algorithm**: Finding an element in a data structure
- **Sorting Algorithm**
- **Encryption**
- **Hashing**
- **Recursive Algorithm**
- **Divide and Conquer Algorithm**
- **Greedy Algorithm**: Opportunistic algorithm; choosing the best path at each decision, but might not choose the best result

### Complexity
How algorithms are measured
**Time Complexity**
- The amount of time required for an algorithm to complete, represented by how it scales according to input
- Expressed in Big O notation
- Calculated by counting the number of steps required to complete the execution

**Space Complexity**
- The amount of space or RAM an algorithm requires to solve a problem, represented by how it scales according to input.
- Expressed in Big O Notation

### Big-O Complexity
***n* = input; Big O Notation represents how something scales determined by the size of input**
![BigO Complexity Chart](../images/bigO_compChart.png)
***From Best to Worst***
- **O(1)**: *Constant or instant time*; complexity is unaffected by input size. Dream scenario.
- **O(log n)**: Quite a bit longer, but still very efficient. Grows by the log of the input size, seen often in binary search or binary tree traversal, when the input is being recursively divided in half. *Remember that the base is always 2 in Computer Science -> see: [Logarithms in Computer Science](logarithms.md)*
- **O(n)**: *Linear Time;* with every added unit, complexity grows by one unit. The linear search algorithm, in the worst case, must look through every element in an array.
- **O(n log n)**: With every added unit, complexity grows by one unit $\cdot log(n)$. Seen with merge sort, or quick sort (best, average case). 
- **O(n^2)**: With every added unit, complexity grows quadratically. Bubble sort, insertion sort.
- **O(2^n)**: 