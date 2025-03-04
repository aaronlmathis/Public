"""
Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

Example 1:
Input: n = 12
Output: true
Explanation: 12 = 3**1 + 3**2

Example 2:
Input: n = 91
Output: true
Explanation: 91 = 3**0 + 3**2 + 3**4

Example 3:
Input: n = 21
Output: false
 
Constraints:

1 <= n <= 107
"""
from collections import deque
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n != 0:
            r = n % 3
            if r == 2:
                return False
            n //= 3
        return True
    
sol = Solution()
vals = [(12, True), (91, True), (21, False), (7627, True)]
for val, ans in vals:
    print(f"{sol.checkPowersOfThree(val)}\tExpected: {ans}")