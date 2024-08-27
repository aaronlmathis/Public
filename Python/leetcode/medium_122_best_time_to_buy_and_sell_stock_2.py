class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        p = 0
        b = prices[0]
        max_profit = 0
        for s in prices[1:]:
            if b < s:
                max_profit += s-b
            b = s
            
        return max_profit
    
sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices)) #7
prices = [1,2,3,4,5]
print(sol.maxProfit(prices)) #4
prices = [7,6,4,3,1]
print(sol.maxProfit(prices))#0