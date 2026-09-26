def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, current, target):
        if target == 0:
            result.append(current[:])
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, target - candidates[i])
            current.pop()
    
    backtrack(0, [], target)
    return result

print(combination_sum([2,3,6,7], 7))  
print(combination_sum([2,3,5], 8))     