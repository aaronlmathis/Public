"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        result = []
        top, bottom = 0, m-1
        left, right = 0, n-1

        while top <= bottom and left <= right:
            for col in range(left, right+1):
                result.append(matrix[top][col])
            top+=1

            for row in range(top, bottom+1):
                result.append(matrix[row][right])
            right-=1

            if top <= bottom:
                for col in range(right, left-1, -1):
                    result.append(matrix[bottom][col])
                bottom-=1

            if left <= right:
                for row in range(bottom, top-1, -1):
                    result.append(matrix[row][left])
                left+=1
        
        return result
        """
        result = []
        # Hash set tracking what coordinates have been visited
        visited = set()
        # Current direction
        #   - 0 - right, 1 - down, 2 - left, 3 - up
        direction = 0
        m = len(matrix)
        n = len(matrix[0])
        # Need a value to track total destinations and a value to track current move
        totalMoves = m * n
        currMove = 0
        x, y = 0, 0
        while currMove < totalMoves:
            result.append(matrix[x][y])
            visited.add((x, y))
            if direction == 0:
                if y == n-1:
                    direction = 1
                elif (x, y+1) in visited:
                    direction = 1
            elif direction == 1: 
                if x == m - 1:
                    direction = 2
                elif (x+1, y) in visited:
                    direction = 2
            elif direction == 2:
                if y == 0:
                    direction = 3
                elif (x, y-1) in visited:
                    direction = 3
            elif direction == 3:
                if x == 0:
                    direction = 0
                elif (x-1, y) in visited:
                    direction = 0

            if direction == 0:
                y+=1
            if direction == 1:
                x+=1
            if direction == 2:
                y-=1
            if direction == 3:
                x-=1

            currMove+=1
        
        return result
    """
sol = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(sol.spiralOrder(matrix))