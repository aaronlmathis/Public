"""
There is an undirected graph with n nodes, numbered from 0 to n - 1.

You are given a 0-indexed integer array scores of length n where scores[i] denotes the score of node i. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A node sequence is valid if it meets the following conditions:

    ` There is an edge connecting every pair of adjacent nodes in the sequence.
    ` No node appears more than once in the sequence.
The score of a node sequence is defined as the sum of the scores of the nodes in the sequence.

Return the maximum score of a valid node sequence with a length of 4. If no such sequence exists, return -1.

 

Example 1:
Input: scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output: 24
Explanation: The figure above shows the graph and the chosen node sequence [0,1,2,3].
The score of the node sequence is 5 + 2 + 9 + 8 = 24.
It can be shown that no other node sequence has a score of more than 24.
Note that the sequences [3,1,2,0] and [1,0,2,3] are also valid and have a score of 24.
The sequence [0,3,2,4] is not valid since no edge connects nodes 0 and 3.

Example 2:
Input: scores = [9,20,6,4,11,12], edges = [[0,3],[5,3],[2,4],[1,3]]
Output: -1
Explanation: The figure above shows the graph.
There are no valid node sequences of length 4, so we return -1.

Constraints:
n == scores.length
4 <= n <= 5 * 104
1 <= scores[i] <= 108
0 <= edges.length <= 5 * 104
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
There are no duplicate edges.
"""
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"{fname} took {after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper
from collections import defaultdict
from typing import List

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        # DFS with Backtracking helper function
        def explore(node, depth, current_score):
            nonlocal max_score
                
            # Base Case - sequence has length of 4.
            if depth == 4:
                max_score = max(max_score, current_score)
                return

            if current_score + (4 - depth) * ms <= max_score:
                return

            if node not in graph:
                return
            # Choose next neighboring node from top 3 scoring neighbors and explore it
            for neighbor in graph[node]:
                if neighbor not in visited:                    
                    visited.add(neighbor)
                    explore(neighbor, depth+1, current_score + scores[neighbor])
                    visited.remove(neighbor)
        
        # Initialize `n` as the number of nodes in graph
        n = len(scores)

        # Initialize `max_score` as -1
        max_score = -1

        # Initialize ms as the max score in scores
        ms = max(scores)

        # Build graph of nodes with undirected edges
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Initialize visited set
        visited = set()

        # Sort highest scores first
        for node in graph:
            graph[node].sort(key=lambda x: scores[x], reverse=True) 
        
        sorted_nodes = sorted(range(n), key=lambda x: scores[x], reverse=True)           
        
        # Explore from every node as a starting point, starting with nodes with largest scores
        for idx in sorted_nodes:
            explore(idx, 1, scores[idx])

        return max_score        

sol = Solution()
scores = [5,2,9,8,4]
edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]    
scores = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,4,4,10,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
edges = [[0,100],[1,100],[2,100],[3,100],[4,100],[5,100],[6,100],[7,100],[8,100],[9,100],[10,100],[11,100],[12,100],[13,100],[14,100],[15,100],[16,100],[17,100],[18,100],[19,100],[20,100],[21,100],[22,100],[23,100],[24,100],[25,100],[26,100],[27,100],[28,100],[29,100],[30,100],[31,100],[32,100],[33,100],[34,100],[35,100],[36,100],[37,100],[38,100],[39,100],[40,100],[41,100],[42,100],[43,100],[44,100],[45,100],[46,100],[47,100],[48,100],[49,100],[50,100],[51,100],[52,100],[53,100],[54,100],[55,100],[56,100],[57,100],[58,100],[59,100],[60,100],[61,100],[62,100],[63,100],[64,100],[65,100],[66,100],[67,100],[68,100],[69,100],[70,100],[71,100],[72,100],[73,100],[74,100],[75,100],[76,100],[77,100],[78,100],[79,100],[80,100],[81,100],[82,100],[83,100],[84,100],[85,100],[86,100],[87,100],[88,100],[89,100],[90,100],[91,100],[92,100],[93,100],[94,100],[95,100],[96,100],[97,100],[98,100],[99,100],[100,101],[101,102],[102,103],[104,103],[105,103],[106,103],[107,103],[108,103],[109,103],[110,103],[111,103],[112,103],[113,103],[114,103],[115,103],[116,103],[117,103],[118,103],[119,103],[120,103],[121,103],[122,103],[123,103],[124,103],[125,103],[126,103],[127,103],[128,103],[129,103],[130,103],[131,103],[132,103],[133,103],[134,103],[135,103],[136,103],[137,103],[138,103],[139,103],[140,103],[141,103],[142,103],[143,103],[144,103],[145,103],[146,103],[147,103],[148,103],[149,103],[150,103],[151,103],[152,103],[153,103],[154,103],[155,103],[156,103],[157,103],[158,103],[159,103],[160,103],[161,103],[162,103],[163,103],[164,103],[165,103],[166,103],[167,103],[168,103],[169,103],[170,103],[171,103],[172,103],[173,103],[174,103],[175,103],[176,103],[177,103],[178,103],[179,103],[180,103],[181,103],[182,103],[183,103],[184,103],[185,103],[186,103],[187,103],[188,103],[189,103],[190,103],[191,103],[192,103],[193,103],[194,103],[195,103],[196,103],[197,103],[198,103],[199,103],[200,103],[201,103],[202,103],[203,103]]
#scores = [9,20,6,4,11,12]
#edges = [[0,3],[5,3],[2,4],[1,3]]    
print(sol.maximumScore(scores, edges))