import collections
import heapq

class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append([dst, succProb[i]])
            adj[dst].append([dst, succProb[i]])
        
        pq = [(-1, start)]
        visit = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            visit.add(cur)

            if cur == end:
                return prob * -1
            for nei, edgeProb in adj[cur]:
                if nei not in visit:
                    heapq.heappush(pq, (prob * edgeProb, nei))


sol = Solution()

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

print(sol.maxProbability(n, edges, succProb, start, end))

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.3]
start = 0
end = 2

print(sol.maxProbability(n, edges, succProb, start, end))

"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge 
connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
 
"""        