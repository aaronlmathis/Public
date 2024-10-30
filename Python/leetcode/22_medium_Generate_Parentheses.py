"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(current, open, close):
            if len(current) == 2 * n:
                ans.append(current)

            # Option 1 - add a ( if we haven't reached limit
            if open < n:
                backtrack(current + "(", open + 1, close)
            
            # Option 2
            if close < open:
                backtrack(current + ")", open, close + 1)    

        backtrack("", 0, 0)
        return ans
sol = Solution()
n = 3        
print(sol.generateParenthesis(n))