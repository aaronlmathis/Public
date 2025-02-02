"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.

There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 
"""
from collections import defaultdict
from typing import List
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in trust:
            graph[a].append(b)

        in_degree = [0] * (n+1)
        for _, trustees in graph.items():
            for trustee in trustees:
                in_degree[trustee]+=1
        
        for i in range(1, n+1):
            if in_degree[i] == n-1 and len(graph[i]) == 0:
                return i
        return -1


sol = Solution()
n = 3
trust = [[1,3],[2,3]]
print(sol.findJudge(n, trust))