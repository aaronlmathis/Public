"""
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

    - It is ().
    - It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
    - It can be written as (A), where A is a valid parentheses string.

You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

    - If locked[i] is '1', you cannot change s[i].
    - But if locked[i] is '0', you can change s[i] to either '(' or ')'.

Return true if you can make s a valid parentheses string. Otherwise, return false.

Example 1:
Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.

Example 2:
Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.

Example 3:
Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.
"""
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1: return False

        left_locked = []
        free = []

        for i in range(n):
            if i == 0:
                if locked[i] == '0':
                    free.append(i)
                else:
                    if s[i] == '(':
                        left_locked.append(i)
                    else:
                        return False
                continue
            if locked[i] == '1':
                if s[i] == ')':
                    if left_locked:
                        left_locked.pop()
                    elif free:
                        free.pop()
                    else:
                        return False
                else:
                    left_locked.append(i)
            else:
                free.append(i)    
        
        if len(left_locked) > len(free): return False

        for i in range(len(free)):
            if len(left_locked)==0:
                break
            
            f = free.pop()
            l = left_locked.pop()
            if f < l:
                return False
        
        if len(free) % 2 == 1: return False

        return True
    
sol = Solution()
s = "(()))()))(()((()()(((()))()()()()()())))()()(()())()(()((()()((()((((((()(()()(()()())(((((())((()))))()(((((((()()())()))())((((((()(())())()((())()()((())((((())(((())(())()()))(((()()())())))((()))))()()()((()))())(())(((()()((())(())(())())()((()))())(())()(()())((((()(((())((()()())(((()(((((()))()))))))(()((())())(())))))(())(((())()()(()))())())))(((())))()()))()())))))())()(()()))(())(()())))())()))((((())(()))()(((())())(()(()))()))((()(())()()))))())(()(((((()"
locked = "110001111001011100000100011110101000100110010010011001110010111111100111000100000000101111101001111111011101001110011001001100100001100000000010100010101101100000100001000110111000111110110010111011010010100011111101110011100010010001111001010001001000111101101111111011001000100111100110101000100011011001001100110011111111111100101000100111111100000100101101000101111101000011110001001011111010011010000100100000000011101011001110000110011000100001110101100101111111110100"
print(sol.canBeValid(s, locked))        