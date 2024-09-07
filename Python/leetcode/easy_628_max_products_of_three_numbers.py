from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        res = 1
        mins = []
        maxs = []
        nums.sort()
        for i in range(len(nums) -1, len(nums)-4, -1):
            maxs.append(nums[i])
        for i in range(0, 3, 1):
            mins.append(nums[i])

        return max(mins[0] * mins[1] * maxs[0], maxs[0] * maxs[1] * maxs[2])
        
sol = Solution()
nums = [-100,-98,-1,2,3,4] # 39200
print(sol.maximumProduct(nums))