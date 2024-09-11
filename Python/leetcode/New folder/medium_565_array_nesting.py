class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        size = len(nums)
        visited = [False for c in range(size)]
        max_length = 0
        for i in range(len(nums)):
            if visited[i]:
                continue
            else:
                length = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = nums[j]
                    length+=1
                    if length > max_length:
                        max_length = length
abs(2-2)
        return max_length

nums = [5,4,0,3,1,6,2]
sol = Solution()
print(sol.arrayNesting(nums))

"""

Initialize a boolean visited list of size n, where visited[i] indicates if nums[i] has been visited or not.
Initialize a variable max_length to zero, which will be used to store the maximum length of any set.
Iterate over all elements of nums using a for loop with loop variable i:
Check if nums[i] has already been visited, by checking if visited[i] is True. If it has been visited, skip to the next iteration of the loop.
If nums[i] has not been visited, initialize a variable length to zero.
Set a variable j to i, which is the starting index of the current set.
Enter a while loop that runs until nums[j] has already been visited:
Mark nums[j] as visited by setting visited[j] to True.
Set j to nums[j], which is the index of the next element in the current set.
Increment length by one.
If the length of the current set is greater than max_length, update max_length to the length of the current set.
Return max_length.


You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

The first element in s[k] starts with the selection of the element nums[k] of index = k.
The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
We stop adding right before a duplicate element occurs in s[k].
Return the longest length of a set s[k].
"""