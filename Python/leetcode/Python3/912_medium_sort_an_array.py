from typing import List

class Solution:
    def heapify(self, nums: List[int], n: int, i: int) -> None:
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # left child
        right = 2 * i + 2  # right child

        # See if left child exists and is greater than root
        if left < n and nums[i] < nums[left]:
            largest = left

        # See if right child exists and is greater than the largest so far
        if right < n and nums[largest] < nums[right]:
            largest = right

        # Change root if needed
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]  # swap
            # Heapify the root
            self.heapify(nums, n, largest)

    def heap_sort(self, nums: List[int]) -> None:
        n = len(nums)

        # Build a maxheap.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]  # swap
            self.heapify(nums, i, 0)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.heap_sort(nums)
        return nums
    
sol = Solution()
nums = [5,2,3,1]
print(sol.sortArray(nums))

nums = [5,1,1,2,0,0]
print(sol.sortArray(nums))
"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""        