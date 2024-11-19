class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        highest_profit_seen = 0
        for k, v in enumerate(prices):
            for i in range(k, len(prices)):
                if v < prices[i]:
                    if (prices[i] - v) > highest_profit_seen:
                        highest_profit_seen = prices[i] - v

        return highest_profit_seen
    
sol = Solution()
prices = [7,6,4,3,1]

print(sol.maxProfit(prices))