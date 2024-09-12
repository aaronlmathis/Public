"""
Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

 

Example 1:

Input: n = 3
Output: 3

Example 2:

Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        # Step 1: Determine the range the nth digit is in
        digit_length = 1  # starting with 1-digit numbers
        count = 9  # 9 numbers with 1 digit
        start = 1  # numbers start from 1

        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10

        # Step 2: Determine the actual number
        start += (n - 1) // digit_length  # the number that contains the nth digit

        # Step 3: Find the exact digit in the number
        s = str(start)
        return int(s[(n - 1) % digit_length])
n = 1145639811
sol = Solution()
print(sol.findNthDigit(n))