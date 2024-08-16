class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Pointer for the next unique element
        unique_index = 0

        # Loop through the array
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i] 
        return unique_index + 1
    
    
nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.removeDuplicates(nums))