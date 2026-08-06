def is_valid(s):
    stack = []
    matching = {')': '(', '}': '{',  ']': '['}
    for char in s:
        if char in matching:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()

        else:
            stack.append(char)
    return len(stack) == 0

print(is_valid("()"))      # expected: True
print(is_valid("()[]{}"))  # expected: True
print(is_valid("(]"))      # expected: False
print(is_valid("([)]"))    # expected: False
print(is_valid("{[]}"))    # expected: True