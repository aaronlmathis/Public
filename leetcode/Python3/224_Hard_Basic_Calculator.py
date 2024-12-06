"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Example 4:
Input: s = "2-1*2"
Output: 0
 
"""
from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        def solve(index: int) -> (int, int):
            stack = []
            num = 0
            sign = '+'  # Default to addition
            
            while index < len(s):
                char = s[index]
                
                if char.isdigit():
                    num = num * 10 + int(char)  # Form multi-digit numbers
                elif char in "+-*/":
                    # Process the previous operator with the current number
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        # Perform integer division (truncate towards zero)
                        stack.append(int(stack.pop() / num))
                    
                    # Update the sign and reset the number
                    sign = char
                    num = 0
                elif char == '(':
                    # Solve the expression inside parentheses
                    num, index = solve(index + 1)
                elif char == ')':
                    # Process the last number before exiting the parenthesis
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        stack.append(int(stack.pop() / num))
                    return sum(stack), index  # Return the sum of the stack and the closing index
                
                index += 1
            
            # Process the last number in the expression
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))
            
            return sum(stack), index  # Return the total sum and the final index

        # Start solving from index 0
        result, _ = solve(0)
        return result


sol = Solution()
s = "1 + 1"
print(sol.calculate(s))