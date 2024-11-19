class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for k, v in enumerate(nums):
            if v >= target:
                return k
        return len(nums)
    

        
sol = Solution()
nums = [1,3,5,6]
target = 7
print(sol.searchInsert(nums, target))
