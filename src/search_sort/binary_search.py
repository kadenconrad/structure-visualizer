def binary_search(nums, target):
    if len(nums) == 1:
        return 0
    
    l = 0
    h = len(nums)-1

    mid = l + (h - l) // 2

    if nums[mid] == target:
        return mid
    
    else:
        if nums[mid] < target:
            return binary_search(nums[mid+1:h], target)
        if nums[mid] > target:
            return binary_search(nums[l:mid-1], target)
        
nums = [1, 2, 3, 4, 5]

bs = binary_search(nums, 3)

print(bs)