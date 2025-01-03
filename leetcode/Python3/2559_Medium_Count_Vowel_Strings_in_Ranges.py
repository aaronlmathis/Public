"""
You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:
Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].

Example 2:
Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation: Every string satisfies the conditions, so we return [3,2,1].
"""
from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Hash set for vowels for quick comparisons.        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        # n = number of words
        n = len(words)
        # Initialize prefix sum array of size n+1
        pf = [0] * (n + 1)
        # Fill prefix sum array  
        for i in range(n):
            pf[i + 1] = pf[i] + (1 if words[i][0] in vowels and words[i][-1] in vowels else 0)

        # compute answer for each range (left, right) inclusive by subtracting the left value in pf from the right+1 value of pf.
        ans = []
        for left, right in queries:
            ans.append(pf[right + 1] - pf[left])

        return ans
sol = Solution()        
words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]

print(sol.vowelStrings(words, queries))