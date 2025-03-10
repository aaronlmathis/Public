"""

You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

Example 1:
Input: word = "aeioqq", k = 1
Output: 0
Explanation:
There is no substring with every vowel.

Example 2:
Input: word = "aeiou", k = 0
Output: 1
Explanation:
The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:
Input: word = "ieaouqqieaouqq", k = 1
Output: 3
Explanation:
The substrings with every vowel and one consonant are:
word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".

Constraints:
5 <= word.length <= 2 * 105
word consists only of lowercase English letters.
0 <= k <= word.length - 5
"""
from collections import defaultdict
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        char_count = defaultdict(int)
        vowels = {'a', 'e','i','o','u'}
        consts = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
        for char in word:
            if char in vowels:
                char_count['vowels'] += 1
                char_count[char] += 1
            else:
                char_count['consts'] += 1
        print(char_count)

sol = Solution()
word = "ieaouqqieaouqq"
k = 1
print(sol.countOfSubstrings(word, k))