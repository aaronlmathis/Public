"""
A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.

For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.
"""

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
         return bin(start ^ goal).count('1')
    """    
        if start == goal:
            return 0
        
        s_start, s_goal = str(bin(start))[2:], str(bin(goal))[2:]
        l = max(len(s_start), len(s_goal))
        s_start = s_start.zfill(l)
        s_goal = s_goal.zfill(l)

        count = 0
        for i in range(l):
            if s_start[i] != s_goal[i]:
                count+=1

        return count
    """      

start = 10
goal = 7
sol = Solution()
print(sol.minBitFlips(start, goal))