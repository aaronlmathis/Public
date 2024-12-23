"""
You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.

 

Example 1:


Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
Output: 3
Explanation:
- Swap 4 and 3. The 2nd level becomes [3,4].
- Swap 7 and 5. The 3rd level becomes [5,6,8,7].
- Swap 8 and 7. The 3rd level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
Example 2:


Input: root = [1,3,2,7,6,5,4]
Output: 3
Explanation:
- Swap 3 and 2. The 2nd level becomes [2,3].
- Swap 7 and 4. The 3rd level becomes [4,6,5,7].
- Swap 6 and 5. The 3rd level becomes [4,5,6,7].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
Example 3:


Input: root = [1,2,3,4,5,6]
Output: 0
Explanation: Each level is already sorted in increasing order so return 0.

"""
from collections import deque, defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_binary_tree(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    
    idx = 0
    n = len(nodes)
    if nodes[0] is None:
        return None
    
    head = TreeNode(nodes[idx])
    idx += 1
    queue = deque([head])

    while queue and idx < n:
        curr_node = queue.popleft()

        # Add left child
        if idx < n and nodes[idx] is not None:
            curr_node.left = TreeNode(nodes[idx])
            queue.append(curr_node.left)
        idx += 1

        # Add right child
        if idx < n and nodes[idx] is not None:
            curr_node.right = TreeNode(nodes[idx])
            queue.append(curr_node.right)
        idx += 1

    return head

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        level_vals = defaultdict(list)

        queue = deque([(0, root)])

        while queue:
            curr_level, curr_node = queue.popleft()
            level_vals[curr_level].append(curr_node.val)
            if curr_node.left:
                queue.append((curr_level+1, curr_node.left))
            if curr_node.right:
                queue.append((curr_level+1, curr_node.right))
        
        operations = 0
        for level, values in level_vals.items():
            n = len(values)
            if n < 2:
                continue
            visited = [False] * n
            svals = [(value, index) for index, value in enumerate(values)]
            svals = sorted(svals)

            for i in range(n):
                # Skip if already visited or already in the correct position
                if visited[i] or svals[i][1] == i:
                    continue
                # Start traversing the cycle
                cycle_size = 0
                x = i
                while not visited[x]:
                    visited[x] = True
                    next_index = svals[x][1]  # Get the original index of the sorted value
                    x = next_index
                    cycle_size += 1
                
                # Add operations for this cycle
                if cycle_size > 1:
                    operations += cycle_size - 1

        return operations
    
sol = Solution()
nodes = [1,4,3,7,6,8,5,None,None,None,None,9,None,10]
nodes = [1,3,2,7,6,5,4]
#nodes = [1,2,3,4,5,6]
#nodes = [11,3,43,27,29,None,17,None,None,18]
root = create_binary_tree(nodes)
print(sol.minimumOperations(root))