import collections
import heapq

class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list)
        for (src, dst), prob in zip(edges, succProb):
            adj[src].append((dst, prob))
            adj[dst].append((src, prob))

        max_heap = [(-1.0, start_node)]  
        visited = set()
        max_prob = {start_node: 1.0}  
        
        while max_heap:
            prob, cur = heapq.heappop(max_heap)
            prob = -prob  

            if cur in visited:
                continue  
            visited.add(cur)

            if cur == end_node:
                return prob  

            for nei, edge_prob in adj[cur]:
                new_prob = prob * edge_prob
                if new_prob > max_prob.get(nei, 0): 
                    max_prob[nei] = new_prob
                    heapq.heappush(max_heap, (-new_prob, nei))

        return 0.0

sol = Solution()

n = 5
edges = [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]]
succProb =[0.37,0.17,0.93,0.23,0.39,0.04]
start = 3
end =4

print(sol.maxProbability(n, edges, succProb, start, end))

n = 3
edges =[[0,1]]
succProb =[0.5]
start = 0
end = 2

#print(sol.maxProbability(n, edges, succProb, start, end))

"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge 
connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
 
"""        