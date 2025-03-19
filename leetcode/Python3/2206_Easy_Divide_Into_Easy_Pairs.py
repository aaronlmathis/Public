"""
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.

Example 1:
Input: nums = [3,2,3,2,2,2]
Output: true
Explanation: 
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation: 
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
 

Constraints:
nums.length == 2 * n
1 <= n <= 500
1 <= nums[i] <= 500
"""
from typing import List
from collections import Counter, defaultdict
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"fname took ${after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper

class Solution:
    @timed
    def divideArray(self, nums: List[int]) -> bool:

        count = defaultdict(int)
        for num in nums:
            count[num] ^= 1

        for c in count.values():
            if c ^ 1 == 0:
                return False
        return True 
sol = Solution()
nums = [1,1,3,3]
nums=[12,8,19,5,4,8,14,18,20,12,1,14,9,15,14,5,11,4,7,2,2,11,18,5,13,20,16,7,1,6,13,13,14,3,2,1,12,11,4,17,12,13,19,6,17,4,19,2,4,4,7,19,7,6,9,14,8,2,6,9,17,9,14,1,13,11,11,8,12,13,10,9,11,6,9,20,19,4,10,10,19,12,13,10,3,16,13,10,20,5,14,20,13,14,3,7,15,7,10,1]
print(sol.divideArray(nums))        