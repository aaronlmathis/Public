"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
 
Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

"""
from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i][j] = min( dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        ans = sum(sum(row) for row in dp)
        
        return ans

matrix = [
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
]
sol = Solution()
print(sol.countSquares(matrix))