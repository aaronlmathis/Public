"""
You are given an array of non-overlapping axis-aligned rectangles rects where rects[i] = [ai, bi, xi, yi] indicates that (ai, bi) is the bottom-left corner point of the ith rectangle and (xi, yi) is the top-right corner point of the ith rectangle. Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. A point on the perimeter of a rectangle is included in the space covered by the rectangle.

Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.

Note that an integer point is a point that has integer coordinates.

Implement the Solution class:

Solution(int[][] rects) Initializes the object with the given rectangles rects.
int[] pick() Returns a random integer point [u, v] inside the space covered by one of the given rectangles.
 

Example 1:


Input
["Solution", "pick", "pick", "pick", "pick", "pick"]
[[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
Output
[null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]

Explanation
Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
solution.pick(); // return [1, -2]
solution.pick(); // return [1, -1]
solution.pick(); // return [-1, -2]
solution.pick(); // return [-2, -2]
solution.pick(); // return [0, 0]
(x - a + 1) * (y - b + 1)
"""


import random
import bisect
from typing import List

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = []
        total = 0
        for rect in rects:
            x1, y1, x2, y2 = rect
            # Number of integer points in the rectangle
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            total += area
            self.prefix.append(total)
        self.total = total

    def pick(self) -> List[int]:
        rand = random.randint(1, self.total)
        # Find the rectangle index using binary search
        idx = bisect.bisect_left(self.prefix, rand)
        rect = self.rects[idx]
        x1, y1, x2, y2 = rect
        # Calculate the area before this rectangle
        prev = self.prefix[idx - 1] if idx > 0 else 0
        # Offset within the rectangle
        offset = rand - prev - 1
        # Map the offset to (x, y)
        width = x2 - x1 + 1
        x = x1 + (offset % width)
        y = y1 + (offset // width)
        return [x, y]

solution = Solution([[-2, -2, 1, 1], [2, 2, 4, 6]])
print(solution.pick()) # return [1, -2]
print(solution.pick()) # return [1, -1]
print(solution.pick()) # return [-1, -2]
print(solution.pick()) # return [-2, -2]
print(solution.pick()) # return [0, 0]
# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()