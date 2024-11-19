"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of digits
        digits = list(str(num))
        
        # Track the rightmost position of each digit (0 to 9)
        last = {int(d): i for i, d in enumerate(digits)}
        print(last)
        
        # Traverse the digits to find the first digit that can be swapped
        for i, d in enumerate(digits):
            # Check for a larger digit to the right
            for j in range(9, int(d), -1):
                if last.get(j, -1) > i:
                    # Perform the swap
                    digits[i], digits[last[j]] = digits[last[j]], digits[i]
                    return int(''.join(digits))
        
        # If no swap can improve the number, return the original number
        return num
num = 2736
sol = Solution()
print(sol.maximumSwap(num))

