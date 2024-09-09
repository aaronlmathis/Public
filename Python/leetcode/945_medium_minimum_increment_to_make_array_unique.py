"""
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
Return the minimum number of moves to make every value in nums unique.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown that it is impossible for the array to have all unique values with 5 or less moves.
"""
from typing import List
from collections import Counter

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        def find_next_available_unique(existing_numbers):
            next_unique = 1
            while next_unique in existing_numbers:
                next_unique += 1
            return next_unique
        nums.sort()
        print(nums)
        count = Counter(nums)
        existing_numbers = set(nums)
        next_unique = find_next_available_unique(existing_numbers)
        replaced = set()
        moves_count = 0
        i = 0
        while i < len(nums):
            if count[nums[i]] > 1:
                if nums[i] not in replaced:
                    replaced.add(nums[i])
                    next_unique = find_next_available_unique(existing_numbers)
                    moves_count += abs(nums[i] - next_unique)
                    nums[i] = next_unique
                    existing_numbers.add(nums[i])
            i+=1
        




        print(existing_numbers)
        print(next_unique)
        print(nums)
        return moves_count
        
sol = Solution()
nums = [2,2,2,1]
print(sol.minIncrementForUnique(nums))        