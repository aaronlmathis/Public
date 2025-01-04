"""
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
 
"""
from collections import defaultdict

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        map = defaultdict(list)
        n = len(s)
        prefix = [0] * (n+1)
        char_set = set()
        for i in range(1, n+1):
            map[s[i-1]].append(i-1)
            prefix[i] = prefix[i-1] | (1 << (ord(s[i-1]) - ord('a')))
        print(prefix)

        ans = 0

        for char, indexes in map.items():
            if len(indexes) < 2:
                continue
            # print(indexes)
            # uchars = set()
            # for i in range(indexes[0]+1, indexes[-1]):
            #     uchars.add(s[i])
            # ans+=len(uchars)
            ans+= bin(prefix[indexes[-1] ] ^ prefix[indexes[0]]).count('1')
            print(f"Unique chars in between {indexes[0]} - {indexes[-1]}: { bin(prefix[indexes[-1] - 1] ^ prefix[indexes[0]]).count('1')} ")
        print(map)

        return ans
s = "bbcbaba"
#s = "aabca"
#s ="ckafnafqo" 
sol = Solution()
print(sol.countPalindromicSubsequence(s))