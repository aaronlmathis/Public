class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        costc = 0
        for i in range(len(gas)):
            costc -= cost[gas[i]]

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
sol = Solution()
print(sol.canCompleteCircuit(gas, cost)) # 3