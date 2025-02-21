"""
You are given an integer n denoting the number of nodes of a weighted directed graph. The nodes are numbered from 0 to n - 1.

You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes that there exists a directed edge from fromi to toi with weight weighti.

Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct nodes of the graph.

Return the minimum weight of a subgraph of the graph such that it is possible to reach dest from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph does not exist, return -1.

A subgraph is a graph whose vertices and edges are subsets of the original graph. The weight of a subgraph is the sum of weights of its constituent edges.

 

Example 1:
Input: n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5
Output: 9
Explanation:
The above figure represents the input graph.
The blue edges represent one of the subgraphs that yield the optimal answer.
Note that the subgraph [[1,0,3],[0,5,6]] also yields the optimal answer. It is not possible to get a subgraph with less weight satisfying all the constraints.

Example 2:
Input: n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2
Output: -1
Explanation:
The above figure represents the input graph.
It can be seen that there does not exist any path from node 1 to node 2, hence there are no subgraphs satisfying all the constraints.
 
Constraints:

3 <= n <= 105
0 <= edges.length <= 105
edges[i].length == 3
0 <= fromi, toi, src1, src2, dest <= n - 1
fromi != toi
src1, src2, and dest are pairwise distinct.
1 <= weight[i] <= 105
"""
from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        
        # Build our graph
        graph = defaultdict(dict)
        reverse_graph = defaultdict(dict)
        for x,y,v in edges:
            graph[x][y] = min(v,graph[x][y]) if y in graph[x] else v
            reverse_graph[y][x] = min(v,reverse_graph[y][x]) if x in reverse_graph[y] else v

        def dijkstra(graph, start):
            # Step 1: Initialize min-heap, distances, and visited set
            pq = [(0, start)]  # (distance, node)
            dist = {node: float('inf') for node in graph}
            dist[start] = 0

            while pq:
                # Step 2: Extract the node with the smallest distance
                current_dist, node = heapq.heappop(pq)

                # Step 3: Skip if this is an outdated distance
                if current_dist > dist[node]:
                    continue

                # Step 4: Relax all edges
                for neighbor, weight in graph[node]:
                    new_dist = current_dist + weight

                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))

            return dist  # Shortest distances from start node

        dist_from_src1 = dijkstra(graph, src1)
        dist_from_src2 = dijkstra(graph, src2)
        dist_to_dest = dijkstra(reverse_graph, dest)

        valid_costs = [
            dist_from_src1[x] + dist_from_src2[x] + dist_to_dest[x]
            for x in graph
            if dist_from_src1[x] < float('inf') and dist_from_src2[x] < float('inf') and dist_to_dest[x] < float('inf')]


        return min(valid_costs) if valid_costs else -1




sol = Solution()
n = 6
edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]
src1 = 0
src2 = 1
dest = 5
print(sol.minimumWeight(n, edges, src1, src2, dest))
n = 3
edges = [[0,1,1],[2,1,1]]
src1 = 0
src2 = 1
dest = 2
print(sol.minimumWeight(n, edges, src1, src2, dest))
n = 8
edges = [[4,7,24],[1,3,30],[4,0,31],[1,2,31],[1,5,18],[1,6,19],[4,6,25],[5,6,32],[0,6,50]]
src1 = 4
src2 = 1
dest = 6
#print(sol.minimumWeight(n, edges, src1, src2, dest))
n=5
src1 = 0
src2 = 1
dest = 4
edges = [[0,2,1],[0,3,1],[2,4,1],[3,4,1],[1,2,1],[1,3,10]]
#print(sol.minimumWeight(n, edges, src1, src2, dest))
"""
        min_common_weight = float('inf')
        possible = []
        for path1, weight1 in src1_paths:
            for path2, weight2 in src2_paths:
                common_path = [dest]
                x = -2
                while x > -len(path2) and x > -len(path1) and path2[x] == path1[x]:
                    common_path.append(path2[x])
                    x-=1
                if len(common_path) > 1:
                    possible.append((path1, path2, common_path))
                    common_weight = weight1 + weight2
                    common_path = common_path[::-1]
                    for i in range(len(common_path)-1):
                        common_weight -= weights[common_path[i]][common_path[i+1]]
                    if common_weight < min_common_weight:
                        min_common_weight = common_weight

                    

        #print(possible)
        min_path = min(min_combo_path, min_src1_path + min_src2_path, min_common_weight)
        return min_path if min_path != float('inf') else -1

"""