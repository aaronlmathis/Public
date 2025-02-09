"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 
"""
from typing import List
import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = {}
        min_heap = [(0, k)]
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in dist:
                continue
            dist[node] = time
            for neighbor, travel_time in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(min_heap, (time + travel_time, neighbor))
        print(dist)
        # If not all nodes are reached, return -1.
        if len(dist) != n:
            return -1

        return max(dist.values())
sol = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

print(sol.networkDelayTime(times, n, k))