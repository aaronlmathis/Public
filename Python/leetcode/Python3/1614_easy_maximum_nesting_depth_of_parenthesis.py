class Solution:
    def maxDepth(self, s: str) -> int:
        state = 0 # 0 for open, 1 for close
        count = 0 # levels of nesting
        max_count = 0

        for c in s:
            if c == '(':
                count+=1
            elif c == ')':
                count-=1
            if count > max_count:
                max_count = count

        return max_count

sol = Solution()
s = "(1+(2*3)+((8)/4))+1" #3
print(sol.maxDepth(s))
s = "(1)+((2))+(((3)))" #3
print(sol.maxDepth(s))
s = "()(())((()()))" #3
print(sol.maxDepth(s))

"""
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.


Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation:

Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

Input: s = "(1)+((2))+(((3)))"

Output: 3

Explanation:

Digit 3 is inside of 3 nested parentheses in the string.

Example 3:

Input: s = "()(())((()()))"

Output: 3
"""