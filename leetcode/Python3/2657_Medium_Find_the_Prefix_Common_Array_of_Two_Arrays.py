"""
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

Example 1:
Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

Example 2:
Input: A = [2,3,1], B = [3,1,2]
Output: [0,1,3]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: only 3 is common in A and B, so C[1] = 1.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
"""
from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        fa, fb = [0] * (len(A)+1), [0] * (len(A)+1)
        ans = []
        common = 0
        for i in range(len(A)):
            fa[A[i]]+=1
            fb[B[i]]+=1
            ans.append(sum(1 for ac, bc in zip(fa, fb) if ac==1 and bc==1))
        """
        # Create two boolean arrays that track whether a number i has been seen.
        sa, sb = [False] * (len(A)+1), [False] * (len(A)+1)
        
        # Keep a running count of common prefixes as well as an answer array to return
        count = 0
        ans = []

        # Zip up A and B to compare their values at each index. Set sa[a] and sb[b] True because the number has been seen.
        # Increase count if:
        #   - number a has already been seen in list B.
        #   - number b has already been seen in list A (if a does not equal b)
        # Append the updated count to answer each iteration.
        for a, b in zip(A, B):
            sa[a], sb[b] = True, True

            if sb[a]:
                count+=1

            if a != b and sa[b]:
                count+=1
            
            ans.append(count)
        
        return ans
        
            



sol = Solution()
A = [1,3,2,4]
B = [3,1,2,4]    
print(f"{sol.findThePrefixCommonArray(A, B)}\t\tExpected: [0,2,3,4]" )
A = [2,3,1]
B = [3,1,2]
print(f"{sol.findThePrefixCommonArray(A, B)}\t\tExpected: [0,1,3]" )