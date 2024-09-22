"""
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

Example 1:
Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.

Example 2:
Input: n = 1, k = 1
Output: 1
"""
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
       # Function to count steps between curr and n within a lexicographical order
        def count_steps(curr: int, n: int) -> int:
            steps = 0
            first = curr
            last = curr
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps

        # Start with the prefix "1"
        curr = 1
        k -= 1  # As we consider 1 as the first lexicographical number
        
        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                # If we can skip this prefix and move to the next one
                k -= steps
                curr += 1
            else:
                # Otherwise, we go deeper into the prefix
                curr *= 10
                k -= 1

        return curr

n = 6516650
k = 3611122       
sol = Solution()
print(sol.findKthNumber(n, k))
