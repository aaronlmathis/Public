"""
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

Example 1:
Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

Example 2:
Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0. 

Example 3:
Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.
"""
from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)               # Initialize n as length of code
        if k == 0:                  # If k = 0, return zeros
            return [0] * n
        
        result = [0] * n            # Initialize the result list
        extendedCode = code * 2     # Concatinate the code to handle circular nature.

        if k > 0:                   # Look ahead
            start, end = 1, k   
        else:                       # Look Behind
            start, end = n + k, n - 1

        windowSum = sum(extendedCode[start:end+1])  #Initial Sum of window

        for i in range(n):          # Iterate through each number, sliding window and recalculating code
            result[i] = windowSum
            windowSum -= extendedCode[start]
            windowSum += extendedCode[end + 1]
            start += 1
            end  += 1
        
        return result
        """
        decryptedCode = []      # Initialize list to hold the decrypted code
        n = len(code)           # Initialize n as length of code
        for digit in range(n):
            newNum = 0
            if k > 0:
                iteration = 0
                spot = digit
                while iteration < k:
                    if spot == n-1:
                        spot = 0
                    else:
                        spot +=1
                    newNum+=code[spot]
                    iteration+=1
                decryptedCode.append(newNum)
            elif k < 0:
                iteration = 0
                spot = digit
                while iteration > k:
                    if spot == 0:
                        spot = n-1
                    else:
                        spot-=1
                    newNum+=code[spot]
                    iteration-=1
                decryptedCode.append(newNum)                
            else:
                decryptedCode.append(0)

        return decryptedCode
        """

sol = Solution()
code = [5,7,1,4]
k = -3        
print(sol.decrypt(code, k))