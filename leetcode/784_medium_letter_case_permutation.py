"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.

Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]
"""
from typing import Lists
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [""]
        subset = []

        for c in s:
            tmp = []
            if c.isalpha():
                for o in output:
                    tmp.append(o+c.lower())
                    tmp.append(o+c.upper())
            else:
                for o in output:
                    tmp.append(o+c)

            output = tmp
        return output

s = "a1b2"
sol = Solution()
print(sol.letterCasePermutation(s))