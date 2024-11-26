"""
You are given an n x n integer matrix. You can do the following operation any number of times:

    Choose any two adjacent elements of matrix and multiply each of them by -1.
    Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

Example 1:
Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.

Example 2:
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
"""
from typing import List
import heapq
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # Initialize Variables
        #   - negCount - int - count of negative numbers
        #   - minAbs - int - Minimum absolute value of any number in matrix
        #   - absSum - int - sum of absolute values of numbers in matrix
        negCount, minAbs, absSum = 0, float('inf'), 0

        # Iterate through each number in the matrix
        for row in matrix:
            for num in row:
                # During each iteration:
                #       - If num < 0, increase negative count by one
                #       - Get the absolute value of num
                #       - Find the minimum absolute value in matrix
                #       - Add num to the sum of absolute values of matrix
                if num < 0:         
                    negCount += 1
                num = abs(num)      
                minAbs = min(minAbs, num) 
                absSum += num  
        # If a zero is found (minAbs == 0) or there are an even number of negative numbers, return the sum of absolute values
        #   After all, 2 negatives cancel out, and a zero can cancel out any negative.
        #   Position in matrix doesn't matter, because you can perform infinite moves
        if negCount % 2 == 0 or minAbs == 0:
            return absSum
        # If there are no zeros and an odd amount of negative numbers, return the sum of the absolute numbers
        # You will always want the remaining negative number to be the smallest number in absolute value found.
        # Subtract the minAbs from absSum (because its no longer positive) and then subtract again because it is negative now.
        else:
            return absSum - minAbs - minAbs

#matrix = [[1,-1],[-1,1]]
matrix = [[2,9,3],[5,4,-4],[1,7,1]]
sol = Solution()

print(sol.maxMatrixSum(matrix))        

test =  [[[2,9,3],[5,4,-4],[1,7,1]],
        [[0,0,0],[0,0,0],[0,0,0]],
        [[-9,9,9,-9],[-10,10,7,5],[4,-8,-9,6],[10,2,-6,1]],
        [[-3,0,0],[0,0,0],[0,3,2]],
        [[-1,0,-1],[-2,1,3],[3,2,2]],
        [[-3,-4,-1,-2],[-2,-2,1,1],[1,6,-5,-3],[-3,-3,-9,-1]]]
