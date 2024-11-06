class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        for i in arr:
            if i % 2 == 0:
                count = 0
            else:
                count+=1
            
            if count > 2:
                return True
        
        return False

sol = Solution()
arr = [2,6,4,1, 3, 5]
print(sol.threeConsecutiveOdds(arr))