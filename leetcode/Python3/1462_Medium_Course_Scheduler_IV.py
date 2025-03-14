"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.

Example 2:
Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.

Example 3:
Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]
"""
from typing import List
from collections import defaultdict, deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for prereq, postreq in prerequisites:
            graph[prereq].append(postreq)

        postreq_set = [set() for _ in range(numCourses)]
    
        def dfs(course):
            for postreq in graph[course]:
                if postreq not in postreq_set[course]:
                    postreq_set[course].add(postreq)
                    postreq_set[course].update(dfs(postreq))
            return postreq_set[course]
            
        for i in range(numCourses):
            dfs(i)
        
        res = []
        for prereq, postreq in queries:
            if postreq not in postreq_set[prereq]:
                res.append(False)
            else:
                res.append(True)
        return res

sol = Solution()
numCourses = 2
prerequisites = [[1,0]]
queries = [[0,1],[1,0]]     
#Output: [false,true]

numCourses = 3
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]
# Output: [true,true]
numCourses = 5
prerequisites = [[0,1],[1,2],[2,3],[3,4]]
queries = [[0,4],[4,0],[1,3],[3,0]]
print(sol.checkIfPrerequisite(numCourses, prerequisites, queries))