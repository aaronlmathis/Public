"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
"""
import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Initialize DP as list of size n.
        dp = [0] * n
        # Set dp[0] to 1
        dp[0] = 1
        # Start three pointers at 0
        i2, i3, i5 = 0, 0, 0
        # Iterate from 1 to n
        for i in range(1, n):
            # Find the next three numbers
            n2 = dp[i2] * 2
            n3 = dp[i3] * 3
            n5 = dp[i5] * 5
            # Set dp[i] to the smallest of those three numbers
            dp[i] = min(n2, min(n3, n5))

            #Increase the pointer of the number that was the smallest
            if dp[i] == n2:
                i2+=1
            if dp[i] == n3:
                i3+=1
            if dp[i] == n5:
                i5+=1
        # Return the nth ugly number
        return dp[n-1]
        

sol = Solution()
n = 19
print(sol.nthUglyNumber(n))
