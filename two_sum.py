def two_sum_optimized(nums, target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement],i]
        else:
            seen[nums[i]] = i

print(two_sum_optimized([2, 7, 11, 15], 9))