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

        n = len(word)
        
        # Dictionary for char counts and hashset for O(1) lookup of vowels.
        char_count = defaultdict(int)
        vowels = {'a', 'e','i','o','u'}

        substrings = 0

        # Count the first letter in word
        char = word[0]
        if char in vowels:
            char_count['vowels'] += 1
            char_count[char] += 1
        else:
            char_count['consts'] += 1

        # Dynamic Sliding-Window
        # - Left: 0, R: 1. Iterate R to n-1.
        # - Every iteration:
        #   - Take count of total consonants and individual vowels.
        #   - If consonants reach or equal k, and vowels have at least one each, increase count.
        #   - If consonants exceed k, shrink window by moving left to the index first consonant + 1, increase count
        left = 0
        
        for right in range(1, n):
            print(f"{left} - {right}")
            char = word[right]
            if char in vowels:
                char_count['vowels']+=1
                char_count[char] += 1
            else:
                char_count['consts'] += 1
            
            if right - left + 1 >= 5 + k and char_count['consts'] == k:       # k reached, suitable window size
                # Check that all vowels are at least 1
                if all(char_count[x] > 0 for x in vowels):
                    print('Valid Substring:1')
                    substrings+=1
                
                # Now shrink window until left is on the first consonant. Remove it from count and increase left once more.
                while left != n-1 and word[left] in vowels:
                    left+=1
                    print(f"{left} - {right} shrink")
                    if right - left + 1 >= 5 + k:
                        if all(char_count[x] > 0 for x in vowels):
                            substrings+=1

                char_count['consts']-=1
                left+=1
            
            if right - left + 1 >= 5 + k and char_count['consts'] == k:       # k reached, suitable window size
                # Check that all vowels are at least 1
                if all(char_count[x] > 0 for x in vowels):
                    print('Valid Substring:1')
                    substrings+=1
        return substrings
 


sol = Solution()

k = 1
word = "aeioqq"
k = 1
word = "aeiou"
k = 0

word = "ieaouqqieaouqq"
k = 1

#word ="iqeaouqi"
#k=2
print(sol.countOfSubstrings(word, k))