"""
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.


"""
from typing import List        
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        
        def rotate_90(mat):
            for i in range(len(mat)):
                for j in range(i, len(mat[0])):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            
            for i in range(len(mat)):
                mat[i].reverse()


        for _ in range(3): # a Square can be rotated 90 degrees 4 times.
            rotate_90(mat)
            if mat == target:
                return True            
        return False
    
mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
sol = Solution()
print(sol.findRotation(mat, target))