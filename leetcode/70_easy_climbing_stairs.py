class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        n1, n2 = 1,2
        for x in range(3, n+1):
            w = n2 + n1
            n1 = n2
            n2 = w
        return w


sol = Solution()
n = 10
print(sol.climbStairs(n))
