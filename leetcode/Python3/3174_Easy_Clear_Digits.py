"""
You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
- Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.
 
Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.

Example 2:
Input: s = "cb34"
Output: ""
Explanation:
First, we apply the operation on s[2], and s becomes "c4".
Then we apply the operation on s[1], and s becomes "".

Constraints:
1 <= s.length <= 100
s consists only of lowercase English letters and digits.
The input is generated such that it is possible to delete all digits.
"""
class Solution:
    def clearDigits(self, s: str) -> str:
        # Let `n` be equal to the length of `s`
        # We will use `n` to iterate over `s`
        n = len(s)

        # Initialize a set that contains numbers 0-9
        numbers = {'0','1','2','3','4','5','6','7','8','9'}

        # Initialize a list for our `stack`
        stack = []

        # Iterate over `s` 
        for i in range(n):
            # If `s[i]`` is in the `numbers` set, pop the stack
            # This will remove the item inserted before it (to the left)
            if s[i] in numbers:
                    stack.pop()
            # If `s[i]` is not a number, add it to `stack`
            else:
                stack.append(s[i])
       
        # Join `stack` into a str and return it
        return ''.join(stack)


sol = Solution()
s = "abc"
s = "cb34"
print(sol.clearDigits(s))