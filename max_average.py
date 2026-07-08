def find_max_average(nums, k):
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]

    max_average = window_sum / k

    for i in range(1, len(nums) - k + 1):
        window_sum = window_sum - nums[i-1] + nums[i+k-1]
        max_average = max(max_average, window_sum / k)

    return max_average

print(find_max_average([1, 12, -5, -6, 50, 3], 4)) 