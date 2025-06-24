def partition(nums, l, h):
    pivot = nums[h]
    i = l - 1

    for j in range(l, h):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[h] = nums[h], nums[i+1]
    return i+1

def quicksort(nums, l, h):
    if h == None:
        h = len(nums)-1

    if l<h:
        pivot_idx = partition(nums, l, h)
        quicksort(nums, l, pivot_idx-1)
        quicksort(nums, pivot_idx+1, h)
    return nums