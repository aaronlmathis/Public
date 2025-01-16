"""
You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3.

 

Example 1:

Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
Output: 13
Explanation:
A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
The bitwise XOR of all these numbers is 13, so we return 13.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 0
Explanation:
All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^ nums2[1], nums1[1] ^ nums2[0],
and nums1[1] ^ nums2[1].
Thus, one possible nums3 array is [2,5,1,6].
2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.
 

Constraints:

1 <= nums1.length, nums2.length <= 105
0 <= nums1[i], nums2[j] <= 109
"""
from typing import List
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Brute Force attempt
        
        total = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                xor = nums1[i] ^ nums2[j]
                total ^= xor
        return total
        """

        """
        Helper function to return the XOR of a list... item1 ^ item2 ^ item3.....
        """
        def get_xor(nums: List[int])->int:
            xor = 0
            for num in nums:
                xor ^= num
            return xor
        
        # Let n1 and n2 be the XOR sum of nums1 and nums2
        n1, n2 = get_xor(nums1), get_xor(nums2)
        print(n2)
        # Let m, n be the length of nums1, nums2
        m, n = len(nums1), len(nums2)

        # Keeping with the principal of XOR that:
        #    n ^ n = 0
        #    n ^ 0 = n
        # We can surmise that if m is even, then n2 should be 0. If n is even, n1 should be 0
        n1 = 0 if not n&1 else n1
        n2 = 0 if not m&1 else n2

        return n1 ^ n2

nums1 = [2, 1, 3]
nums2 = [10,2,5,0]

sol = Solution()
print(sol.xorAllNums(nums1, nums2))