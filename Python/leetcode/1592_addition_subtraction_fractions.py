import re
import math

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        fractions = re.findall('[+-]?\d+/\d+', expression)
        numerator, denominator = 0, 1
        
        for frac in fractions:
            num, denom = map(int, frac.split('/'))
            # Find least common denominator (LCD)
            denominator = denominator * denom // math.gcd(denominator, denom)

        # Sum all fractions after converting to a common denominator
        for frac in fractions:
            num, denom = map(int, frac.split('/'))
            numerator += num * (denominator // denom)
        
        # Reduce the resulting fraction
        gcd = math.gcd(abs(numerator), denominator)
        numerator //= gcd
        denominator //= gcd
        
        # Return the result as a string
        return f"{numerator}/{denominator}"

sol = Solution()
expression = "-1/2+1/2+1/3"
print(sol.fractionAddition(expression))
