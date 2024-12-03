"""
Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s.

Example 1:

Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4
Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
Example 2:

Input: sentence = "this problem is an easy problem", searchWord = "pro"
Output: 2
Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.
Example 3:

Input: sentence = "i am tired", searchWord = "you"
Output: -1
Explanation: "you" is not a prefix of any word in the sentence.
"""
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        widx = 1
        wordStart = 0
        n = len(sentence)
        
        for i in range(n + 1):  # Loop through sentence with an additional index for the last word
            if i == n or sentence[i] == ' ':
                # Extract the current word from word_start to i
                if sentence[wordStart:i].startswith(searchWord):
                    return widx
                widx += 1
                wordStart = i + 1  # Start of the next word
        return -1

sol = Solution()
sentence = "i love eating burger"
searchWord = "burg"
print(sol.isPrefixOfWord(sentence,searchWord))