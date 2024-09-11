class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Initialize the new array with the same length as nums, filled with 1
        new_array = [1] * len(nums)

        # Calculate the product of all elements to the left of each index
        left_product = 1
        for i in range(len(nums)):
            new_array[i] = left_product
            left_product *= nums[i]

        # Calculate the product of all elements to the right of each index
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            new_array[i] *= right_product
            right_product *= nums[i]

        return new_array       

sol = Solution()        
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))
nums = [-1,1,0,-3,3]
print(sol.productExceptSelf(nums))