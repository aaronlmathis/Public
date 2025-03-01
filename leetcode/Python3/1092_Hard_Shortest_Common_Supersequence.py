"""
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

Example 1:
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Example 2:
Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
 
Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
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
class Solution:
    @timed
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        M = len(str1)
        N = len(str2)

        # Initialize the DP table with zeros
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        LCS = set()

        # Fill the DP table
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if str1[i - 1] == str2[j - 1]:  # Match found
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:  # No match, take max from left or top
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j = M, N
        scs = []
        while i >0 and j > 0:
            if str1[i-1] == str2[j-1]:
                scs.append(str1[i-1])
                i-=1
                j-=1
            elif dp[i-1][j] > dp [i][j-1]:
                scs.append(str1[i-1])
                i-=1
            else:
                scs.append(str2[j-1])
                j-=1

        while i > 0:
            scs.append(str1[i-1])
            i-=1
        while j > 0:
            scs.append(str2[j-1])
            j-=1


        return ''.join(reversed(scs))

sol = Solution()
str1 = "bbbaaaba"
str2 = "bbababbb"
print(sol.shortestCommonSupersequence(str1, str2))
str1 = "abac"
str2 = "cab"
print(sol.shortestCommonSupersequence(str1, str2))