"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 
"""
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Total number of characters we need to match in t
        total_chars_needed = len(t)

        # Quick exit conditions
        if total_chars_needed > len(s) or total_chars_needed == 0:
            return ""
        if t in s:
            return t

        # Dictionary to store character frequency in t
        char_frequency = defaultdict(int)
        for char in t:
            char_frequency[char] += 1

        # Result tuple to store the start and end indices of the minimum window
        result = (0, len(s) + 1)

        # Start pointer for the sliding window
        window_start = 0

        # Iterate through the string with the end pointer
        for window_end, char in enumerate(s):
            # Check if the current character is in t
            if char in char_frequency:
                # If the character is still needed, decrease the count of needed characters
                if char_frequency[char] > 0:
                    total_chars_needed -= 1
                # Decrease the character count in the frequency dictionary
                char_frequency[char] -= 1

            # When all characters from t are matched
            if total_chars_needed == 0:
                # Try to shrink the window from the left to find the smallest valid window
                while True:
                    start_char = s[window_start]
                    # If the start character is not part of t, move the start pointer forward
                    if start_char not in char_frequency:
                        window_start += 1
                        continue
                    # If the start character is still needed, stop shrinking the window
                    if char_frequency[start_char] == 0:
                        break
                    # Increment the count for the start character in the frequency dictionary
                    char_frequency[start_char] += 1
                    # Move the start pointer forward
                    window_start += 1

                # Update the result if the current window is smaller than the previous smallest
                if window_end - window_start + 1 < result[1] - result[0]:
                    result = (window_start, window_end + 1)

                # Move the start pointer forward to look for the next valid window
                char_frequency[s[window_start]] += 1
                total_chars_needed += 1
                window_start += 1

        # Return the minimum window substring or an empty string if no valid window was found
        return '' if result[1] > len(s) else s[result[0]:result[1]]

    

s = "ADOBECODEBANC"
t = "ABC"
#s = "a"
#t = "a"
sol = Solution()
print(sol.minWindow(s, t))        