def three_sum(nums):
    sorted_nums = sorted(nums)
    result = []
    for i in range(len(nums)):
        if sorted_nums[i] > 0:
            break
        if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
            continue
        left = i + 1
        right = len(sorted_nums) - 1
        while left < right:
            current_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
            if current_sum == 0:
                result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                left += 1
                right -= 1
            elif current_sum > 0:
                right -= 1
            else:
                left += 1
    return result

print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([0, 0, 0]))
print(three_sum([0, 1, 1]))