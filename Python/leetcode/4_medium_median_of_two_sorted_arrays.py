class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) % 2 == 0:
            m1 = (len(nums3) // 2 -1)
            m2 = (len(nums3)// 2)
            median = (nums3[m2] + nums3[m1]) / 2.0
            return median      

        else:
            median = len(nums3) // 2
            return nums3[median]     

sol = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(sol.findMedianSortedArrays(nums1, nums2))