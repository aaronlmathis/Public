from typing import List
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])

        heights = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    heights[i][j] = heights[i-1][j] + 1 if i > 0 else 1
        def count_histogram(row):
            stack = []
            sum_submatrices = 0
            cur_sum = 0
            
            for j in range(n):
                count = 1  # Frequency of the current height
                
                while stack and stack[-1][0] >= row[j]:
                    h, c = stack.pop()
                    cur_sum -= h * c
                    count += c
                
                stack.append((row[j], count))
                cur_sum += row[j] * count
                sum_submatrices += cur_sum
            
            return sum_submatrices

        # Step 3: Sum over all rows
        result = sum(count_histogram(heights[i]) for i in range(m))
        return result

sol = Solution()
mat = [[1,0,1],[1,1,0],[1,1,0]]
mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
print(sol.numSubmat(mat))        

"""
2
m(m+1) //2 * n(n+1) //2
​
 × 
2

​
For each row i, create an array nums where: if mat[i][j] == 0 then nums[j] = 0 else nums[j] = nums[j-1] +1.
"""