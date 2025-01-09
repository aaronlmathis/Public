"""
You are given an array of strings words and a string pref.
Return the number of strings in words that contain pref as a prefix.
A prefix of a string s is any leading contiguous substring of s.

Example 1:
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

Example 2:
Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
"""
from typing import List, Optional
"""   
class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.word_count = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str):
        current_node = self.root
        for char in word:
            k = ord(char) - ord('a')
            if current_node.children[k] == None:
                newNode = TrieNode()
                current_node.children[k] = newNode
            current_node = current_node.children[k]
        current_node.word_count += 1
    
    def count_prefix(self, prefix: str) -> int:
        current_node = self.root
        for char in prefix:
            k = ord(char) - ord('a')
            if current_node.children[k] is None:
                return 0
            current_node = current_node.children[k]
        
        def count_words(node: TrieNode) -> int:
            count = node.word_count
            for child in node.children:
                if child is not None:
                    count += count_words(child)
            return count
        
        return count_words(current_node)
    
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.count_prefix(pref)
"""     
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for word in words:
            if word.startswith(pref):
                ans+=1
        return ans
words = ["pay","attention","practice","attend"]
pref = "at"        
sol = Solution()
print(sol.prefixCount(words,pref))