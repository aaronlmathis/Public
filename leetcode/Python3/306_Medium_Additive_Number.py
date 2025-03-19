"""
An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:
Input: "112358"
Output: true
Explanation: 
The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:
Input: "199100199"
Output: true
Explanation: 
The additive sequence is: 1, 99, 100, 199. 
1 + 99 = 100, 99 + 100 = 199

Constraints:
1 <= num.length <= 35
num consists only of digits.
 
Follow up: How would you handle overflow for very large input integers?
"""
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        ls = []
        flag = False

        def backtrack(index):
            nonlocal flag
            if index == len(num):
                if len(ls) < 3:
                    return
                # Check additive property for the complete sequence
                for i in range(2, len(ls)):
                    if ls[i] != ls[i-1] + ls[i-2]:
                        return
                flag = True
                return

            for i in range(index, len(num)):
                # Skip numbers with leading zeros
                if num[index] == '0' and i > index:
                    break
                curr = int(num[index:i+1])
                # If we have at least two numbers, check if the current number fits
                if len(ls) >= 2 and curr != ls[-1] + ls[-2]:
                    continue
                ls.append(curr)
                backtrack(i+1)
                ls.pop()

        backtrack(0)
        return flag

sol = Solution()
num = "199100199"
print(sol.isAdditiveNumber(num))