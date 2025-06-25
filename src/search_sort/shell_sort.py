def shell_sort(nums):
    if nums.size <= 1:
        return nums
    gap = nums.size // 2
    while gap > 0:
        for i in range(gap, nums.size):
            j = i
            while j > 0 and nums.get_index_data(j) < nums.get_index_data(j - gap):
                temp = nums.get_index_data(j)
                nums.set_index(j, nums.get_index_data(j - gap))
                nums.set_index(j - gap, temp)
                j -= gap
        gap //= 2
    return nums
