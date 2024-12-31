"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        i = 0
        j = 0
        startIndex = -1
        match = 0

        while i < n:

            # Characters match or '?' in pattern matches
            # any character.
            if j < m and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1

            elif j < m and p[j] == '*':

                # Wildcard character '*', mark the current
                # position in the pattern and the text as a
                # proper match.
                startIndex = j
                match = i
                j += 1

            elif startIndex != -1:

                # No match, but a previous wildcard was found.
                # Backtrack to the last '*' character position
                # and try for a different match.
                j = startIndex + 1
                match += 1
                i = match

            else:

                # If none of the above cases comply, the
                # pattern does not match.
                return False

        # Consume any remaining '*' characters in the given
        # pattern.
        while j < m and p[j] == '*':
            j += 1

        # If we have reached the end of both the pattern and
        # the text, the pattern matches the text.
        return j == m        
s = "aa"
p = "a"
sol = Solution()
print(sol.isMatch(s, p))       