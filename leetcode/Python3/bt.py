nums = [1,2,3,4,5]
result = []
visited = set()
def backtrack(path):
    if len(path) == len(nums):
        result.append(path[:])
        return
    
    for num in nums:
        if num in visited:
            continue
        
        path.append(num)
        visited.add(num)
        backtrack(path)

        path.pop()
        visited.remove(num)


backtrack([])
print(result)