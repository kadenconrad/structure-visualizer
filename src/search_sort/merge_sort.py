def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2

    l_half = nums[:mid]
    r_half = nums[mid:]

    sorted_l = merge_sort(l_half)
    sorted_r = merge_sort(r_half)

    return merge(sorted_l, sorted_r)

def merge(sorted_l, sorted_r):
    result = []
    l = 0
    r = 0

    while l < len(sorted_l) and r < len(sorted_r):
        if sorted_l[l] <= sorted_r[r]:
            result.append[l]
            l += 1
        else:
            result.append[r]
            r += 1
    while l < len(sorted_l):
        result.append(sorted_l[l])
        l += 1
    while r < len(sorted_l):
        result.append(sorted_r[r])
        r += 1
    return result
        