"""
Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:

    -1 <= i <= n
    -The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.

Example 1:
Input: n = 10
Output: 182
Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182

Example 2:
Input: n = 37
Output: 1478
Explanation: There are exactly 4 integers i in the range [1, 37] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1. 
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
"""
class Solution:
    def punishmentNumber(self, n: int) -> int:
        answer = 0
        pun_nums = {}
        for i in range(1, n+1):
            squared = i * i
            val = squared
            sub = []
            while val > 0:
                sub.append(val % 10)
                val //= 10
            pun_nums[i] = (squared, sub[::-1], sum(sub))
        
        for k, (a, b, c) in pun_nums.items():
            print(f"{k} - \t{a}\t{b}\t\t{c}")
        return answer

sol = Solution()
n=100
print(sol.punishmentNumber(n))        