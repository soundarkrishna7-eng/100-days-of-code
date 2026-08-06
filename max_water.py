def max_water(height):
    left = 0
    right = len(height) - 1
    best_water = 0
    while left < right:
        current_water = (right-left) * min(height[left], height[right])
        best_water = max(best_water, current_water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best_water


print(max_water([1,8,6,2,5,4,8,3,7]))  # expected: 49
print(max_water([1,1]))      