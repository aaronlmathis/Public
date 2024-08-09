class Solution:
  def isValid(self, s: str) -> bool:
        # Dictionary to map closing brackets to their corresponding opening brackets
        matching_brackets = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in matching_brackets.values():
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
            elif char in matching_brackets.keys():
                # If it's a closing bracket, check if it matches the top of the stack
                if stack and stack[-1] == matching_brackets[char]:
                    stack.pop()
                else:
                    return False  # Mismatch found
            else:
                return False  # Invalid character (though the problem states we only get valid characters)

        return len(stack) == 0  # If stack is empty, all brackets were matched

s = ['(', '(', '{', '}', '[', ']' ]
sol = Solution()
print(s)
print(sol.isValid(s))

