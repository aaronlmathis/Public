"""
Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string

Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:
Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.
"""
from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Create a string from words with a space between each item
        sentence = ' '.join(words)
        # Iterate through words, checking to see if sentence.count() > 1 for each item
        answer = [subarray for subarray in words if sentence.count(subarray) > 1]
        return answer


words = ["mass","as","hero","superhero"]     
sol = Solution()
print(sol.stringMatching(words))   