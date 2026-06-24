def valid_anagram(s, t):
    count = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] in count:
            count[s[i]] = count[s[i]] + 1
        else:
            count[s[i]] = 1
    for i in range(len(t)):
        if t[i] in count and count[t[i]] > 0:
            count[t[i]] = count[t[i]] - 1
        else:
            return False
    return True

print(valid_anagram('anagram', 'nagaram'))   # expected: True
print(valid_anagram('rat', 'car'))            # expected: False
print(valid_anagram('aacc', 'ccac'))          # expected: False (the one that broke earlier)