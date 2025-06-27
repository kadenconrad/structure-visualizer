from src.models._array import Array


def selection_sort(nums: Array):
    if nums.size <= 1:
        return nums
    for i in range(nums.size):
        cur_min = i
        for j in range(i + 1, nums.size):
            if nums.get_index_data(j) < nums.get_index_data(cur_min):
                cur_min = j
        temp = nums.get_index_data(i)
        nums.set_index(i, nums.get_index_data(cur_min))
        nums.set_index(cur_min, temp)
    return nums  # Θ(n^2), Ω(n^2), O(n^2)
