"""
Given the string s, return the size of the longest substring containing each vowel an even number of times. 
That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

Example 1:
Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
"""
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Mapping vowels to their respective bit positions
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        # Initialize variables
        prefix_xor = 0  # Initial XOR (no vowels yet)
        first_occurrence = {0: -1}  # To handle substrings starting from the beginning
        max_length = 0
        
        # Traverse through the string
        for i, char in enumerate(s):
            # If the character is a vowel, update the prefix_xor
            if char in vowels:
                prefix_xor ^= (1 << vowels[char])  # Flip the corresponding bit for the vowel
            
            # If this prefix_xor has been seen before, calculate the length of the substring
            if prefix_xor in first_occurrence:
                max_length = max(max_length, i - first_occurrence[prefix_xor])
            else:
                # If it's the first time seeing this prefix_xor, store the index
                first_occurrence[prefix_xor] = i

        return max_length



sol = Solution()
s = "eleetminicoworoep"
print(sol.findTheLongestSubstring(s))