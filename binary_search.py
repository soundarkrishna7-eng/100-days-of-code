def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] > target:
            right = mid - 1

    return -1

print(binary_search([-1,0,3,5,9,12], 9))  
print(binary_search([-1,0,3,5,9,12], 2))   
print(binary_search([5], 5)) 