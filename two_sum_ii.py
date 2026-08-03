def two_sum_ii(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right :
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return[left + 1, right + 1]
        if current_sum > target:
            right -= 1
        if current_sum < target:
            left += 1

print(two_sum_ii([2, 7, 11, 15], 9))   # expected: [1, 2]
print(two_sum_ii([2, 3, 4], 6))         # expected: [1, 3]
print(two_sum_ii([-1, 0], -1))          # expected: [1, 2]