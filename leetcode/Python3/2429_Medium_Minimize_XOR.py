"""
Given two positive integers num1 and num2, find the positive integer x such that:

    - x has the same number of set bits as num2, and
    - The value x XOR num1 is minimal.

Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.

Example 1:
Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.

Example 2:
Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.
 
"""
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1,b2 = bin(num1)[2:], bin(num2)[2:]
        b1, b2 = b1.zfill(max(len(b1), len(b2))), b2.zfill(max(len(b1), len(b2)))
        b1_count, b2_count = b1.count('1'), b2.count('1')

        if b2_count == b1_count:
            return num1
        
        elif b2_count > b1_count:
            ans = list(b1)
            swaps = b2_count - b1_count
            for i in range(len(ans)-1, -1, -1):
                if ans[i] == '0':
                    ans[i] = '1'
                    swaps-=1
                if swaps == 0:
                    break
        else:
            ans = list(b1)
            swaps = b1_count - b2_count
            for i in range(len(ans)-1, -1, -1):
                if ans[i] == '1':
                    ans[i] = '0'
                    swaps-=1
                if swaps == 0:
                    break            
        
        return int(''.join(ans), 2)
num1 = 1 
num2 = 12        
sol = Solution()
print(sol.minimizeXor(num1, num2))