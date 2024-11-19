from math import sqrt

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = round(sqrt(c))
        sq = 0

        while b >= a:
            sq = a*a + b*b
            if sq == c:
                return True
            elif sq > c:
                b-=1
            else:
                a+=1

        return False
  
c = 3
sol = Solution()
print(sol.judgeSquareSum(c))
