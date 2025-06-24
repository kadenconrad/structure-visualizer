# Big O Notation and Time Complexity
## Constant Time Operations
- **Asignment of a fixed size data value**
```python
x = 1000
y = x
```
- **Addition, subtraction, multiplication, and division of fixed size integer or floating point vals**
```python
x = 10.4 - 2.6
y = 2 + 3
z = x - y
```
- **Comparison of two fixed size data values**
- **Read or write index from array**
- **Copying a pointer/reference to a variable *(a.k.a. not all characters in a string)***
```python
str2 = str1 # just stores a reference
```

## Asymptotic Bounding

**Asymptotic**: The nature of a graph or function as it reaches an untouchable or arbitrarily large ends.

**T(n)**: The *time* or *space* $T$ a function takes as it's input $n$ changes.

Every algorithm can be described as a function, has a **lower** and an **upper bound** that bounds the best *(lower bound, i.e., runs least lines of code possible)* and worst case *(upper bound, i.e., runs the most lines of code possible)* behavior for the function with another function. The **upper bound** function always be *greater than* or *equal to* your worst case performance and this should be proven with a constant. The **lower bound** function will always be *less than* or *equal to* your best case performance. 

An *ideal* bound is a tight bound.

## Asymptomtic Notation
**Algorithm Complexity Analysis**
O: **Worst Case**
Ω *(omega)*: **Best Case** 
Θ *(theta)*: **Average Case**

## O Notation
To determine the complexity of an algorithm (e.g., $5 + 13n + 7n^2$):
- Only keep the highest order term *(the one with the highest growth rate)* and discard the others: $O(7n^2)$
- Omit all constants: $O(n^2)$

## Common Big O Complexities
***O(1)* Constant Time**
```python
def find_min(x, y):
    if x < y:
        return x
    else:
        return y
    # O(3)
```
*IF a for loop is set to run for a fixed length that is NOT determined or affected by the input, $n$, it runs in constant time*

***O(log N) Logarithmic***: Cuts dataset in half
```python
def binary_search(nums, key):
    l = 0
    h = len(nums)        
    while l <= h:
        m = (h + l) // 2
        if nums[m] == key:
            return m
        elif nums[m] > key:
            h = m - 1
        elif nums[m] < key:
            l = m + 1
    return -1
    # O(log n)

```

***O(n) Linear***: One `for` loop
```python
def linear_search(nums, key):
    for i in range(nums):
        if nums[i] == key:
            return i
    return -1
    # f(N) = N(1 + 1) = O(n)
```

***O(n log n) Log-linear***: Cuts dataset in half in linear loop
```python
def merge_sort(nums, i, k):
    if i < k:
        j = (i + k) // 2
        merge_sort(nums, i, j)
        merge_sort(nums, j + 1, k)
        merge(nums, i, j, k)
```

***O(N^2) Quadratic***: Loop inside of a loop
```python
def selection_sort(nums):
    for i in range(len(nums)):
        index = 0
        for j in range(i + 1, len(nums)):
            if numbers[j] < numbers[0]:
                index = j
        temp = numbers[i]
        numbers[i] = numbers[index]
        numbers[index] = temp
```

***O(N^3) Cubed***: Loop inside of a loop, inside of a loop

***O(2^n) Exponential***: 
```python
def fibonacci(n):
    if (1 == n) or (2 == n):
        return n
    return fibonacci(n-1) + fibonnaci(n-2)
```


