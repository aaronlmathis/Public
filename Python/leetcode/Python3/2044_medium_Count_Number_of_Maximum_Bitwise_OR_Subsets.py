"""
Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.
An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. 
Two subsets are considered different if the indices of the elements chosen are different.
The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
 

Example 1:

Input: nums = [3,1]
Output: 2
Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]
Example 2:

Input: nums = [2,2,2]
Output: 7
Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.
Example 3:

Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]

"""
from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bo = 0
        bo_count = 0

        # Calculate the maximum possible bitwise OR across all numbers in nums
        for num in nums:
            max_bo |= num

        def dfs(i, curr_or):
            nonlocal bo_count
            
            # If we've processed all elements
            if i == len(nums):
                # If the current OR equals the max OR, increase the count
                if curr_or == max_bo:
                    bo_count += 1
                return
            
            # First decision: include nums[i] and update the OR
            dfs(i + 1, curr_or | nums[i])
            
            # Second decision: exclude nums[i]
            dfs(i + 1, curr_or)

        # Start DFS from index 0 with an OR of 0
        dfs(0, 0)
        
        return bo_count
       

sol = Solution()
nums = [3, 2, 1, 5]
print(sol.countMaxOrSubsets(nums))

    