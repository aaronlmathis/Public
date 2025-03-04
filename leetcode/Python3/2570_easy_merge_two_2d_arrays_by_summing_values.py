"""
You are given two 2D integer arrays nums1 and nums2.

nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays then its value in that array is considered to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.

Example 1:

Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]
Explanation: The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.
Example 2:

Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
Explanation: There are no common ids, so we just include each id with its value in the resulting list.
"""
from typing import List
from collections import defaultdict
from itertools import zip_longest
class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        # Build hashmap for id:val combos.
        val_map = defaultdict(int)
        # Use itertools.zip_longest to iterate over both lists (without stopping at end of shortest like zip())
        # If there is no value, it defaults to None. So we check if n1 or n2 is not None before adding to hashmap
        for n1, n2 in zip_longest(nums1, nums2, fillvalue=None):
            if n1 is not None:
                val_map[n1[0]]+=n1[1]
            if n2 is not None:
                val_map[n2[0]]+=n2[1]
            
        # Unlike other languages, Python v 3.7+ maintains insertion order in dictionaries. No need to sort.
        # We could write this out in full form:
        # for k, v in val_map.items():
        #   answer.append([k, v])
        # Or just return a list comprehension....
        return [[k, val_map[k]] for k in sorted(val_map.keys())]
            


sol = Solution()
nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
# [[1,6],[2,3],[3,2],[4,6]]

print(sol.mergeArrays(nums1, nums2))