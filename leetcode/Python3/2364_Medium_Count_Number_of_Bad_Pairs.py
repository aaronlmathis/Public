"""
You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.

Example 1:
Input: nums = [4,1,3,3]
Output: 5
Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
There are a total of 5 bad pairs, so we return 5.

Example 2:
Input: nums = [1,2,3,4,5]
Output: 0
Explanation: There are no bad pairs.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
"""
from collections import defaultdict
from typing import List
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Let n be the length of nums
        n = len(nums)
        # Initialize `pair_totals` to track number of times the same total of `nums[i] - i` occurs.
        # Initialize `total_possible`` to be the total number of pairs that can be made from 'n' numbers
        # Set `total_good` to 0.
        pair_totals = defaultdict(int)
        total_possible = n * (n-1) // 2
        total_good = 0

        # Iterate through nums taking a count of totals when calculating `nums[i] - i`.
        for i in range(len(nums)):
            pair_totals[nums[i]-i]+=1
        
        # Iterate through `pair_totals`. 
        # If v is greater than 1, calculate how many pairs can be made from v and add it to `total_good`
        for _, v in pair_totals.items():
            if v > 1:
                total_good+= v * (v-1) //2
        # Return `total_possible` - `total_good` to get total bad.
        return total_possible - total_good

# Notice that (j - i != nums[j] - nums[i]) is the same as (nums[i] - i != nums[j] - j).
nums = [4,1,3,3]
sol = Solution()
print(sol.countBadPairs(nums))
# if i < j and j - i != nums[j] - nums[i].
nums = [1,2,3,4,5]
print(sol.countBadPairs(nums))