from collections import Counter
class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        new = [key for key, value in Counter(arr).items() if value == 1]
        return new[k-1] if len(new) >= k else ""

    
arr = ["d","b","c","b","c","a"]
k = 2      
sol = Solution()
print(sol.kthDistinct(arr, k))
"""
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. 
If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
"""