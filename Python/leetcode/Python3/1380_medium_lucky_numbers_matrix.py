class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        
        minimums = []
        maximums = []
        columns = []
        rows = matrix
        res = []
        for row in rows:
            minimums.append(min(row))

        column = []
        for i in range(len(matrix[0])):
            column = []
            for ii in range(len(matrix)):
                column.append(matrix[ii][i])
            columns.append(column)

        for col in columns:
            maximums.append(max(col))


        for i in minimums:
            if i in maximums:
                res.append(i)
        return res
        """
        res = []
        
        # Iterate over each row to find the minimum element and its column index
        for i in range(len(matrix)):
            min_value = min(matrix[i])
            min_index = matrix[i].index(min_value)
            
            # Check if this minimum element is the maximum in its column
            if all(min_value >= matrix[k][min_index] for k in range(len(matrix))):
                res.append(min_value)
        
        return res
sol = Solution()
matrix = [[1,10,4,2],
          [9,3,8,7],
          [15,16,17,12]]
print(sol.luckyNumbers(matrix))