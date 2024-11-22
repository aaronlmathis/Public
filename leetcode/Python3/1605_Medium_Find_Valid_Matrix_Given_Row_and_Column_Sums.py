"""
You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

 

Example 1:

Input: rowSum = [3,8], colSum = [4,7]
Output: [[3,0],
         [1,7]]
Explanation: 
0th row: 3 + 0 = 3 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
                             [3,5]]

Example 2:
Input: rowSum = [5,7,10], colSum = [8,6,8]
Output: [[0,5,0],
         [6,1,0],
         [2,0,8]]
 
"""
from typing import List
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Calculate the length of rowSum and colSum
        r = len(rowSum)
        c = len(colSum)
        # Create r * c matrix, fill with zeros
        grid = [[0] * c for _ in range(r)]

        # Initialize two pointers, i for rowSum, j for colSum
        i, j = 0,0
        # Iterate while i and j while there are more rows/columns
        while i < r and j < c:
            # Calculate the minimum between rowsum[i] and colSum[j]
            x = min(rowSum[i], colSum[j])
            # Set grid[i][j] equal to x
            grid[i][j] = x
            # Subtract x from rowSum[i] and colSum[j]
            rowSum[i] -= x
            colSum[j] -= x
            # Increment i and j if roWsum[i] or colSum[j] equals zero. 
            i += (rowSum[i] == 0)
            j += (colSum[j] == 0)
        # Return Grid
        return grid

sol = Solution()
rowSum = [3,8]
colSum = [4,7] 
print(sol.restoreMatrix(rowSum, colSum))       
# Find the smallest rowSum or colSum, and let it be x. Place that number in the grid, and subtract x from rowSum and colSum. Continue until all the sums are satisfied.