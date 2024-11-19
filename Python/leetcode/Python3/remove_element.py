class Solution:
    def removeElement(self, nums, val):
        for k, v in enumerate(nums):
            if v == val:
                nums.pop(k)
        length = len(nums)
        return length, nums

sol = Solution()
list= [0,1,2,2,3,0,4,2]
print(list)
length, list = sol.removeElement(list, 2)
print(length)
print(list)
