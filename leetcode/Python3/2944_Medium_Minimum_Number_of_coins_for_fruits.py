"""
You are given an integer array prices where prices[i] denotes the number of coins needed to purchase the ith fruit.

The fruit market has the following reward for each fruit:

If you purchase the ith fruit at prices[i] coins, you can get any number of the next (i + 1) fruits for free.
Note that even if you can take fruit j for free, you can still purchase it for prices[j] coins to receive its reward.

Return the minimum number of coins needed to acquire all the fruits.

Example 1:
Input: prices = [3,1,2]
Output: 4
Explanation:
Purchase the 1st fruit with prices[0] = 3 coins, you are allowed to take the 2nd fruit for free.
Purchase the 2nd fruit with prices[1] = 1 coin, you are allowed to take the 3rd fruit for free.
Take the 3rd fruit for free.
Note that even though you could take the 2nd fruit for free as a reward of buying 1st fruit, you purchase it to receive its reward, which is more optimal.

Example 2:
Input: prices = [1,10,1,1]
Output: 2
Explanation:
Purchase the 1st fruit with prices[0] = 1 coin, you are allowed to take the 2nd fruit for free.
Take the 2nd fruit for free.
Purchase the 3rd fruit for prices[2] = 1 coin, you are allowed to take the 4th fruit for free.
Take the 4th fruit for free.
"""
from typing import List
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        coins = prices[0]
        i = 1
        j = i+1
        for i in range(1, len(prices)-1):
            if prices[j] > prices[i]:
                coins+=prices[i]
            else:
                coins+=prices[j]
            i+= 1
            j+= 1
        return coins
    
sol = Solution()
prices = [1,10,1,1]
print(sol.minimumCoins(prices))