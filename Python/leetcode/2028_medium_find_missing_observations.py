"""
You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. 
Fortunately, you have also calculated the average value of the n + m rolls.
You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.
Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. 
If there are multiple valid answers, return any of them. If no such array exists, return an empty array.
The average value of a set of k numbers is the sum of the numbers divided by k.
Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

Example 1:

Input: rolls = [3,2,4,3], mean = 4, n = 2
Output: [6,6]
Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
Example 2:

Input: rolls = [1,5,6], mean = 3, n = 4
Output: [2,3,2,2]
Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.
Example 3:

Input: rolls = [1,2,3,4], mean = 6, n = 4
Output: []
Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.
"""
from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_rolls = len(rolls) + n
        total_sum = mean * total_rolls
        missing_sum = total_sum - sum(rolls)
        
        # Check if the missing_sum is achievable with n dice rolls
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        # Distribute the missing sum across the n dice
        base_value = missing_sum // n
        remainder = missing_sum % n
        
        result = [base_value] * n
        
        # Distribute the remainder to make up the exact sum
        for i in range(remainder):
            result[i] += 1
        
        return result


sol = Solution()
rolls = [3,2,4,3]
mean = 4 
n = 2   
print(sol.missingRolls(rolls, mean, n))     

