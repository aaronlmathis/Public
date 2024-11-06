"""
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
"""
from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        current_window = set()
        left = 0 #left pointer
        current_sum = 0 # Sum of elements from current window
        max_value = 0 # Track the max value

        # Iterate throught he list, opening the window to the right until there are duplicates. 
        # Then shrink window from left until next item on the right is unique again.
        
        for right in range(len(nums)):
            #If the number to the right is a duplicate, shrink the window from the left
            while nums[right] in current_window:
                current_window.remove(nums[left]) # Remove the left number from the set
                current_sum -= nums[left] # Reduce the current sum by nums[left]
                left+=1 # Move the left pointer to the right

            
            current_window.add(nums[right]) # Add the new numbers to the right to the set
            current_sum += nums[right] # Add the new number to the total

            max_value = max(max_value, current_sum) # Track the maximum sum

        return max_value

sol=Solution()
nums = [4,2,4,5,6]    
print(sol.maximumUniqueSubarray(nums))

