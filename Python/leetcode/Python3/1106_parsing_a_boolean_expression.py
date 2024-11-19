"""
A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

't' that evaluates to true.
'f' that evaluates to false.
'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
'&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
'|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.

Example 1:

Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.
Example 2:

Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.
Example 3:

Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.
"""

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        def parse_or(expression) -> bool:

            # Convert 't' and 'f' to True and False
            expression = [True if e == 't' or e == True else False for e in expression]
            print(f"Sub: {expression}")
            # Return True if any value in the expression is True
            print(any(expression))
            return any(expression)
  
        def parse_and(expression) -> bool:
            # Convert 't' and 'f' to True and False
            expression = [True if e == 't' or e == True else False for e in expression]

            # Return True if any value in the expression is True
            return all(expression)
  
        def parse_not(expression) ->bool:
            # Convert 't' and 'f' to True and False
            value = True if expression[0] == 't' or expression[0] == True else False

            # Return the negated value
            return not value
        
        stack = []
        for e in expression:
            if e == ")":
                sub_expression = []
                while stack[-1] != '(':
                    sub_expression.append(stack.pop()) # Get every character within those parenthesis until the open parenthesis
                stack.pop()  # Get the open parenthesis

                operator = stack.pop() #Get the operator
                print(f"Op: {operator} Exp:{sub_expression}")

                # Evaluate the expression within the parentheses
                if operator == '!':
                    stack.append(parse_not(sub_expression))
                elif operator == '&':
                    #stack.append('t' if all(x == 't' for x in sub_expression) else 'f')
                    stack.append(parse_and(sub_expression))
                elif operator == '|':
                    #stack.append('t' if any(x == 't' for x in sub_expression) else 'f')
                    stack.append(parse_or(sub_expression))
            
            elif e != ',':
                stack.append(e)

        return stack[0]

expression = "!(&(!(&(f)),&(t),|(f,f,t)))"
sol = Solution()
print(sol.parseBoolExpr(expression))        