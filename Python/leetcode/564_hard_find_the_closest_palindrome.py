class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)
        
        # Edge case for single digit number or powers of 10 like 1000, 10000
        if num <= 10:
            return str(num - 1)
        if n == '1' + '0' * (length - 1):
            return str(num - 1)
        if n == '9' * length:
            return str(num + 2)

        # Create palindromes by manipulating the middle part
        prefix = int(n[:(length + 1) // 2])
        candidates = [
            self.create_palindrome(str(prefix - 1), length % 2 == 0),
            self.create_palindrome(str(prefix), length % 2 == 0),
            self.create_palindrome(str(prefix + 1), length % 2 == 0),
            "9" * (length - 1),  # One less digit (all 9s)
            "1" + "0" * (length - 1) + "1"  # One more digit (100...001)
        ]
        
        # Print candidates before removing the original number
        print("Candidates before filtering:", candidates)

        # Convert to integers and remove the original number itself
        candidates = [int(c) for c in candidates if c != n]
        
        # Print candidates after filtering
        print("Candidates after filtering:", candidates)
        
        # Find the closest palindrome
        closest = min(candidates, key=lambda x: (abs(x - num), x))
        
        return str(closest)
    
    def create_palindrome(self, s, even_length):
        if even_length:
            return s + s[::-1]
        else:
            return s + s[-2::-1]


# Test case
n = "124"
sol = Solution()
print(sol.nearestPalindromic(n))  # Expected output: "9"




"""
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. 

If there is a tie, return the smaller one. The closest is defined as the absolute difference minimized between two integers.

Example 1:

Input: n = "123"
Output: "121"

Test Cases:

"101"
"999999999999999999"
"11"
"1000000000000000"
"1837722381"
"1805170081"
"11011"
"807045053224792883"

"""