def is_palindrome(s):
    Filtered = [c for c in s.lower() if c.isalnum()]
    left = 0
    right = len(Filtered) - 1
    while left < right:
        if Filtered[left] != Filtered[right]:
            return False
        else:
            left += 1
            right -= 1

    return True

print(is_palindrome("A man, a plan, a canal: Panama"))  # expected: True
print(is_palindrome("race a car"))                       # expected: False
print(is_palindrome(" "))                                # expected: True