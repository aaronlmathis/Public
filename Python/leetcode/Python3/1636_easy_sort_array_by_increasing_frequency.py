class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Sort by frequency in ascending order and by number in descending order for ties
        sorted_count = sorted(count.items(), key=lambda x: (x[1], -x[0]))
        
        # Build the result list using a list comprehension
        res = [num for num, freq in sorted_count for _ in range(freq)]
        
        return res
    
nums = [5,5,9,9,5,6]
sol = Solution()
print(sol.frequencySort(nums))

"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

Output: [3,1,1,2,2,2]
"""