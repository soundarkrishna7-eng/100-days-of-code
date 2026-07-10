def min_subarray_sum(target, nums):
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0

print(min_subarray_sum(7, [2, 3, 1, 2, 4, 3]))  # expected: 2
print(min_subarray_sum(4, [1, 4, 4]))             # expected: 1
print(min_subarray_sum(11, [1, 1, 1, 1, 1]))      # expected: 0