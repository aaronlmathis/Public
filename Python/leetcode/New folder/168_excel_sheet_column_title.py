class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        res = ""
        while columnNumber > 0:
            offset = (columnNumber -1) % 26
            res += chr(ord('A') + offset)
            columnNumber = (columnNumber -1) // 26
        
        return res[::-1]
sol = Solution()
print(sol.convertToTitle(701))