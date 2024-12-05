"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].
"""
from typing import List
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        totalLen = wordLen * len(words)
        wordCount = Counter(words)
        
        result = []
        for i in range(wordLen):
            left, right = i, i
            currentCount = Counter()
            while right + wordLen <= len(s):
                word = s[right:right + wordLen]
                right+=wordLen
                if word in wordCount:
                    currentCount[word]+=1
                    while currentCount[word] > wordCount[word]:
                        leftWord = s[left:left + wordLen]
                        currentCount[leftWord] -= 1
                        left += wordLen
                    if right - left == totalLen:
                        result.append(left)
                else:
                    currentCount.clear()
                    left = right
        return result

s = "barfoofoobarthefoobarman" 
words = ["bar","foo","the"]
sol = Solution()
print(sol.findSubstring(s, words))        