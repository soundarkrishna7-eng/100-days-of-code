def find_min(nums):
    left = 0
    right = len(nums) - 1
    result = nums[0]
    while left <= right:
        if nums[left] < nums[right]:
            result = nums[left]
            break
        mid = (right + left) // 2
        result = nums[mid]
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    return result

print(find_min([3,4,5,1,2]))      # expected: 1
print(find_min([4,5,6,7,0,1,2]))  # expected: 0
print(find_min([11,13,15,17]))    # expected: 11