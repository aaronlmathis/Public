class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates

            left = i+1
            right = len(nums) - 1
            sum = nums[i] + nums[left] + nums[right]
            if sum == 0:
                res.append([nums[i], nums[left], nums[right]])
                # Move left and right pointers, and skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1                
                
                left += 1
                right -= 1
                
            elif sum < 0:
                left+=1
            else:
                right-=1
        
        return res



sol = Solution()
nums = [-1,0,1,2,-1,-4]       
print(sol.threeSum(nums))