"""
There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.
"""
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_bottles = 0
        full_bottles = numBottles
        empty_bottles = 0
        
        while empty_bottles >= numExchange or full_bottles>0:

            empty_bottles += full_bottles
            max_bottles += full_bottles
            full_bottles = 0
            full_bottles = empty_bottles // numExchange
            empty_bottles-=full_bottles * numExchange


        return max_bottles

sol = Solution()
numBottles = 9
numExchange = 3
print(sol.numWaterBottles(numBottles, numExchange))# 13
numBottles = 15
numExchange = 4
print(sol.numWaterBottles(numBottles, numExchange)) # 19

