def search_matrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n -1
    while left <= right:
        mid = (right + left) // 2
        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True
        if matrix[row][col] < target:
            left = mid + 1
        if matrix[row][col] > target:
            right = mid - 1

    return False

print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))   # True
print(search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))  # False
print(search_matrix([[1]], 1))                                       # True