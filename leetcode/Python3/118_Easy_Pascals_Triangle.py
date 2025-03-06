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



