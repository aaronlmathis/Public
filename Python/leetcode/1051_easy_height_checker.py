
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        count = 0
        for k,v in enumerate(heights):
            if v != expected[k]:
                count+=1

        return count



sol = Solution()
heights = [1,1,4,2,1,3]
print(sol.heightChecker(heights))
