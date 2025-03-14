"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
"""
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # List to store all possible combination lists.
        combinations = []

        # Helper backtracking function
        def backtrack(start: int, path: set) -> None:
            # Base case - `path` is k size. Add to `combinations`
            if len(path) == k:
                combinations.append(list(path))
                return
            # Iterate through numbers from start to n+1
            for i in range(start, n+1):
                # Add `i` to path
                path.add(i)
                # Explore further
                backtrack(i+1, path)
                # Remove i and backtrack
                path.remove(i)

        backtrack(1, set())
        return combinations

n = 4
k = 2        
sol = Solution()
print(sol.combine(n, k))