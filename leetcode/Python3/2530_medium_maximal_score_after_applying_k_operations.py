"""
You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.
In one operation:
choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.
The ceiling function ceil(val) is the least integer greater than or equal to val.

Example 1:
Input: nums = [10,10,10,10,10], k = 5
Output: 50
Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.

Example 2:
Input: nums = [1,10,3,3,3], k = 3
Output: 17
Explanation: You can do the following operations:
Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
The final score is 10 + 4 + 3 = 17.
"""
from typing import List
import math
import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Init variables for score, j, and max_heap
        score, j = 0,0
        max_heap = []

        #Build max heap from nums list.
        for num in nums:
            heapq.heappush(max_heap, -num)

        #iterate through k operations
        while j < k:
            #Pop the maximum number in heap to select nums[i]
            curr_num = -(heapq.heappop(max_heap))
            #Increase score by nums[i]
            score+=curr_num
            #perform Ceil function on nums[i]
            alt_num = math.ceil(curr_num / 3)
            #add new num to max_heap
            heapq.heappush(max_heap, -alt_num)
            j+=1
        return score

nums = [1,10,3,3,3]
k = 3

sol = Solution()
print(sol.maxKelements(nums, k))