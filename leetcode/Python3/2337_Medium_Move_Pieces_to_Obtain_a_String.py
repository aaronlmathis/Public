"""
You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

Example 1:
Input: start = "_L__R__R_", target = "L______RR"
Output: true
Explanation: We can obtain the string target from start by doing the following moves:
- Move the first piece one step to the left, start becomes equal to "L___R__R_".
- Move the last piece one step to the right, start becomes equal to "L___R___R".
- Move the second piece three steps to the right, start becomes equal to "L______RR".
Since it is possible to get the string target from start, we return true.

Example 2:
Input: start = "R_L_", target = "__LR"
Output: false
Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
After that, no pieces can move anymore, so it is impossible to obtain the string target from start.

Example 3:
Input: start = "_R", target = "R_"
Output: false
Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.
"""
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start == target:
            return True
        
        unmatched_lefts = 0  # Tracks how many `L`s need to move left
        unmatched_rights = 0  # Tracks how many `R`s need to move right
        
        for start_char, target_char in zip(start, target):
            if start_char == 'R':
                if unmatched_lefts > 0:  # `R` is blocked by unmatched `L`s
                    return False
                unmatched_rights += 1  # Increment count of unmatched `R`s
            if target_char == 'L':
                if unmatched_rights > 0:  # `L` is blocked by unmatched `R`s
                    return False
                unmatched_lefts += 1  # Increment count of unmatched `L`s
            if target_char == 'R':
                if unmatched_rights == 0:  # No unmatched `R`s to align
                    return False
                unmatched_rights -= 1  # Match an `R`
            if start_char == 'L':
                if unmatched_lefts == 0:  # No unmatched `L`s to align
                    return False
                unmatched_lefts -= 1  # Match an `L`
        
        return unmatched_lefts == 0 and unmatched_rights == 0


        """
        print(start)
        print(target)
        # Set n to the length of start
        n = len(start)
        # Quick Exit - Start cannot Target if they have unequal lengths
        if n != len(target):
            return False
        # Quick Exit - With all '_' removed, start should equal target
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        # Iterate from the left, ensuring that no L in start is farther left then its corresponding L in target (because L's can't move right)
        ls, lt = 0,0
        while ls < n and start[ls] != "R" and lt < n and target[lt] != "R":
            # If the currenct character in start is '_' then keep iterating right
            while ls < n-1 and start[ls]  == '_':
                ls+=1
            # If the currenct character in target is '_' then keep iterating right
            while lt < n-1 and target[lt] == '_':
                lt+=1
            print(f"Debug:  L {ls} - {lt}")
            # start[ls] and start[lt] should now both be on a non '_' character. Check if the index of start[lt] is greater than the index of start[ls]. This means that the L in target is farther right than the L in start and L's can't move right so return false
            if target[lt] == 'L' and start[ls] == 'L' and lt > ls:
                return False
            # Both indexes are on a valid character, and they aren't in invalid positions,so increment both and start the loop all over again, checking for the next L
            ls+=1
            lt+=1
        
        # Iterate from the right, ensuring that no R in start is farther right then its corresponding R in target (because R's can't move left)
        rs, rt = n-1,n-1
        while rs > 0 and start[rs] != "L" and rt > 0 and target[rt] != "L":
            # If the currenct character in start is '_' then keep iterating left
            while  rs > 0 and start[rs] == '_':
                rs-=1
            # If the currenct character in target is '_' then keep iterating left
            while rt > 0 and target[rt] == '_':
                rt-=1
            # start[lrs] and start[rt] should now both be on a non '_' character. Check if the index of start[rt] is less than the index of start[rs]. This means that the R in target is farther left than the R in start and R's can't move left so return false
            if target[rt] == 'R' and start[rs] == 'R' and rt < rs:
                return False
            
            # Both indexes are on a valid character, and they aren't in invalid positions,so increment both and start the loop all over again, checking for the next R
            rs-=1
            rt-=1
        # Return True because False was never returned, so start must be able to become target.
        return True
    """
start ="_R"
target ="R_"
sol = Solution()
#start = ["_L__R__R_", "R_L_", "_R","_LL__R__R_","_____R","L_L","R_R"]         
#target = ["L______RR", "__LR", "R_","L___L___RR","____R_","_LL","RR_"]

#for i in range(len(start)):
#    print(f"Example: {i+1}")
print(sol.canChange(start, target))
