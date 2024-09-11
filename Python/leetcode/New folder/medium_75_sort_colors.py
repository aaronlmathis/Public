class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zeros, ones, twos = nums.count(0), nums.count(1), nums.count(2)
        i = 0
        while i < len(nums):
            if zeros >0:
                nums[i] = 0
                zeros-=1
            elif ones > 0:
                nums[i] = 1
                ones-=1
            elif twos > 0:
                nums[i] = 2
                twos-=1
            i+=1

sol = Solution()
nums = [0, 2, 1, 1, 0]
print(sol.sortColors(nums))