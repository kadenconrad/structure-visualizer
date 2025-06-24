## Selection sort:
**Best case**: Ω(n^2)
**Average case**: Θ(n^2)
**Worst case**: O(n^2)
Comparison based; not fast.


Treats input as two parts, *sorted* and *unsorted*. Place an index pointer at the first position, *this is where we want the smallest value*, set another index pointer equal to the first index pointer's value and iterate through the list, keeping track of the *minimum value* in the list. Once the iteration is complete, swap the value of the current minimum with the first index pointer. 

Like repeatedly finding the smallest card in a deck of cards and placing it in the correct position. 

```python
def selection_sort(nums):
    for i in range(len(nums)-1):
        cur_min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[cur_min]:
                cur_min = j
        nums[cur_min], nums[i] = nums[i], nums[cur_min]
    return nums
```
---

## Insertion sort: 
**Best case**: Ω(n)
**Average case**: Θ(N^2)
**Worst case**: O(n^2)
Comparison based; not fast.

Treats array as two parts, unsorted and sorted. Take two index pointers, starting at index 1 *(one index to the right of the first index)*, and compare the value at that index to the value at the index before it. If the value at the index before it is < the current index's value, swap the values and decrement the second pointer to compare the value with the value before it.

Initialize the first pointer in an outer for loop and *set the second pointer's value* to the value of the *first pointer*. Then, declare a while loop that lasts under these conditions: 
- The second pointer's value stays above 0
- The element at the second pointer's index position is *less than* the element in front of it.
If these conditions are met, swap the two elements and decrement the second pointer.

**If list is nearly sorted**: Insertion sort is *better* than selection sort because it can perform closer to O(n). 


```python
def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums
```

---

## Shell sort: 
**Best case**: Ω(n log n)
**Average case**: Θ(N^1.5)
**Worst case**: O(n (log n)^2)
Comparison based; not fast.

An optimization of insertion sort using interval comparisons. Shell sort takes (or calculates) a gap value and sorts through the list as subarrays using insertion sort. Though ideal gap values exist, any gap values can be chosen as long as 1 is the last value.

*In the textbook, sum of the gap values == the number of times insertion_sort_interleaved() is called*

```python
def shell_sort(nums):
    gap = len(nums) // 2
    while gap > 0:
        for i in range(gap, len(nums)):
            j = i
            while j > gap and nums[j-gap] > nums[j]:
                nums[j], nums[j-gap] = nums[j-gap], nums[j]
                j -= gap
        gap //= 2
```
---

## Quick sort 
**Best case**: Ω(n log n)
**Best case**: Ω
**Average case**: Θ(n log n)
**Worst case**: O(n^2)
Comparison based; fast.

Generally two functions: partition and quicksort. There are multiple partition algorithms, the a common, efficient one being **Hoare's Partition** algorithm, where the *first element* of the given array is assumed as the *pivot* element. 

**Hoare's Partition**: A pointer `i` is initialized at the start of the array and `j` at the end. `i` is incremented to the right until an element greater than or equal to the pivot is found. `j` is incremented to the left until an element less than or equal to is found. If `i` points to an element >= pivot AND `j` points to an element <= the pivot, swap them. Once the pointers cross, the partitioning is complete

The **Quick Sort** algorithm uses a similar exit condition. If i < j, it calls `partition(nums, i, j)` and recursively calls quicksort with the return value of `partition()`, once as the high value *(-1 to account for pivot point)* and then as the low value *(+1 to accound for pivot point)*

```python
def partition(nums, i, j):
    pivot = nums[0]
    while True
        i += 1 # could start never ending loop without this
        while pivot > nums[i]:
            i += 1
        while pivot < nums[j]:
            j -= 1
        if i > j:
            return j
        nums[i], nums[j] = nums[j], nums[i]
    
```

```python
def quicksort(nums, i, j):
    if i < j:
        pivot = partition(nums, i, j)

        quicksort(nums, i, pivot - 1)
        quicksort(nums, pivot+1, j)
    return nums
```
---

## Merge sort: 
**Best case**: Ω(n log n)
**Average case**: Θ(n log n)
**Worst case**: O(n log n)
Comparison based; fast.

---

## Heap sort: 
**Best case**: Ω(N)
**Average case**: Θ(n log n)
**Worst case**: O(n log n)
Comparison based; fast.

---

## Radix sort:
**Best case**: Ω(n)
**Average case**: Θ(N)
**Worst case**: O(n)
Not comparison based; fast. Subdivides arrays into integer digits. 