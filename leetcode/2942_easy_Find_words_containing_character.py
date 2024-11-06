"""
You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order.

Example 1:

Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
Example 2:

Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
Output: [0,2]
Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.
Example 3:

Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
Output: []
Explanation: "z" does not occur in any of the words. Hence, we return an empty array.
 
"""
from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []  # Initialize answer list

        """ Nested Loop Solution

        for i in range(len(words)): # Iterate through each word in the words list, tracking the index.
            for c in words[i]: #Iterate through each character in the word
                if c == x: # Check for the X letter
                    ans.append(i) # If found, add the index of the word to the answer list and break the loop.
                    break 
        """
        """ Single Loop solution

        for i, word in enumerate(words):
            if x in word:
                ans.append(i)
        """
        for i in range(0, len(words)):
            incl = words[i].find(x)
            if incl >= 0:
                ans.append(i)

        return ans # Return the answer list

sol = Solution()
words = ["leet","code"]
x = "e"
print(sol.findWordsContaining(words, x))