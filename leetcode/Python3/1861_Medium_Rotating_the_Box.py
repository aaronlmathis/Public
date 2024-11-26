"""
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
Example 2:



Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
Example 3:



Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]

from typing import List
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Let m and n be the length of box (rows) and box[0] (cols)
        m = len(box)
        n = len(box[0])
        # Create newBox as n x m
        newBox = [[0] * m for _ in range(n)]

        # Fill newBox from original box (rotate it 90 degrees)
        for i in range(m):
            for j in range(n):
                newBox[j][m - 1 - i] = box[i][j]

        # Let m and n be the length of newBox (rows) and newBox[0] (cols)
        m = len(newBox)
        n = len(newBox[0])
        for j in range(n):  # Iterate column by column
            empty = m - 1  # Start from the bottom of the column
            for i in range(m - 1, -1, -1):  # Move upwards
                if newBox[i][j] == "*":  # Obstacle encountered
                    empty = i - 1  # Update empty to just above the obstacle
                elif newBox[i][j] == "#":  # Rock encountered
                    if empty != i:  # Slide the rock only if necessary
                        newBox[empty][j], newBox[i][j] = newBox[i][j], "."  # Swap
                        empty -= 1  # Move empty upwards
        # Return the new box!
        return newBox
"""
from typing import List
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Get the dimensions of the box
        ROWS = len(box)
        COLS = len(box[0])

        # Step 1: Simulate sliding rocks ('#') downwards within each row
        for r in range(ROWS):
            # Start from the last column (rightmost position to slide rocks)
            i = COLS - 1
            for c in reversed(range(COLS)):  # Traverse the row in reverse order
                if box[r][c] == "#":
                    # If we find a rock, swap it with the position at 'i'
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1  # Update the next available position for the rock
                elif box[r][c] == "*":
                    # If we find an obstacle, reset 'i' to just before the obstacle
                    i = c - 1

        # Step 2: Rotate the box 90 degrees clockwise
        newBox = []
        for c in range(COLS):  # Iterate through each column of the original box
            col = []
            for r in reversed(range(ROWS)):  # Traverse the rows in reverse for rotation
                col.append(box[r][c])  # Add elements to the new column
            newBox.append(col)  # Append the rotated column to the new box
        
        return newBox

box = [["#",".","*","."],
              ["#","#","*","."]]
sol = Solution()
print(sol.rotateTheBox(box))