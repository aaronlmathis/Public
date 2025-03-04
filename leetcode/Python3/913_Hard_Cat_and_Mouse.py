"""
A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.

The mouse starts at node 1 and goes first, the cat starts at node 2 and goes second, and there is a hole at node 0.

During each player's turn, they must travel along one edge of the graph that meets where they are.  For example, if the Mouse is at node 1, it must travel to any node in graph[1].

Additionally, it is not allowed for the Cat to travel to the Hole (node 0).

Then, the game can end in three ways:

    - If ever the Cat occupies the same node as the Mouse, the Cat wins.
    - If ever the Mouse reaches the Hole, the Mouse wins.
    - If ever a position is repeated (i.e., the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.

Given a graph, and assuming both players play optimally, return

     - 1 if the mouse wins the game,
     - 2 if the cat wins the game, or
     - 0 if the game is a draw.


Example 1:
nput: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0

Example 2:
Input: graph = [[1,3],[0],[3],[0,2]]
Output: 1
 
Constraints:
3 <= graph.length <= 50
1 <= graph[i].length < graph.length
0 <= graph[i][j] < graph.length
graph[i][j] != i
graph[i] is unique.
The mouse and the cat can always move. 
"""
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"function_name took {after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper

from typing import List
from collections import defaultdict, deque

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        distance = [60 for _ in range(n)]

        queue = deque([(0, 0)])     # Node 0, Distance 0
        visited = {0}
        while queue:
            curr, dist = queue.popleft()
            distance[curr] = dist
            for neigh in graph[curr]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh, dist+1))
        
        game_state = set()
        game_state.add((1, 2, 1))

        game = deque([(1, 2, 0)])   # Mouse pos, cat pos, turn (0 mouse, 1 cat)
        while game:
            mpos, cpos, turn = game.popleft()
            print(f"M: {mpos} C: {cpos}")
            if turn == 0:   # Mouses turn
                td = 60 # Temporary distance (max)
                for move in graph[mpos]:
                    if move == 0:
                        return 1
                    if distance[move] < td and move != cpos:
                        nmove = move
                        td = distance[move]
                next = (nmove, cpos, 1)
                game.append(next)
                if next in game_state:
                    return 0
                else:
                    game_state.add(next)
            
            else:   # Cats turn
                td = 60 # Temporary distance (max)
                for move in graph[cpos]:
                    if move == 0:
                        continue
                    if move == mpos:
                        return 2
                    if distance[move] < td:
                        nmove = move
                        td = distance[move]
                next = (mpos, nmove, 0)
                game.append(next)
                if next in game_state:
                    return 0
                else:
                    game_state.add(next)

sol = Solution()
graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
graph = [[3,4],[3,5],[3,6],[0,1,2],[0,5,6],[1,4],[2,4]]
print(sol.catMouseGame(graph))        