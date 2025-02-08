"""
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

Example 1:
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

Example 2:
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.

Example 3:
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
"""
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

from typing import List
class Solution:
    @timed
    def check(self, nums: List[int]) -> bool:
        # Set `n` to the length of `nums` array
        # This will be the number of non-decreasing items required to return True
        n = len(nums)

        # Extend the list by itself, doubling it.
        # This allows you to search for a non-decreasing sequence of length `n`
        nums.extend(nums[:])

        # Set `scount` to track the non-decreasing sequence count
        scount = 0

        # Iterate over `nums`, checking if `num[i]` is less than `nums[i-1]`
        # If so, set `scount` back to 0. Increase `scount` by one
        # If `scount` reaches `n` return True

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                scount=0
            scount+=1
            if scount == n:
                return True
            
        # Return False because no sequence of non-decreasing numbers had n items
        return False
sol = Solution()
test_cases = [('True', [3,4,5,1,2]), ('False', [2,1,3,4]),('True', [1,1,1]), ('True', [6,10,6]), ('True', [7,9,1,1,1,3])]
for expected, case in test_cases:
    print(f"{sol.check(case)} - Expected: {expected}")