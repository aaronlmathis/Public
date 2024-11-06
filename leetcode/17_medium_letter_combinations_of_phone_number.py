class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
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
        if len(digits) == 1:
            return phone_keypad[digits]
        if not digits:
            return None
        
        result = ['']
        for digit in digits:
            new_combo = []
            for combination in result:
                for letter in phone_keypad[digit]:
                    new_combo.append(combination + letter)
            result = new_combo
        return result
    
number = '23'
sol = Solution()
print(sol.letterCombinations(number))
