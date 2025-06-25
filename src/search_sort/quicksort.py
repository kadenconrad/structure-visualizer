from src.models._array import Array


def partition(nums: Array, l, h):
    pivot = nums.get_index_data(h)
    i = l - 1

    for j in range(l, h):
        if nums.get_index_data(j) <= pivot:
            i += 1
            temp = nums.get_index_data(i)
            nums.set_index(i, nums.get_index_data(j))
            nums.set_index(j, temp)

    temp = nums.get_index_data(i + 1)
    nums.set_index(i + 1, nums.get_index_data(h))
    nums.set_index(h, temp)

    return i + 1


def quicksort(nums: Array, l=0, h=None):
    if h == None:
        h = nums.size - 1

    if l < h:
        pivot_index = partition(nums, l, h)
        quicksort(nums, l, pivot_index - 1)
        quicksort(nums, pivot_index + 1, h)
    return nums
