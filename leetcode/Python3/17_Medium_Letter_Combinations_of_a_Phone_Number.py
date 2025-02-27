"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Return empty list if digits is null.
        if not digits:
            return []
        
        # Dictionary to store letter optons for each number key.
        phone_keypad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        # Create stack from digits (reversed) so we can pop the next number off stack.
        digits = list(digits[::-1])

        # create empty list to store answers.
        combinations = []

        # Backtrack function that explores every combo of letter by adding it to `combo`
        # calling the backtrack function recursively, and removing it from `combo` to try next letter.
        def backtrack(combo, digits):
            # Digits has been exhausted, add string generated from `combo` to `combinations`
            if not digits:
                combinations.append(''.join(combo[:]))
                return
            # Get current digit
            digit = digits.pop()

            # Iterate through every letter option for digit
            for letter in phone_keypad[digit]:
                combo.append(letter)    # Add to combo and explore further
                backtrack(combo, digits)
                combo.pop() # Remove letter and try a different one.
            # Backtrack
            digits.append(digit)
        
        # Call initial backtrack method
        backtrack([], digits)
        return combinations

digits = "2"
sol = Solution()
print(sol.letterCombinations(digits))