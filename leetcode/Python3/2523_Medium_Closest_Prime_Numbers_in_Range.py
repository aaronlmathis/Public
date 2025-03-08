"""
Given two positive integers left and right, find the two integers num1 and num2 such that:

    -Both num1 and num2 are prime numbers.
    -left <= num1 < num2 <= right .
    -num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.

Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

Example 1:
Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

Example 2:
Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

Constraints:

1 <= left <= right <= 106
 
"""
from typing import List
class Solution:
    
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True] * (right+1)
        primes[0], primes[1] = False, False
        for i in range(2, int(right**0.5)+1):
            if primes[i]:
                for j in range(i*i, right+1, i):
                    primes[j] = False
        print(primes)
        candidates = [index for index, val in enumerate(primes) if val == True and index >= left]
        min_diff = float('inf')
        answer = [-1, -1]
        for i in range(1, len(candidates)):
            diff = candidates[i] - candidates[i-1]
            if diff < min_diff:
                min_diff = diff
                answer = [candidates[i-1], candidates[i]]
        return answer
        

            

sol = Solution()
left, right = 10, 19
print(sol.closestPrimes(left, right))            