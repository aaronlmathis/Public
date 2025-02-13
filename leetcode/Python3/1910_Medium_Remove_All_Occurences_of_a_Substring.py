"""
Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.

Example 1:
Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".

Example 2:
Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"
Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".

Constraints:
1 <= s.length <= 1000
1 <= part.length <= 1000
s​​​​​​ and part consists of lowercase English letters.
"""
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Set `part_len` to the length of part and initialize `stack`
        part_len = len(part)
        stack = []

        # Iterate through every character in `s`
        for ch in s:
            # Append current character `ch` to `stack` 
            stack.append(ch)
            # Check if stack is big enough to contain `part` yet and 
            # if the last `part_len` characters equals `part` when joined into a string
            if len(stack) >= part_len and ''.join(stack[-part_len:]) == part:
                # If so, delete that part of the stack.
                del stack[-part_len:] 
        # Return the joined string formed from `stack`
        return ''.join(stack)

sol = Solution()
s = "daabcbaabcbc"
part = "abc"    
print(f"{sol.removeOccurrences(s, part)} - dab")    
s = "axxxxyyyyb"
part = "xy"
print(f"{sol.removeOccurrences(s, part)} - ab")    