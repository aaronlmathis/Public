from collections import Counter
class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return Counter(target) == Counter(arr)   


target = [3,7,9]
arr = [3,7,11]
sol = Solution()
print(sol.canBeEqual(target, arr))

"""        
You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. 
You are allowed to make any number of steps.
Return true if you can make arr equal to target or false otherwise.

"""