class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map = {}
        res = []

        for num in nums1:
            if num in map:
                map[num]+=1
            else:
                map[num] = 1
    
        for num in nums2:
            if num in map:
                if map[num] > 0:
                    res.append(num)
                    map[num]-=1
    
        return res

"""
        # Create a frequency counter for nums1
        counts = Counter(nums1)
        result = []
        
        # Iterate over nums2 and check for intersection
        for num in nums2:
            if counts[num] > 0:  # If num is in nums1 and the count is positive
                result.append(num)
                counts[num] -= 1  # Decrease the count
        
        return result

"""


nums1 = [1,2,2,1,2]
nums2 = [2,2]
sol = Solution()
print(sol.intersect(nums1, nums2))