"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        n = len(nums)
        start, end = 0, 1
        while start < n:
            # Extend `end` while consecutive numbers are found
            while end < n and nums[end] == nums[end - 1] + 1:
                end += 1
            
            # Append the current range
            range = f"{nums[start]}->{nums[end-1]}" if start != end-1 else f"{nums[start]}"
            answer.append(range)
            
            # Move `start` to `end` for the next range
            start = end
            end = start + 1

        return answer

sol = Solution()
nums = [0,1,2,4,5,7]
print(sol.summaryRanges(nums))