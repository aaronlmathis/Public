"""
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

Example 1:
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Example 2:
Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
"""
from typing import List
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_value = float('-inf')

        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0)) # Push (number, list index, element index) into heap
            max_value = max(max_value, nums[i][0]) # Keep track of the maximum value.

        result = [float('-inf'), float('inf')]   # initialize the answer variable [x, x]

        while min_heap: # while there is still something in min_heap
            min_value, lst_idx, ele_idx = heapq.heappop(min_heap) #pop the top value off the min heap

            if max_value - min_value < result[1] - result[0]:
                result = [min_value, max_value]

            if ele_idx + 1 == len(nums[lst_idx]): # Break the loop if end of list
                break
            
            next_value = nums[lst_idx][ele_idx+1]
            heapq.heappush(min_heap, (next_value, lst_idx, ele_idx+1))
            max_value = max(max_value, next_value)

        return result

sol = Solution()
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
print(sol.smallestRange(nums))