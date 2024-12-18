"""
You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

 

Example 1:

Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explanation: 
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
For items 3 and 4 you will not receive any discount at all.
Example 2:

Input: prices = [1,2,3,4,5]
Output: [1,2,3,4,5]
Explanation: In this case, for all items, you will not receive any discount at all.
Example 3:

Input: prices = [10,1,1,6]
Output: [9,0,1,6]
 
"""
from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []  # Monotonic decreasing stack of indices
        ans = prices[:]  # Copy of prices for the result

        for i, price in enumerate(prices):
            # While stack is not empty and current price is less than or equal to price at the stack's top
            while stack and prices[stack[-1]] >= price:
                ans[stack.pop()]-= price
            # Push current index onto the stack
            stack.append(i)

        return ans

prices = [8,4,6,2,3]
#Output: [4,2,4,2,3]        
sol = Solution()
print(sol.finalPrices(prices))
