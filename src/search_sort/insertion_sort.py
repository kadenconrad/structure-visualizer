from src.models._array import Array


def insertion_sort(nums: Array):
    if nums.size <= 1:
        return nums
    for i in range(1, nums.size):
        j = i
        while j > 0 and nums.get_index_data(j) < nums.get_index_data(j - 1):
            temp = nums.get_index_data(j)
            nums.set_index(j, nums.get_index_data(j - 1))
            nums.set_index(j - 1, temp)
            j -= 1
    return nums  # Ω(n); Θ(n^2); O(n^2)
