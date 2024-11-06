"""
You are given an array nums consisting of positive integers.
We call two integers x and y in this problem almost equal if both integers can become equal after performing the following operation at most once:
Choose either x or y and swap any two digits within the chosen number.
Return the number of indices i and j in nums where i < j such that nums[i] and nums[j] are almost equal.

Note that it is allowed for an integer to have leading zeros after performing an operation.

Example 1:
Input: nums = [3,12,30,17,21]
Output: 2

Explanation:
The almost equal pairs of elements are:
3 and 30. By swapping 3 and 0 in 30, you get 3.
12 and 21. By swapping 1 and 2 in 12, you get 21.
"""
from typing import List
from collections import defaultdict
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def can_be_almost_equal(x, y):
            # Convert numbers to strings
            str_x, str_y = str(x), str(y)
            
            # If lengths differ, they cannot be almost equal
            if len(str_x) != len(str_y):
                return False
            
            # Find positions where the digits differ
            diff_positions = []
            for i in range(len(str_x)):
                if str_x[i] != str_y[i]:
                    diff_positions.append(i)
            
            # To be "almost equal", there must be exactly 2 differences
            if len(diff_positions) == 2:
                # Check if swapping the differing digits in str_x makes it equal to str_y
                i, j = diff_positions
                swapped_x = list(str_x)
                swapped_x[i], swapped_x[j] = swapped_x[j], swapped_x[i]
                return swapped_x == list(str_y)
            
            return False

        # Count the number of valid (i, j) pairs where i < j and nums[i] and nums[j] are almost equal
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if can_be_almost_equal(nums[i], nums[j]):
                    count += 1
        return count



        return nums

sol = Solution()
nums = [226726,387862,880512,611522,343461,420841,334461,10813,226726,334461,80113,314364,10813,163067,134364,332548,413463,343416,236429,164332,566432,226726,334164,343461,143463,163229,667555,667555,343461,657565,343461,770521,285866,930657,236429,502387,313446,334461,12219,163760,144363,227626]
print(sol.countPairs(nums))