# Problem: Contains Duplicate
# Approach: Set for fast O(1) lookups
# Time Complexity: O(n)

def contains_duplicate(nums):
    my_set = set()
    for i in range(len(nums)):
        if nums[i] in my_set:
            return True
        elif nums[i] not in my_set:
            my_set.add(nums[i])
    return False

print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))