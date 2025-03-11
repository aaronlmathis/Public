"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 
Constraints:
0 <= n <= 105
Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for t in range(1, n+1):
            i = t
            oc = 0
            if i >= 65536:
                i%=65536
                oc+=1
            if i >= 32768:
                i%=32768
                oc+=1            
            if i >= 16384:
                i%=16384
                oc+=1
            if i >= 8192:
                i%=8192
                oc+=1
            if i >= 4096:
                i%=4096
                oc+=1
            if i >= 2048:
                i%=2048
                oc+=1
            if i >= 1024:
                i%=1024
                oc+=1
            if i >= 512:
                i%=512
                oc+=1

            if i >= 256:
                i%=256
                oc+=1

            if i >= 128:
                i%=128
                oc+=1

            if i >= 64:
                i %= 64
                oc += 1
            if i >= 32:
                i %= 32
                oc += 1
            if i >= 16:
                i %= 16
                oc += 1
            if i >= 8:
                i %= 8
                oc+=1
            if i >= 4:
                i %= 4
                oc += 1
            if i >= 2:
                i %= 2
                oc+=1
            if i == 1:
                oc+=1
            ans[t] = oc
        
        return ans
n =85723


sol = Solution()  
print(sol.countBits(n))
n=5        