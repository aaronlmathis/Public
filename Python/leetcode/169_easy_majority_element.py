class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
 
        if len(nums) == 1:
            return nums[0]

        n = len(nums) // 2
  
        seen = {}
        for c in nums:
            if c in seen:
                seen[c] += 1
                if seen[c] > n:
                    return c
            else:
                seen[c] = 1       
        
        count = {}
        res, maxCount = 0, 0
        for n in nums:
            count[n] = 1 + count.get(n,0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)

        return res
        """
        res, count = 0,0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res