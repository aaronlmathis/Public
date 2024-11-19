"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #Write helper function to remove character's before # as well as # from string
        def parse(s) -> str:
            stack= []
            for c in s:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)
        
        return parse(s) == parse(t)

        

sol = Solution()        
s = "ab#c"
t = "add#c"
print(sol.backspaceCompare(s, t))