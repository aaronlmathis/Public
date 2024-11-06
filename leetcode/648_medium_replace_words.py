"""
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. 
For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. 
If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.
"""
from typing import List

# Create TrieNode class

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

#Create Trie Class

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def find_root(self, word):
        """
        Returns the shortest root for a word if present; otherwise, returns None.
        """
        node = self.root
        root = ""
        for char in word:
            if char not in node.children:
                return None  # No matching root found
            node = node.children[char]
            root += char
            if node.is_end_of_word:
                return root  # Return the root as soon as we reach the end of a root word
        return None  # No root found for the word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        words = sentence.split()
        replaced_words = []
        for word in words:
            root = trie.find_root(word)
            if root:
                replaced_words.append(root)
            else:
                replaced_words.append(word)
        
        return ' '.join(replaced_words)
    
dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
sol = Solution()
print(sol.replaceWords(dictionary, sentence))