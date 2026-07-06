def max_subarray(nums):
    current_sum = nums[0]
    best_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        best_sum = max(best_sum, current_sum)
    return best_sum

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expected: 6
print(max_subarray([1]))                                  # expected: 1
print(max_subarray([-3, -1, -2]))                        # expected: -1