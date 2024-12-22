"""
You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.
If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].
You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.
Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1.

Example 1:
Input: heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
Output: [2,5,-1,5,2]
Explanation: In the first query, Alice and Bob can move to building 2 since heights[0] < heights[2] and heights[1] < heights[2]. 
In the second query, Alice and Bob can move to building 5 since heights[0] < heights[5] and heights[3] < heights[5]. 
In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
In the fourth query, Alice and Bob can move to building 5 since heights[3] < heights[5] and heights[4] < heights[5].
In the fifth query, Alice and Bob are already in the same building.  
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.

Example 2:
Input: heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
Output: [7,6,-1,4,6]
Explanation: In the first query, Alice can directly move to Bob's building since heights[0] < heights[7].
In the second query, Alice and Bob can move to building 6 since heights[3] < heights[6] and heights[5] < heights[6].
In the third query, Alice cannot meet Bob since Bob cannot move to any other building.
In the fourth query, Alice and Bob can move to building 4 since heights[3] < heights[4] and heights[0] < heights[4].
In the fifth query, Alice can directly move to Bob's building since heights[1] < heights[6].
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.
"""
from typing import List
import heapq

class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        # Initialize the result array with default value -1
        results = [-1] * len(queries)
        
        # Group queries by their rightmost index
        queries_by_right_index = [[] for _ in range(len(heights))]
        
        for query_index, (start, end) in enumerate(queries):
            # Ensure start <= end by swapping if necessary
            if start > end:
                start, end = end, start
            
            # If the query is trivial (start == end or heights[start] < heights[end]), record the answer directly
            if start == end or heights[start] < heights[end]:
                results[query_index] = end
            else:
                # Otherwise, group the query by its rightmost index `end`
                queries_by_right_index[end].append((heights[start], query_index))
        
        # Min-heap to track active queries and their conditions
        min_heap = []
        
        # Iterate through heights to process queries
        for current_index, current_height in enumerate(heights):
            # Add queries grouped by the current index to the min-heap
            for query in queries_by_right_index[current_index]:
                heapq.heappush(min_heap, query)
            
            # Process the heap: Remove invalid queries (where heights[start] < current_height)
            while min_heap and min_heap[0][0] < current_height:
                _, query_index = heapq.heappop(min_heap)
                results[query_index] = current_index  # Update result for this query
        
        return results


heights = [6,4,8,5,2,7]
queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]        
sol = Solution()
print(sol.leftmostBuildingQueries(heights, queries))