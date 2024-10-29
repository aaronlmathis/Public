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
        if not nums:
            return 0

        nums.sort()
        moves_count = 0
        current = nums[0]

        for num in nums[1:]:
            if num <= current:
                # If num is not greater than current, we need to increment it
                moves_count += current + 1 - num
                current += 1
            else:
                # Update current to the latest unique number
                current = num

        return moves_count
sol = Solution()
nums = [2,2,2,1]
print(sol.minIncrementForUnique(nums))        