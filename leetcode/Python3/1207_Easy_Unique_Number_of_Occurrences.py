"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_count = {}
        for num in arr:
            if num in num_count:
                num_count[num]+=1
            else:
                num_count[num]=1
        unique = set()
        for _,v in num_count.items():
            if v in unique:
                return False
            unique.add(v)
        return True
arr = [1,2,2,1,1,3]
sol = Solution()
print(sol.uniqueOccurrences(arr))        