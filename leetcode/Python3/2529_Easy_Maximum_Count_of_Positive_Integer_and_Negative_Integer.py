"""
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

Example 1:
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

Example 2:
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

Example 3:
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
 
Constraints:
1 <= nums.length <= 2000
-2000 <= nums[i] <= 2000
nums is sorted in a non-decreasing order.
 
"""
from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 and nums[0] == 0:
            return 0
        low, high, maxNeg = 0, n-1, -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < 0:
                maxNeg = mid
                low = mid + 1
            else:
                high = mid - 1
        if (n % 2 == 0 and maxNeg + 1 >= n//2) or (n%2!=0 and maxNeg >= n // 2):
            return maxNeg+1

        minPos = -1
        low, high = maxNeg+1, n-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > 0:
                high = mid - 1
                minPos = mid
            else:
                low = mid + 1
        if minPos == -1 and maxNeg == -1:
            return 0
        return max(maxNeg+1, n-minPos)
        
        

sol = Solution()
nums = [0,0,0,0]
print(sol.maximumCount(nums))