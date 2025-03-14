"""
You are given two integers n and x. You have to construct an array of positive integers nums of size n where 
for every 0 <= i < n - 1, nums[i + 1] is greater than nums[i], 
and the result of the bitwise AND operation between all elements of nums is x.
Return the minimum possible value of nums[n - 1].

Example 1:
Input: n = 3, x = 4
Output: 6
Explanation:
nums can be [4,5,6] and its last element is 6.

Example 2:
Input: n = 2, x = 7
Output: 15
Explanation:
nums can be [7,15] and its last element is 15.
"""
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x  # Start with `result` as `x` to retain its set bits.
        remaining = n - 1  # `remaining` represents bits from `n - 1` to be merged into `x`.
        position = 1  # `position` tracks the current bit position to check and potentially modify in `result`.
    
        # Loop until there are no more set bits left in `remaining`.
        while remaining:
            # Check if the current `position` in `x` is unset (i.e., equal to 0).
            if not (x & position):
                # If `position` in `x` is unset, set this position in `result` using the current least significant bit of `remaining`.
                result |= (remaining & 1) * position  # Set bit in `result` based on the current bit in `remaining`.
                
                # Shift `remaining` right by one to check the next bit in the next loop iteration.
                remaining >>= 1
            # Shift `position` left to move to the next bit position.
            position <<= 1
    
        return result  # Return the final merged result.







sol = Solution()
n = 3
x = 1
print(sol.minEnd(n, x))