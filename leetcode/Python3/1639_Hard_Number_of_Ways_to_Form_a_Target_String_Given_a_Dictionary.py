"""
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")

Let dp[i][j] represent the number of ways to form the first i characters of the target using characters up to position j in the words.

Iterate through each character of the target and, for each position in the words, multiply the frequency of the target character at that position by the number of ways to form the previous part of the target.
"""
from typing import List
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        if not words or not words[0]:
            return 0
        
        target_len = len(target)
        word_len = len(words[0])

        MOD = 10**9 + 7

        letter_freq = [[0] * word_len for _ in range(26)]

        for word in words:
            for idx, character in enumerate(word):
                letter_freq[ord(character) - 97][idx]+=1
        
        dp = [[0] * (word_len + 1) for _ in range(target_len + 1)]
        for j in range(word_len + 1):
            dp[0][j] = 1

        for i in range(1, target_len + 1):
            for j in range(1, word_len + 1):
                dp[i][j] = (dp[i][j-1] + (letter_freq[ord(target[i-1]) - 97][j-1] * dp[i-1][j- 1])) % MOD

        return dp[target_len][word_len]

words = ["acca","bbbb","caca"]
target = "aba"        
sol = Solution()
print(sol.numWays(words, target))