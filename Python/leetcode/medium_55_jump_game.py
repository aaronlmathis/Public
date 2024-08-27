class Solution:
    def canJump(self, nums: list[int]) -> bool:
        m = 0
        for i in range(1, nums[0]+1):
            if nums[i] > nums[i+1]:
                m = nums[i]

        

sol =Solution()
nums = [2,3,1,1,4] #True
print(sol.canJump(nums))
nums = [3,2,1,0,4] #False
print(sol.canJump(nums))