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

        # Backtrack function that has 2 options, add an open or add a closed parenthesis
        def backtrack(current, open, close):
            # Base Case: current is the length of 2 * n (there are no more characters left)
            if len(current) == 2 * n:
                # Add the current string to the answer list.
                ans.append(current)

            # Option 1 - add a ( if we haven't reached limit of available '(' characters
            if open < n:
                backtrack(current + "(", open + 1, close)
            
            # Option 2 - add a ')' if it makes a valid () (there are more open parenthesis than closed in current string)
            if close < open:
                backtrack(current + ")", open, close + 1)    
        
        # Call the initial backtrack() starting with an empty string current, 0 open, and 0 closed parenthesis
        backtrack("", 0, 0)
        
        # Return the answer
        return ans
    
sol = Solution()
n = 3        
print(sol.generateParenthesis(n))