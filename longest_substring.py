def length_of_longest_substring(s):
    new_dict = {}
    left_pointer = 0
    max_length = 0
    for right in range(len(s)):
        if s[right] in new_dict:
            left_pointer = max(left_pointer, new_dict[s[right]] + 1)
        new_dict[s[right]] = right
        max_length = max(max_length, right - left_pointer + 1)
    return max_length

print(length_of_longest_substring("abcabcbb"))  
print(length_of_longest_substring("bbbbb"))      
print(length_of_longest_substring("pwwkew")) 