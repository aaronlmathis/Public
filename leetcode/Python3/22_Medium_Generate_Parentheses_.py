"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtrack(state, open, close):
            if len(state) == n*2:
                answer.append(''.join(state[:]))
                return
            
            if open < n:
                state.append('(')
                backtrack(state, open+1, close)
                state.pop()
            
            if close < open:
                state.append(')')
                backtrack(state, open, close+1)
                state.pop()
        
        backtrack([], 0, 0)
        return answer

n=3
sol = Solution()
print(sol.generateParenthesis(n))