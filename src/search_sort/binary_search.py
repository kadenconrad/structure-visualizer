from src.models._array import Array


def binary_search(nums: Array, target):
    if nums.size == 0:
        return -1
    low = 0
    high = nums.size - 1
    while low <= high:
        mid = low + (high - low) // 2
        mid_value = nums.get_index_data(mid)
        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
