def shell_sort(nums):
    gap = len(nums) // 2
    while gap > 0:
        i = 0
        for i in range(gap, len(nums)):
            j = i
            while j > 0 and nums[j-gap] > nums[j]:
                nums[j-gap], nums[j] = nums[j], nums[j-gap]
                j -= gap
        gap //= 2 
    return nums