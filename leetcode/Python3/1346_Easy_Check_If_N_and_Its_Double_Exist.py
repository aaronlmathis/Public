"""
Given an array arr of integers, check if there exist two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
"""
from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        # Create a hashmap to store each number 
        # This helps us efficiently check for the existence of numbers.
        seen = {}

        # Iterate through the nums array.
        # Check if arr[i] * 2 or arr[i] / 2 exist in hashmap, if so return true
        # If not, add arr[i] to the hashmap and continue
        for i in range(n):
            if arr[i] * 2 in seen or arr[i] / 2 in seen:
                return True
            else:
                seen[arr[i]] = seen.get(arr[i], 0) + 1
        
        # Return false if no pair exists
        return False

        """
        # Populate the hashmap with all the numbers in arr
        for idx, num in enumerate(arr):
            seen[num] = idx
        
        # Iterate through the array to check if the double of the current number exists
        for idx, num in enumerate(arr):
            double = num * 2    # Calculate the double of the current number

            # Check if the double exists in the hashmap
            # Additionally, ensure the indices are not the same because i != j
            if double in seen and seen[double] != idx:
                return True
        """


sol = Solution()
arr = [10,2,5,3]
print(sol.checkIfExist(arr))        