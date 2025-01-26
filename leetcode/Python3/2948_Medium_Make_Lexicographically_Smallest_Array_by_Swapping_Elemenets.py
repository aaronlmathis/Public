"""
You are given a 0-indexed array of positive integers nums and a positive integer limit.

In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.

Example 1:
Input: nums = [1,5,3,9,8], limit = 2
Output: [1,3,5,8,9]
Explanation: Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.

Example 2:
Input: nums = [1,7,6,18,2,1], limit = 3
Output: [1,6,7,18,1,2]
Explanation: Apply the operation 3 times:
- Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
- Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
- Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
We cannot obtain a lexicographically smaller array by applying any more operations.

Example 3:
Input: nums = [1,7,28,19,10], limit = 3
Output: [1,7,28,19,10]
Explanation: [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.
 
Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= limit <= 109
"""
from typing import List
from collections import defaultdict

class DisjointUnionSets:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]    
    
    def unionSets(self, x: int, y: int) -> None:
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return
        
        # Union by rank
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1   
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])
    
    def join(self, x: int, y: int) -> None:
        self.parent[self.find(y)] = self.find(x)
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        uf = UnionFind(n)
        for i in range(n - 1):
            if abs(nums[i] - nums[i + 1]) <= limit:
                uf.union(i, i + 1)

        groups = defaultdict(list)
        for i in range(n):
            groups[uf.find(i)].append(i)

        result = []
        for group in groups.values():
            group.sort(key=lambda i: nums[i])  # Sort indices within each group
            result.extend([nums[i] for i in group])

        return result         
        n = len(nums)
        dus = DisjointUnionSets(n)
        
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= limit:
                    dus.unionSets(i, j)

        groups = defaultdict(list)
        for i in range(n):
            groups[dus.find(i)].append(i)
        

        answer = nums[:]
        
        for indices in groups.values():
            sorted_values = sorted(answer[i] for i in indices)  # Sort values in the group
            for i, val in zip(sorted(indices), sorted_values):  # Assign sorted values back
                answer[i] = val

        return answer



sol = Solution()
nums = [1,60,34,84,62,56,39,76,49,38] # [1,56,34,84,60,62,38,76,49,39]
limit = 4 
print(sol.lexicographicallySmallestArray(nums, limit))