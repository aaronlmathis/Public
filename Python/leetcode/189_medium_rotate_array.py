class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0,nums[len(nums) - 1])
            nums.pop()
sol = Solution()
nums = [1,2,3,4,5,6,7,8]
k = 3
print(sol.rotate(nums, k))