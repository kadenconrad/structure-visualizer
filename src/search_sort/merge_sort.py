from src.models._array import Array


def merge_sort(nums: Array):
    if len(nums.memory) <= 1:
        return nums
    mid = len(nums.memory) // 2

    l_half = Array(
        array_type=nums.array_type,
        size=len(nums.memory[:mid]),
        max_str_length=nums.str_arr_length - 1 if nums.array_type == "str" else None,
    )

    for i in range(len(nums.memory[:mid])):
        l_half.set_index(i, nums.get_index_data(i))

    r_half = Array(
        array_type=nums.array_type,
        size=len(nums.memory[mid:]),
        max_str_length=nums.str_arr_length - 1 if nums.array_type == "str" else None,
    )
    for i in range(len(nums.memory[mid:])):
        r_half.set_index(i, nums.get_index_data(i + mid))

    sorted_l = merge_sort(l_half)
    sorted_r = merge_sort(r_half)

    return merge(sorted_l, sorted_r, nums)


def merge(l: Array, r: Array, nums: Array):
    # i = left index, j = right index;
    i = 0
    j = 0
    idx = 0
    while i < len(l.memory) and j < len(r.memory):
        if l.get_index_data(i) <= r.get_index_data(j):
            nums.set_index(idx, l.get_index_data(i))
            idx += 1
            i += 1
        else:
            nums.set_index(idx, r.get_index_data(j))
            idx += 1
            j += 1
    while i < len(l.memory):
        nums.set_index(idx, l.get_index_data(i))
        idx += 1
        i += 1
    while j < len(r.memory):
        nums.set_index(idx, r.get_index_data(j))
        idx += 1
        j += 1

    return nums
