"""
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction 
that has a denominator 1. So in this case, 2 should be converted to 2/1.

"""
import re
import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        res = ""
        fractions = re.findall(r'[+-]?\d+/\d+', expression)
        
        numerator = 0
        denominator = 1

        for fraction in fractions:
            num, denom = map(int, fraction.split('/'))
            # Find the least common denominator
            lcm = denominator * denom // math.gcd(denominator, denom)
            
            # Adjust the numerators accordingly
            numerator = numerator * (lcm // denominator) + num * (lcm // denom)
            denominator = lcm
        
        # Simplify the fraction
        gcd = math.gcd(abs(numerator), denominator)
        numerator //= gcd
        denominator //= gcd
        
        # Format the result
        return f"{numerator}/{denominator}"            

sol = Solution()
expression = "-1/2+1/2"
print(sol.fractionAddition(expression))      # "0/1"  
expression = "-1/2+1/2+1/3"
print(sol.fractionAddition(expression))      # "1/3" 
expression = "1/3-1/2"
print(sol.fractionAddition(expression))      # "-1/6"