"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 
"""
from typing import List
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Initialize the adjacency list
        graph = defaultdict(list)

        # Building the graph
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend].append((divisor, value))       # a -> b with weight 
            graph[divisor].append((dividend, 1 / value))   # b -> a with weight
        
        # Recursive Depth-First-Search function
        #   - Break if node equals target - return the accumulated total of multiplied weights
        #   - Iterate through all graph neighbors, travel to unvisited nodes, multiplying weights of the edges
        def dfs(node, target, accumulated, visited):
            if node == target:
                return accumulated
            
            visited.add(node)

            for  nnode, weight in graph[node]:
                if nnode not in visited:
                    result = dfs(nnode, target, accumulated * weight, visited)
                    if result != -1.0:
                        return result
            return -1.0
        
        # Process each query. If C or D is not in graph, return -1. If C == D, return 1, otherwise, call DFS and return accumulated weight of edges.
        results = []
        for C, D in queries:
            if C not in graph or D not in graph:
                results.append(-1.0)
                continue
            if C == D:
                results.append(1.0)
                continue
            result = dfs(C, D, 1, set())
            results.append(result)

        return results

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
sol = Solution()
print(sol.calcEquation(equations, values, queries))