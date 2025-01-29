"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""
import time
def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after =  time.time()
        fname = function.__name__
        print(f"{fname} took {round(after-before, 3)} seconds to execute!")
        return value
    return wrapper

from typing import List
from collections import deque
class Solution:
    @timed
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        DFS Solution

        """
        """
        def dfs(node):
            if node in rec_stack:  # Cycle detected
                return False
            if node in visited:    # Node already fully processed
                return True

            # Mark the node as being processed
            rec_stack.add(node)

            # Visit all neighbors
            for next_node in graph[node]:
                if not dfs(next_node):  # Cycle found in a neighbor
                    return False

            # Mark the node as fully processed
            rec_stack.remove(node)
            visited.add(node)
            answer.append(node)  # Add to the topological order
            return True

        # Create adjacency list of sets where graph[b] -> {a}
        graph = [set() for _ in range(numCourses)]
        answer = []
        visited = set()
        rec_stack = set()      # Tracks nodes in the current recursion stack
        
        for a, b in prerequisites:
            graph[b].add(a)

        # Perform DFS for all nodes
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):  # If a cycle is detected, return an empty list
                    return []
        return answer[::-1]

        BFS Solution
        
        """
        # Create adjacency list of sets where graph[b] -> {a}
        # Create an in_degree list to count the number of edges going into each class
        graph = [set() for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for a, b in prerequisites:
            graph[b].add(a)
            in_degree[a]+=1

        # Create a queue of classes that have 0 in_degree (meaning they don't have prerequisites)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        answer = []

        # Process the queue - each iteration:
        #   - Add the current course to the answer because it doesn't require anything
        #   - Iterate through the classes that require the current course.
        #       - reduce the in_degree of the next course by 1
        #       - if the in_degree is 0, add it to the queue because it can now be taken.
        while queue:
            course = queue.popleft()
            answer.append(course)
            for next in graph[course]:
                in_degree[next]-=1
                if in_degree[next] == 0:
                    queue.append(next)
        # Only return the answer if the length of answer is equal to the number of courses (meaning every class was taken)
        # If answer is shorter than numCourses, it means a cycle was detected and its impossible to satisfy prerequisites
        return answer if len(answer) == numCourses else []
    
numCourses = 3
prerequisites = [[1,0],[1,2],[0,1]]
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
sol = Solution()
print(sol.findOrder(numCourses, prerequisites))