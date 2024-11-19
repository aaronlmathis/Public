"""
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
"""
from typing import List
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Initialize n as length of nums
        n = len(nums)
        
        # Early exit if k > n
        if k > n: return 0
        
        # Initialize int variable to hold answer returned
        answer = 0

        # Set start pointer to represent start of each window
        start = 0
        # Initialize a set to track frequency of numbers
        seen = set()
        # Initialize subTotal to track sum of current subarray
        subTotal = 0

        # Iterate through the nums list, dynamically resizing window and calculating sum
        for end in range(n):
            # Handle duplicates by shrinking window from left until duplicate is gone.
            # While shrinking, reduce total by each number and remove number from seen hashset
            while nums[end] in seen:
                subTotal-=nums[start]
                seen.remove(nums[start])
                start+=1
            
            # If not a duplicate anymore, add it to seen hashset and increase subTotal
            seen.add(nums[end])
            subTotal+=nums[end]

            # If window size is larger than k, shrink it from left
            # Remove each number from subTotal and hashset while shrinking.
            if end - start + 1 > k:
                subTotal -= nums[start]
                seen.remove(nums[start])
                start+=1

            # If window is of size k, its a valid subarray.
            # Check if subTotal is > answer, if so, set answer to subTotal
            if end - start + 1 == k:
                if subTotal > answer:
                    answer = subTotal

        # Return the max subTotal sum of a subarray of length k with no duplicates
        return answer

sol = Solution()
nums = [1,1,2]
k = 2
print(sol.maximumSubarraySum(nums, k))        
"""
# Iterate while start can make a valid window of size k
while start <= n - k:
    # Int to store sum of the subarray  
    subTotal = 0

    # Clear the hash set tracking frequency each iteration
    seen.clear()

    # Iterate end of window until window is size k
    for end in range(start, start + k):
        # Check if the number has been seen already
        if nums[end] in seen:
            # shrink window until all numbers before the duplicate are excluded
            while nums[start] != nums[end]:
                # Remove number while shrinking window
                seen.remove(nums[start])
                start += 1
            # Increase one more to exclude the duplicate number
            start += 1
            # Break the loop, as a duplicate was found.
            break
        # No duplicate found, so add the current element and increase sum total
        seen.add(nums[end])
        total += nums[end]
    print(start)
    print(end)
    print(seen)
    
    # Make sure that the window forms a valid subarray of length k.
    if len(seen) == k:
        print(f"Window: {nums[start:start + k]}, Sum: {total}")                
        # Set answer to the subarray sum total if it is larger than any seen previously
        if answer < total:
            answer = total
    
    # continue finding subarrays
    start += 1
"""