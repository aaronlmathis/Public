"""
You are given a string s that consists of lowercase English letters.
A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.
Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
Input: s = "aaaa"
Output: 2
Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
It can be shown that the maximum length achievable is 2.

Example 2:
Input: s = "abcdef"
Output: -1
Explanation: There exists no special substring which occurs at least thrice. Hence return -1.

Example 3:
Input: s = "abcaba"
Output: 1
Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
It can be shown that the maximum length achievable is 1.
 
"""
from collections import defaultdict
class Solution:
    def maximumLength(self, s: str) -> int:
        # Function for checking if each window is filled with same character.
        def is_homogenous(s: str) -> bool:
            for i in range(len(s) - 1):
                if s[i] != s[i + 1]:
                    return False
            return True
        
        n = len(s)
        if n < 3:
            return -1
        longest = -1
        low, high = 1, n
        counts = defaultdict(int)
        while low <= high:
            found = False
            print(f"{low} - {high}")
            k = (low + high) // 2
            print(f"K: {k}")
            for i in range(n-k+1):
                window = s[i:i+k]
                if is_homogenous(window):
                    counts[window]+=1
                    if counts[window] > 2:
                        longest = max(longest, k)
                        found = True
            if found:
                low = k+1
            else:
                high = k-1
        print(counts)
        return longest
            
s = "abcaba"
sol = Solution()
print(sol.maximumLength(s))