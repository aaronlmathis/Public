class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        """
        count = 0
        for i in range(len(stones)-1, -1, -1):
            for stone in stones:
                if stone != stones[i]:
                    if (stone[0] == stones[i][0]) or (stone[1] == stones[i][1]):
                        stones[i] = ['X','X']
                        count+=1
        return count
        """
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent.setdefault(x, x)
            parent.setdefault(y, y)
            parent[find(x)] = find(y)
        
        for x, y in stones:
            union(x, ~y)  # Use ~y to distinguish between rows and columns
        
        return len(stones) - len({find(x) for x in parent})
    
sol = Solution()
stones = [[0,1],[1,2],[1,3],[3,3],[2,3],[0,2]]


print(sol.removeStones(stones))
        