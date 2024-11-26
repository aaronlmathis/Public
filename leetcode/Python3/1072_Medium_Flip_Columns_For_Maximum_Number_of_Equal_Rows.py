"""
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

Example 1:

Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.

Example 2:
Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.

Example 3:
Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
"""
from typing import List
from collections import defaultdict
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Create default dict to use as hash map
        map = defaultdict(int)
        # Iterate through rows, if row starts with 0, store binary tuple in map as is
        # If row starts with 1, use bitwise XOR to flip each bit and store in map
        for row in matrix:
            canonical = tuple(col ^ row[0] for col in row)
            map[canonical] += 1
        # Return the maximum count found in map
        return max(map.values())
            
matrix = [[0,0,0],[0,0,1],[1,1,0]]
sol = Solution()
print(sol.maxEqualRowsAfterFlips(matrix))