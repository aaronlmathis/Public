"""
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. 
You may return the answer in any order.
The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

Example 1:
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        for i, char in enumerate(expression):
            if char in "+-*":
                # Split the expression into two parts
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                
                # Combine results from both sides using the current operator
                for l in left:
                    for r in right:
                        if char == '+':
                            results.append(l + r)
                        elif char == '-':
                            results.append(l - r)
                        elif char == '*':
                            results.append(l * r)
        
        return results
    
sol = Solution()
expression = "2*3-4*5"
print(sol.diffWaysToCompute(expression))