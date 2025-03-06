
"""
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        for i in range(numRows - 1):
            tmp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(tmp[j] + tmp[j+1])
            res.append(row)
        return res

sol = Solution()
numRows = 5
print(sol.generate(numRows))



from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = 0         # Index of the lowest price seen so far.
        max_profit = -1         # max profit seen for a trade
        sell = 1
        while sell < n:
            if prices[sell] < prices[buy]:
                buy = sell
                sell+=1
                continue

            profit = prices[sell] - prices[buy]
            if max_profit < profit:
                max_profit = profit
            sell+=1
        return max_profit
sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))    

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [1] * (n+1)
        suffix_sum = [1] * (n+1)
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] * nums[i-1]
        for i in range(n-1, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] * nums[i]
        ans = [suffix_sum[1]]
        for i in range(1, n):
            ans.append(suffix_sum[i+1] * prefix_sum[i])
        print(prefix_sum)
        print(suffix_sum)
        print("[24,12,8,6]")
        print(ans)

sol = Solution()
nums = [1,2,3,4]        
print(sol.productExceptSelf(nums))

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        ans=''
        for mid in range(1, n):
            left = mid-1

            while left >= 0 and n-1-mid >= mid - left:
                window = s[left:mid]
                if window == s[mid]:
                    pdrome = window+s[mid]
                    if len(pdrome) > len(ans):
                        ans=pdrome
                mirror = s[mid+1:mid+1+mid-left][::-1]
                if window == mirror :
                    pdrome = window+s[mid]+mirror
                    if len(pdrome) > len(ans):
                        ans = pdrome
                left-=1
        return ans
sol = Solution()
s = "babad"
print(sol.longestPalindrome(s))


√(x1 - x2)2 + (y1 - y2)2).
"""
from typing import List
import heapq
from math import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        x1, y1 = 0, 0
        for x2, y2 in points:
            distance =  -((x1 - x2) ** 2 + (y1 - y2) ** 2)
            if len(distances) >= k:
                heapq.heappushpop(distances, (distance, [x2,y2]))
            else:
                heapq.heappush(distances, (distance, [x2,y2]))

        return [point for _, point in distances]
sol = Solution()
points = [[1,3],[-2,2]]
k = 1
print(sol.kClosest(points,k))
