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
        # Set `s1, s2` equal to the lengths of `str1`` and `str2`
        s1, s2 = len(str1), len(str2)
        # Set `l_str`, `s_str` equal to the longer of `str1/str2` and the shorter of `str1/str2`
        l_str, s_str = (str1, str2) if s1 > s2 else (str2, str1)

        # set `gcd` to equal the greatest common divisor of s1, s2
        import math
        gcd = math.gcd(s1, s2)

        # While the `gcd` is greater than one: take a slice of `s_str` from index 0 to index `gcd`. 
        #   - If `slice` multiplied by the length of `l_str` divided by `gcd` is equal to `l_str` 
        #       and `slice` multipled by the length of `s_str` divided by `gcd` equals `s_str`, 
        #       return `slice` as the answer. 
        #   - Decrement gcd to continue the loop trying a shorter divisor.
        while gcd > 0:
            slice = s_str[0:gcd]
            if slice * (len(l_str) // gcd) == l_str and  \
                slice * (len(s_str) // gcd) == s_str:
                return slice
            gcd-=1
        
        # Valid Divisor wasn't found, return ""
        return ""

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