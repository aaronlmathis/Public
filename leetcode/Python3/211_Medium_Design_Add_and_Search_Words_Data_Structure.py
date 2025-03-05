"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"function_name took {after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper
from collections import deque
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            i = ord(c) - 97
            if node.children[i] is not None:
                node = node.children[i]
            else:
                node.children[i] = TrieNode()
                node = node.children[i]
        node.isEndOfWord = True
                
    @timed
    def search(self, word: str) -> bool:
        node = self.root
        n = len(word)
        stack = [(node, 0)]
        while stack:
            curr, idx = stack.pop()
            if idx == n:
                if curr.isEndOfWord == True:
                    return True
                else:
                    return False
            
            if word[idx] == '.':
                for child in curr.children:
                    if child is not None:
                        stack.append((child, idx+1))
            else:
                i = ord(word[idx]) - 97
                if curr.children[i] is None:
                    continue
                else:
                    stack.append((curr.children[i], idx+1))
        

    def search_recursive(self, word: str, node=None, idx=0) -> bool:
        if node is None:
            node = self.root  # Start from root on initial call

        if idx == len(word):
            return node.isEndOfWord  # Return True if it's a valid word

        if word[idx] == '.':
            # Explore all children nodes if wildcard
            for child in node.children:
                if child and self.search_recursive(word, child, idx + 1):
                    return True
        else:
            i = ord(word[idx]) - 97
            if node.children[i] and self.search_recursive(word, node.children[i], idx + 1):
                return True

        return False  # No valid path found



    def print_dictionary(self, node=None, prefix="", depth=0):
        if node==None:
            node = self.root
        for i, child in enumerate(node.children):
            if child:
                char = chr(i + ord('a'))
                marker = "*" if child.isEndOfWord else ""
                print("  " * depth + f"└── {char}{marker}")
                self.print_dictionary(child, prefix + char, depth + 1)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
obj = WordDictionary()
obj.addWord('mississippi')
obj.addWord('miss')
obj.addWord('aaron')

obj.addWord('cat')
obj.addWord('catastrophe')
obj.addWord('catastrophic')
obj.addWord('mister')
obj.print_dictionary()
print(obj.search('.i.siss.pp.'))
print(obj.search('.at'))
print(obj.search('c.t'))
print(obj.search('c..'))

print(obj.search_recursive('.i.siss.pp.'))
print(obj.search_recursive('.at'))
print(obj.search_recursive('c.t'))
print(obj.search_recursive('c..'))