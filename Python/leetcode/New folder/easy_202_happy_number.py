class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)            
            arr = [int(c) for c in str(n)]
            n = sum([v**2 for v in arr])
            if n == 1:
                return True
        return False
       


sol = Solution()
print(sol.isHappy(19))