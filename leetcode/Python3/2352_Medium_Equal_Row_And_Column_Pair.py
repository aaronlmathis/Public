"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
"""
from typing import List
from collections import defaultdict, Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        count = 0
        reverse = list(zip(*grid))
        print(reverse)
        row_counter = Counter(tuple(row) for row in grid)
        
        for col in reverse:
            count += row_counter[col]
        
        return count
        n = len(grid)
        # create columns grid to build columns for comparison
        columns = [[] * n for _ in range(n)]
        # Iterate through grid, appending cell value to columns grid
        for i in range(n):
            for j in range(n):
                columns[j].append(grid[i][j])

        # Create frequency counts for col and row hashes by converting lists into tuples
        col_hash = defaultdict(int)
        row_hash = defaultdict(int)

        for row in grid:
            row_hash[tuple(row)]+=1
        for col in columns:
            col_hash[tuple(col)]+=1
        
        # Iterate through row_hash, checking if the row is also in col_hash. if so, increment anwer by the frequency of row x col
        answer = 0
        for k, v in row_hash.items():
            if k in col_hash:
                answer += v * col_hash[k]
        return answer
    
sol = Solution()
grid = [[3,1,2,2],
        [1,4,4,5],
        [2,4,2,2],
        [2,4,2,2]]        

grid = [[3,1,2,2],
        [1,4,4,4],
        [2,4,2,2],
        [2,5,2,2]]
print(sol.equalPairs(grid))