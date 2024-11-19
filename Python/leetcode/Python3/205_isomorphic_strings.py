"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, 
but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        """
        s_count = {c: s.count(c) for c in s}
        t_count = {c: t.count(c) for c in t}
        
        seen1 = []
        for c in s:
            seen1.append(str(s_count[c]))
        
        seen2 = []
        for c in t:
            seen2.append(str(t_count[c]))

        print(seen1)
        print(seen2)
        if seen1 == seen2:
            return True
        """
        map_s_to_t = {}
        map_t_to_s = {}

        for char_s, char_t in zip(s, t):
            print(f"S: {char_s} T: {char_t}")
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t
           
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            else:
                map_t_to_s[char_t] = char_s
                                
        return True


sol = Solution()

s = "badc"
t = "baba"
print(sol.isIsomorphic(s, t))

s = "bbbaaaba"
t = "aaabbbba"
print(sol.isIsomorphic(s, t))
