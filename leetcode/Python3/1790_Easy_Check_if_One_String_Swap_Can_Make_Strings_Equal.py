"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

Constraints:
1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Quick exit if strings are equal
        if s1 == s2:
            return True
        n = len(s1)
        # Create `diffs` list that will hold tuple's storing differences found at each index in s1, and s2.
        # For example, if at index 0, s1[0] = 'b' and s2[0] = 'k' then diffs[0] = ('b', 'k')
        diffs = []
        
        # Iterate through both strings at the same time, storing differences. Exit script early if more than 2 differences are found.
        for i in range(n):
            if s1[i] != s2[i]:
                diffs.append((s1[i], s2[i]))
            if len(diffs) > 2:
                return False
                    
        # Return true if a1 == b2 and b1 == a2 in diffs = (a, b), (a, b) - or return false if two differences weren't found.
        # This would mean that two differences were found, and they correspond with eachother (found at same indexes in both strings and are opposites)  
        return (diffs[0][0] == diffs[1][1] and diffs[0][1] == diffs[1][0]) if len(diffs) > 1 else False



sol = Solution()
s1 = "bank"
s2 = "kanb"        #True
print(f"{sol.areAlmostEqual(s1, s2)}\tExpected: True")
s1 = "attack"
s2 = "defend"    #False
print(f"{sol.areAlmostEqual(s1, s2)}\tExpected: False")
s1 = "kelb"
s2 = "kelb"        #True
print(f"{sol.areAlmostEqual(s1, s2)}\tExpected: True")
s1 ="yhy"
s2 ="hyc"
print(f"{sol.areAlmostEqual(s1, s2)}\tExpected: False")