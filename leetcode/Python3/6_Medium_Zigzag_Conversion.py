"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        if numRows == 1 or l == 1:
            return s

        matrix = [['_'] * (l // 2 +1 ) for _ in range(numRows)]

        y, x = 0, 0
        down = True
        for i in range(l):
           # Place the current character in the matrix
            matrix[y][x] = s[i]

            # Adjust row (y) based on direction
            if down:
                if y < numRows - 1:
                    y += 1
                else:
                    down = False
                    y -= 1
                    x += 1  # Move to the next column when switching direction
            else:
                if y > 0:
                    y -= 1
                    x += 1  # Move to the next column in the upward direction
                else:
                    down = True
                    y += 1
        answer = ''
        for row in matrix:
            for cell in row:
                if cell != '_':
                    answer += cell         
        return answer

sol = Solution()
s = "PAYPALISHIRING"
#Out"PAHNAPLSIIGYIR"
numRows = 3
print(sol.convert(s, numRows))
s = "PAYPALISHIRING"
numRows = 4
print(sol.convert(s, numRows))