"""
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

Example 1:
Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW".
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.

Example 2:
Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.

Constraints:

n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n
"""
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # w_count initially starts at 0
        w_count = 0
 
        # Count the white blocks in the initial window of size `k`
        for i in range(0, k):
            if blocks[i] == 'W':
                w_count+=1

        # If  the initial `wCount` was zero, then 0 operations are needed
        if w_count == 0: return 0

        # Set min_ops to the current w_count as it is the minimum operations we know will work.
        min_ops = w_count

        # `left` is the left side of the window, `right` is the right.
	    # Advance the window across `blocks`, updating `wCount` and noting `min_ops`
        # The window is blocks[left:right+1]
        left = 0
        for right in range(k, len(blocks)):
            print(right)
            # If the left-most boundary of the former window was white, reduce the w_count as we shrink the window.
            if blocks[left] == 'W':
                w_count-=1
            # Shrink the window
            left+=1
            print(blocks[left:right+1])
            # See if the block added to the right was white
            if blocks[right] == 'W':
                w_count+=1
            
            # Return zero if w_count is zero (window is all black, no operations required)
            if w_count == 0: return 0

            # Update `min_ops` if `w_count` is the smallest seen from any window so far
            min_ops = min(min_ops, w_count)
        
        # Return `min_ops` as the answer
        return min_ops
    
sol = Solution()
blocks = "WBBWWBBWBW"
k = 7
print(sol.minimumRecolors(blocks, k))