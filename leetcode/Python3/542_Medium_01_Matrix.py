from collections import deque, defaultdict
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        distance = [[-1 for _ in range(n)] for _ in range(m)]
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    distance[i][j] = 0

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            crow, ccol = queue.popleft()

            for dr, dc in dir:
                nr, nc = crow + dr, ccol + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) and distance[nr][nc] == -1:
                    distance[nr][nc] = distance[crow][ccol] + 1
                    queue.append((nr, nc))
        return distance



sol = Solution()
mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(sol.updateMatrix(mat))