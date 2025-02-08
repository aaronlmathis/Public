"""
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.


Example 1:
Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 
Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 104
All elements in nums are distinct.
"""
from collections import defaultdict
from typing import List
import itertools
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"{fname} took {after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper

class Solution:
    @timed
    def tupleSameProduct(self, nums: List[int]) -> int:
        totals = defaultdict(int)

        # Faster pair generation using combinations
        for a, b in itertools.combinations(nums, 2):
            totals[a * b] += 1  # Direct multiplication

        # Optimized counting step
        return sum(4 * v * (v - 1) for v in totals.values() if v > 1)
    
sol = Solution()
nums = [2,3,4,6]
nums = [1,2,4,5,10]

nums = [2,3,4,6,8,12]#40
print(sol.tupleSameProduct(nums))
