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
from collections import defaultdict, Counter
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def f(min_consonants: int) -> int:
            vowel_count = Counter()
            substring_count = 0
            left_pointer = 0
            consonant_count = 0
            
            for right_pointer in range(len(word)):
                current_char = word[right_pointer]
                
                if current_char in "aeiou":
                    vowel_count[current_char] += 1
                else:
                    consonant_count += 1
                
                while consonant_count >= min_consonants and len(vowel_count) == 5:
                    char_at_left = word[left_pointer]
                    
                    if char_at_left in "aeiou":
                        vowel_count[char_at_left] -= 1
                        if vowel_count[char_at_left] == 0:
                            del vowel_count[char_at_left]
                    else:
                        consonant_count -= 1
                    
                    left_pointer += 1
                
                substring_count += left_pointer
            
            return substring_count
        
        return (f(k) - f(k + 1))

sol = Solution()
word = "ieaouqqieaouqq"
k = 1
print(sol.countOfSubstrings(word, k))