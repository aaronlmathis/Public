# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize matrix with -1
        matrix = [[-1] * n for _ in range(m)]

        # Directions for spiral traversal: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def isValid(x, y):
            return 0 <= x < m and 0 <= y < n and matrix[x][y] == -1

        x, y = 0, 0  # Start position
        dir_index = 0  # Start direction: right
        while head:
            matrix[x][y] = head.val
            head = head.next

            # Move in the current direction
            next_x, next_y = x + directions[dir_index][0], y + directions[dir_index][1]

            # If next position is out of bounds or already filled, change direction
            if not isValid(next_x, next_y):
                dir_index = (dir_index + 1) % 4
                next_x, next_y = x + directions[dir_index][0], y + directions[dir_index][1]

            x, y = next_x, next_y

        return matrix        
sol = Solution()

m = 3
n = 5
head = [3,0,2,6,8,1,7,9,4,2,5,5,0]        