"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, 
also represented as a string. Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        num1, num2 = num1[::-1], num2[::-1]
        result = [0] * (len(num1) + len(num2))  # Initialize result list
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                product = int(num1[i]) * int(num2[j])
                result[i + j] += product  # Add product to the correct position
                
                # Handle carry for the next position
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10  # Keep only the last digit in the current position

        # Remove any leading zeros and convert result list to a string
        while len(result) > 1 and result[-1] == 0:
            result.pop()  # Remove leading zeros
        
        return ''.join(map(str, result[::-1])) 
       


sol = Solution()
num1 = "233"
num2 = "3"
print(sol.multiply(num1, num2))