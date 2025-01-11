"""
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

Example 1:
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:
Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:
Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
"""
from collections import deque, Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        #  Essentially, the easiest way to solve this is to rule out impossibilities:
        #   - If the length of s is less than k, return False
        #   - If the length of n is equal to k, you know you can do k number of one letter pallindromes so return true
        #   - If the number of characters in s that have an odd number of counts is greater than k, return False
        n = len(s)
        if n < k: return False
        if n == k: return True
        odd_count = 0
        for char in set(s):
            odd_count = odd_count + 1 if s.count(char) % 2 == 1 else odd_count
        if odd_count > k: return False
        return True
    
sol = Solution()

s = "annabelle"
k = 2
print(f"1) Answer: True\t\tOutput: {sol.canConstruct(s, k)}")
s = "leetcode" 
k = 3        
print(f"2) Answer: False\tOutput: {sol.canConstruct(s, k)}")
s = "true"
k = 4
print(f"3) Answer: True\t\tOutput: {sol.canConstruct(s, k)}")
s= "cxayrgpcctwlfupgzirmazszgfiusitvzsnngmivctprcotcuutfxdpbrdlqukhxkrmpwqqwdxxrptaftpnilfzcmknqljgbfkzuhksxzplpoozablefndimqnffrqfwgaixsovmmilicjwhppikryerkdidupvzdmoejzczkbdpfqkgpbxcrxphhnxfazovxbvaxyxhgqxcxirjsryqxtreptusvupsstylpjniezyfokbowpbgxbtsemzsvqzkbrhkvzyogkuztgfmrprz"
k=5
print(f"4) Answer: False\tOutput: {sol.canConstruct(s, k)}")
s = "yzyzyzyzyzyzyzy"
k = 2
print(f"5) Answer: True\t\tOutput: {sol.canConstruct(s, k)}")