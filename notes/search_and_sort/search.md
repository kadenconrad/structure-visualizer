# Search Algorithms
## Linear Search
Starts from the beginning of a list, checking each element until the search key is found or the end of list is reached.

**Time Complexity**: *O(n)*
**Runtime**: 1s/million elements *(Given that 1 microsecond/comparison)*

```python
def linear_search(vals, key):
    for i in range(len(vals)):
        if vals[i] == key:
            return i
```

## Binary Search
Searches a **SORTED** list by checking the midpoint index first; if the target value is less than the midpoint, it checks the midpoint of the left half of the array, if the target value is larger than the midpoint, it checks the midpoint of the right half. This is repeated until the element is found. 


**Time Complexity**: *O(log n)*
**Runtime**: 20microseconds per million elements *(Given that 1 microsecond/comparison)*
Calculate runtime as $log_2(n) + 1$

```python
def binary_search(nums, key):
    low = 0
    high = len(nums)
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == key:
            return mid
        
        if nums[mid] < key:
            low = mid + 1
        
        if nums[mid] > key:
            high = mid - 1
    return f"Key not found."
```
