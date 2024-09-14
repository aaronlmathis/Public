"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 
"""
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])  # m is the number of rows, n is the number of columns
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Convert mid index back to 2D indices
            row = mid // n
            col = mid % n
            mid_value = matrix[row][col]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
sol = Solution()
print(sol.searchMatrix(matrix, target))