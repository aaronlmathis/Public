"""
There are n teams numbered from 0 to n - 1 in a tournament; each team is also a node in a DAG.

You are given the integer n and a 0-indexed 2D integer array edges of length m representing the DAG, where edges[i] = [ui, vi] indicates that there is a directed edge from team ui to team vi in the graph.

A directed edge from a to b in the graph means that team a is stronger than team b and team b is weaker than team a.

Team a will be the champion of the tournament if there is no team b that is stronger than team a.

Return the team that will be the champion of the tournament if there is a unique champion, otherwise, return -1.

Notes

A cycle is a series of nodes a1, a2, ..., an, an+1 such that node a1 is the same node as node an+1, the nodes a1, a2, ..., an are distinct, and there is a directed edge from the node ai to node ai+1 for every i in the range [1, n].
A DAG is a directed graph that does not have any cycle.
 
"""
from typing import List
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Create a list where i represents each team and teams[i] represents whether team i can be the champion.
        # All teams start with the ability to be the champion (True)
        teams = [True] * n

        # Iterate through the edges, since each edge [u, v] means team u is better than team v, we know that teams[v] becomes False
        # They cannot be the champion if someone is better than them.
        for u, v in edges:
            teams[v] = False
        
        # Set the initial champion to -1
        champion = -1
        champCount = 0
        # Iterate teams looking for any team that is still able to be the champion
        # If found, set champion to the id of that team and increase the champCount by one.
        # If champCount is one, return the champion, otherwise return -1
        for i in range(n):
            if teams[i]:
                champCount+=1
                champion = i
        # Only one team is still able to be champion, return it's id
        return champion if champCount == 1 else -1

sol = Solution()
n = 4
edges = [[0,2],[1,3],[1,2]]        
print(sol.findChampion(n, edges))
n = 3
edges = [[0,1],[1,2]]
print(sol.findChampion(n, edges))