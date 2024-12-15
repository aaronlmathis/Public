"""
You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

You can perform the following operation at most maxOperations times:

- Take any bag of balls and divide it into two new bags with a positive number of balls.
For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.

Example 1:
Input: nums = [9], maxOperations = 2
Output: 3
Explanation: 
- Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
- Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.

Example 2:
Input: nums = [2,4,8,2], maxOperations = 4
Output: 2
Explanation:
- Divide the bag with 8 balls into two bags of sizes 4 and 4. [2,4,8,2] -> [2,4,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,4,4,4,2] -> [2,2,2,4,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,4,4,2] -> [2,2,2,2,2,4,2].
- Divide the bag with 4 balls into two bags of sizes 2 and 2. [2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2].
The bag with the most number of balls has 2 balls, so your penalty is 2, and you should return 2.
"""
from typing import List
from math import ceil
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """ 
        def minMax(low:int, high:int) -> int:
            - Returns the minimum max balls in each bag given a range of possible ball amounts, from 1 to the maximum number in nums
        """
        def minMax(low: int, high: int) -> int:
            """
            def canSplit(newMax: int) -> bool:
                - returns True or False whether you can split the bags of balls into having a maximum ball count of newMax in each bag in maxOperations or less.
            """
            def canSplit(newMax: int) -> bool:
                # Number of operations starts at 0
                operations = 0
                # Iterate through each bag of balls to calculate how many operations it would take to split the bag into newMax balls each
                for num in nums:
                    # This is the formula to determine how many operations it would take. (number of balls in bag - 1) integer divided by proposed max in each bag. For example, if a bag has 8 balls and you wanted to split it into bags of 2 balls each, (8-1) // 2 = 3. It would require 3 operations.
                    operations += (num - 1) // newMax
                # If operations is <= maxOperations, return True because you canSplit this bag.
                if operations <= maxOperations:
                        return True
                else:
                    return False
            # Start answer at low (1)      
            ans = low
            # do a binary search where low = 1 and high = max(nums). Keep going as long as low does not pass high.
            while low <= high:
                # Find the middle between low and high and check if canSplit
                mid = (low+high) // 2
                if canSplit(mid):
                    # You can split, so set ans to mid, and change high to mid - 1 to see if any lower numbers work
                    ans = mid
                    high = mid - 1
                else:
                    # You cant, so increase low to mid+1 to see if any higher numbers work
                    low = mid+1
            # Once loop is done, you should have the minimum number of balls per bag. Return it.
            return ans
        # Return minMax function
        return minMax(1, max(nums))

sol = Solution()
nums = [2,4,8,2]
maxOperations = 4       
print(sol.minimumSize(nums, maxOperations))