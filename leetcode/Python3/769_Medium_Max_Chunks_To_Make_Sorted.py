"""
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].
We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
Return the largest number of chunks we can make to sort the array.

Example 1:
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:
Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

A[:k+1] == [0, 1, 2, ...k];
 
"""
from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Keep track of the number of chunks that can be made
        chunks = 0
        # Keep track of the maximum value found so far in arr
        max_val = -1

        # Iterate through arr
        for i in range(len(arr)):
            # Find the maximum value in arr seen so far.
            v = arr[i]
            max_val = max(max_val, v)

            # If the maximum value is ever equal to the index, you know a chunk can be made. Increment chunks
            if max_val == i:
                chunks+=1

        # Return chunks
        return chunks


sol = Solution()
arr = [4,3,2,1,0]
print(sol.maxChunksToSorted(arr))        