"""
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

 

Example 1:
Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.

Example 2:
Input: bombs = [[1,1,5],[10,10,5]]
Output: 1
Explanation:
Detonating either bomb will not detonate the other bomb, so the maximum number of bombs that can be detonated is 1.

Example 3:
Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.
 

Constraints:

1 <= bombs.length <= 100
bombs[i].length == 3
1 <= xi, yi, ri <= 105
"""
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"{fname} took {after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper
from collections import defaultdict, deque
from typing import List
import math
class Solution:
    @timed
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # First we need to build our graph by figuring out which bombs are detonated by each bomb
        # This gives us a directional edge from 'detonated' to 'will detonate'
        graph = defaultdict(set)
               
        # Process every combination of bombs (once) to see if either bomb is in blast radius of other.
        graph = defaultdict(set)
        for i, (sx, sy, sr) in enumerate(bombs):
            for j, (nx, ny, nr) in enumerate(bombs):
                if i != j and (nx - sx) ** 2 + (ny - sy) ** 2 <= sr ** 2:
                    graph[i].add(j)

        n = len(bombs)
        # Now use either DFS or BFS to traverse the graph from each starting bomb to maximize carnage.
        # Exit early if bombs visited equals `n`
        """
        max_bombs = 1
        for start in range(n):
            exploded = {start}
            queue = [start]
            for bomb in queue:
                for neighbor in graph[bomb]:
                    if neighbor not in exploded:
                        exploded.add(neighbor)
                        queue.append(neighbor)
            ne = len(exploded)
            if ne == n:
                return n
            if ne > max_bombs:
                max_bombs = ne
        return max_bombs
        """
        def dfs(bomb, exploded):
            """Recursive DFS function that detonates bombs."""
            exploded.add(bomb)
            for neighbor in graph[bomb]:
                if neighbor not in exploded:
                    dfs(neighbor, exploded)
        
        max_bombs = 0
        
        # Try detonating from each bomb as the starting point
        for start in range(n):
            exploded = set()
            dfs(start, exploded)
            max_bombs = max(max_bombs, len(exploded))
            if max_bombs == n:
                return n  # Early exit if all bombs detonate
        
        return max_bombs
        
        # Build queue by filling it with tuples of `(x, {x})` 
        # where `x` is the starting bomb and `{x}` is a set tracking exploded bombs. 
        queue = deque([(x, {x}) for x in range(n)])   # Start, exploded
        
        max_bombs = 0
        # Process Queue
        while queue:
            bomb, exploded = queue.popleft()
            exploded.add(bomb)
            ne = len(exploded)
            # All bombs have been exploded, so return `n`
            if ne == n:
                return n
            if ne > max_bombs:
                max_bombs = ne

            for neighbor in graph[bomb]:
                if neighbor not in exploded:
                    queue.append((neighbor, exploded))
        
        return max_bombs
bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]        
#bombs = [[2,1,3],[6,1,4]]
sol = Solution()
print(sol.maximumDetonation(bombs))
