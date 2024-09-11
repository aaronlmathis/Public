"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backtrack(temp):
            if len(temp) == len(nums):
                res.append(temp[:])  # Add a copy of temp_list to result
                return
            
            for num in nums:
                if num in temp:
                    continue  # Skip if num is already in the current permutation
                
                temp.append(num)  # Choose the number
                backtrack(temp)   # Explore further with this choice
                
                temp.pop()        # Backtrack: remove the last chosen number
        backtrack([])
        return res



sol = Solution()
nums = [1,2,3]
print(sol.permute(nums))
