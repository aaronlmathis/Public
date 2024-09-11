class Solution:

    def singleNumber_alt(nums):
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                unique_nums.remove(num)
            else:
                unique_nums.add(num)
        return unique_nums.pop()

    def singleNumber(self, nums: list[int]) -> int:
        unique = 0
        for num in nums:
            unique ^= num
        return unique
    
sol = Solution()
nums = [2, 2, 1]
print(sol.singleNumber(nums))
