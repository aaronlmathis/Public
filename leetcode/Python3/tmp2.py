"""
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
"""
from typing import List

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(n)]  # Initialize n x n matrix

        # Directions: Right, Down, Left, Up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, di = 0, 0, 0  # Start position and initial direction
        cur = 1  # Start filling from 1

        for _ in range(n * n):
            matrix[x][y] = cur
            cur += 1

            # Compute next position
            nx, ny = x + directions[di][0], y + directions[di][1]

            # Check boundary or if cell is already filled
            if nx < 0 or ny < 0 or nx >= n or ny >= n or matrix[nx][ny] != -1:
                di = (di + 1) % 4  # Change direction (right → down → left → up)
                nx, ny = x + directions[di][0], y + directions[di][1]

            x, y = nx, ny  # Move to the next position

        return matrix

# Example usage
sol = Solution()
matrix = sol.generateMatrix(3)
for row in matrix:
    print(row)


sol = Solution()
n = 4
print(sol.generateMatrix(n))        