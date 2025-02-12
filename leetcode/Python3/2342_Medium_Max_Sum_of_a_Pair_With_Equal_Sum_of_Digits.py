"""
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.


Example 1:
Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

Example 2:
Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
 

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
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
import heapq
from collections import defaultdict
class Solution:
    @timed
    def maximumSum(self, nums: List[int]) -> int:
        """ Helper function to return the sum of all digits in an integer. """
        def get_digit_sum(num: int) -> int:
            sum_total = 0
            while num:
                sum_total += num % 10
                num //= 10
            sum_total += num
            return sum_total

        # Dictionary (hashmap) k: digit sum, v: largest number seen
        common_sums = {}
        # Set `answer`` to -1, If there are no common digit sums, this will be returned.
        answer = -1
        
        # Iterate over `nums`, calculating digit sum of `num`
        # If the digit sum exists in `common_sums`:
        #   - Calculate max sum of the two numbers with common digit sums
        #   - If the existing number in `common_sums` is less than `num`, replace it
        # If not, add it to `common_sums`
        for num in nums:
            dsum = get_digit_sum(num)
            if dsum in common_sums:
                answer = max(answer, common_sums[dsum] + num)
                common_sums[dsum] = max(common_sums[dsum], num)
            else:
                common_sums[dsum] = num
        
        # Return answer, it should be either -1 or 
        # the largest sum found of numbers with common digit sums
        return answer



sol = Solution()
nums = [18,43,36,13,7]      
nums = [10,12,19,14]  
print(sol.maximumSum(nums))