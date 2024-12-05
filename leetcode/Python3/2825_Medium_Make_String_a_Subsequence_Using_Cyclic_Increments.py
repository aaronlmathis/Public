"""
You are given two 0-indexed strings str1 and str2.

In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.

Note: A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.

Example 1:
Input: str1 = "abc", str2 = "ad"
Output: true
Explanation: Select index 2 in str1.
Increment str1[2] to become 'd'. 
Hence, str1 becomes "abd" and str2 is now a subsequence. Therefore, true is returned.

Example 2:
Input: str1 = "zc", str2 = "ad"
Output: true
Explanation: Select indices 0 and 1 in str1. 
Increment str1[0] to become 'a'. 
Increment str1[1] to become 'd'. 
Hence, str1 becomes "ad" and str2 is now a subsequence. Therefore, true is returned.

Example 3:
Input: str1 = "ab", str2 = "d"
Output: false
Explanation: In this example, it can be shown that it is impossible to make str2 a subsequence of str1 using the operation at most once. 
Therefore, false is returned.
"""
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # Set s1, s2 to the length of str1, str2
        s1, s2 = len(str1), len(str2)
        
        # Quick exit: If s2 is longer than s1, then there are not enough characters in s1 to make a subsequence that equals s2.
        if s2 > s1:
            return False

        # If both s1 and s2 are the same length, we can iterate through using one loop, checking 3 different conditions.
        if s1 == s2:
            for i in range(s1):
                # If there is an 'a' in str2 and a 'z' in str1 (since z->a) continue
                if str2[i] == 'a' and str1[i] == 'z':
                    continue
                # If str1[i] is equal to str2[i] (we don't have to make a shift)
                elif str1[i] == str2[i]:
                    continue

                elif ord(str2[i]) - ord(str1[i]) != 1:
                    return False
            # If the loop finishes without returning False, then it is possible to make a subsequence, return true
            return True
        
        # List to track letters that are in str2 but not str1.
        letters = []

        # Iterate through str2, if a character is not in str1, append it to letters
        for char in str2:
            if char not in str1:
                letters.append(char)
        # c is a counter that tracks valid shift operations, you need c to equal the length of letters
        # Since letters is full of characters that are in str2 but not in str1, you need to have a shiftable char in str1 for every char in letters.        
        c = 0

        # Iterate through letters
        for char in letters:
            # Is the character thats made from the unicode code of char minus 1 (a shift) found in str1, IF so, this is valid shift, increase counter
            if chr(ord(char)-1) in str1:
                c+=1
            # Is char an 'a' and 'z' is in str1? A valid shift.. increase counter.
            if char == 'a' and 'z' in str1:
                c+=1
        # Return whether a valid shift was found for every letter in letters.
        return c == len(letters)

sol = Solution()
strs = [
    ["abc", "ad"],
    ["zc", "ad"],
    ["ab", "d"]
]        
for i in range(len(strs)):
    print(f"Example: {i+1}")
    print(sol.canMakeSubsequence(strs[i][0], strs[i][1]))
    print()
    