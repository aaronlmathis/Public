"""
Given an array of integers arr of even length n and an integer k.
We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
Return true If you can find a way to do that or false otherwise.

Example 1:
Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

Example 2:
Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).

Example 3:
Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
"""
from typing import List
from collections import Counter
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:


        # Create a frequency dictionary of remainders
        remainder_count = Counter([num % k for num in arr])
        
        # Check each remainder
        for r in range(k):
            if r == 0:
                # For remainder 0, the count must be even
                if remainder_count[r] % 2 != 0:
                    return False
            else:
                # For other remainders, the count of remainder `r` must be equal to the count of remainder `k - r`
                if remainder_count[r] != remainder_count[k - r]:
                    return False
        
        return True
arr = [1,2,3,4,5,10,6,7,8,9]
k = 5
sol = Solution()
print(sol.canArrange(arr, k))
