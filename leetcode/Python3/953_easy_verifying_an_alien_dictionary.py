"""
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. 
The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically 
in this alien language.


Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
"""
from typing import List
from collections import defaultdict
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        #Create a hash map of the alien alphabet and its corresponding place in the alphabet....
        alien_dict = {char: i for i, char in enumerate(order)}

        # Iterate through the word list, comparing words in pairs.

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]

            # Compare letters in word1 and word2 for as long as the length of the smaller word.
            for j in range(min(len(word1), len(word2))):
                # If the place of the character in word 1 is greater than the place of the character in word2, return False
                if alien_dict[word1[j]] > alien_dict[word2[j]]:
                    return False
                #If the place of the character word 1 is less than the place of the character of word 2 and the characters are not the same, break
                if alien_dict[word1[j]] < alien_dict[word2[j]] and word1[j] != word2[j]:
                    break
            else:
                # Assuming we finished checking characters and they were all the same, make sure second word isn't shorter than first.
                if len(word1) > len(word2):
                    return False
                    
        return True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
sol = Solution()
print(sol.isAlienSorted(words, order))
words = ["kuvp","q"]
order ="ngxlkthsjuoqcpavbfdermiywz"
print(sol.isAlienSorted(words, order))