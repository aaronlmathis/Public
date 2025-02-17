"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"{fname} took {after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper
from collections import Counter
class Solution:
    @timed
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math

        def gcd_of_strings(str1, str2):
            if str1 + str2 != str2 + str1:  # If concatenation order changes the result, there's no common divisor
                return ""

            gcd_len = math.gcd(len(str1), len(str2))  # Compute the greatest common divisor of lengths
            return str1[:gcd_len]  # The prefix of this length is the common divisor

str1 = "ABCABC"
str2 = "ABC"
#str1 = "ABABAB"
#str2 = "ABAB"
#str1 = "LEET"
#str2 = "CODE"
#str1 ="ABCDEF"
#str2 ="ABC"
#str1 ="AAAAAAAAA"
#str2 = "AAACCC"
sol = Solution()
print(sol.gcdOfStrings(str1, str2))        