"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

"""
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        x = len(s)
        i = 0
        newString = s
        while i < x:
            newString =  newString[1:] + newString[0:1] 
            if newString == goal:
                return True
            i+=1
        return False
    
    #    return len(s) == len(goal) and goal in (s + s)   - One Liner

s = "abcde"
goal = "cdeab"        
sol = Solution()
print(sol.rotateString(s, goal))