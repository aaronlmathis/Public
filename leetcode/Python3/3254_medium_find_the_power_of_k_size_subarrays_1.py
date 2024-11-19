"""
You are given an array of integers nums of length n and a positive integer k.
The power of an array is defined as:
Its maximum element if all of its elements are consecutive and sorted in ascending order. -1 otherwise.
You need to find the power of all subarrays of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

Example 1:
Input: nums = [1,2,3,4,3,2,5], k = 3
Output: [3,4,-1,-1,-1]
Explanation:
There are 5 subarrays of nums of size 3:
[1, 2, 3] with the maximum element 3.
[2, 3, 4] with the maximum element 4.
[3, 4, 3] whose elements are not consecutive.
[4, 3, 2] whose elements are not sorted.
[3, 2, 5] whose elements are not consecutive.
Example 2:
Input: nums = [2,2,2,2,2], k = 4
Output: [-1,-1]

Example 3:
Input: nums = [3,2,3,2,3,2], k = 2
Output: [-1,3,-1,3,-1]

from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        subarrays = [nums[i:i+k] for i in range(len(nums) - (k-1))] #Get all subarrays of length k
        ans = [-1] * len(subarrays)
        curr = 0
        for s in range(len(subarrays)):
            if sorted(subarrays[s]) == subarrays[s]:
                consecutive = True
                for i in range(len(subarrays[s])-1):
                    if abs(subarrays[s][i] - subarrays[s][i+1]) != 1:
                        consecutive = False
                if consecutive == True:
                    ans[s] = max(subarrays[s])
                curr+=1
        return ans
"""        
from typing import List
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * (len(nums) - k + 1)
        for i in range(len(nums) - k +1):
            subarray = nums[i:i+k]
            con = True
            for j in range(k-1):
                #if subarray[j] >= subarray[j+1] and abs(subarray[j] - subarray[j+1] == 1):
                if subarray[j+1] - subarray[j] != 1:
                    con = False
                    break
            ans[i] = max(subarray) if con else -1
        return ans

                



sol = Solution()
nums = [1,2,3,4,3,2,5]
k = 3
print(sol.resultsArray(nums, k))