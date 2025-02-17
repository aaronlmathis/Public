"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l, r = 0,0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            l = flowerbed[i-1] if i > 0 else 0
            r = flowerbed[i+1] if i < len(flowerbed)-1 else 0
            print(f"{l} {r}")
            if l == 0 and r == 0:
                flowerbed[i] = 1
                n-=1
            if n == 0:
                return True

        return False

flowerbed = [0,0,1,0,0]
n = 1      
sol = Solution()
print(sol.canPlaceFlowers(flowerbed,n))