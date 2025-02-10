from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
        
        return len(res )
sol = Solution()
nums = [1, 2, 3, 4, 5]
print(sol.permute(nums))