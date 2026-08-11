import math

def min_eating_speed(piles, h):
    left = 1
    right = max(piles)
    result = max(piles)
    while left <= right:
        mid = (right + left) // 2
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / mid)

        if total_hours <= h:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

print(min_eating_speed([3,6,7,11], 8))   # expected: 4
print(min_eating_speed([30,11,23,4,20], 5))  # expected: 30
print(min_eating_speed([1,1,1,1], 4))    # expected: 1