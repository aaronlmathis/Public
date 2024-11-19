"""
Given two positive integers n and k, the binary string Sn is formed as follows:
S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).
For example, the first four strings in the above sequence are:
S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

Example 1:
Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".
Example 2:

Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".
 
"""

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def find(n, k):
            # Base case: If it's the first string, S1 is just "0"
            if n == 1:
                return '0'
            
            length = (1 << n) - 1  # Length of Sn is 2^n - 1
            mid = (length // 2) + 1  # Middle bit position
            
            if k == mid:
                return '1'
            elif k < mid:
                return find(n - 1, k)
            else:
                # Corresponding position in the first half
                return '1' if find(n - 1, length - k + 1) == '0' else '0'
    
        return find(n, k)
    
sol = Solution()
n = 13
k = 15
print(sol.findKthBit(n, k))        