"""
Kadane's Algorithm - Find the maximum subarray sum in an array in O(n) time and O(1) Space.


The idea of Kadane’s algorithm is to traverse over the array from left to right and for each element, find the maximum sum among all subarrays ending at that element. The result will be the maximum of all these values. 


But, the main issue is how to calculate maximum sum among all the subarrays ending at an element in O(1) time?


To calculate the maximum sum of subarray ending at current element, say maxEnding, we can use the maximum sum ending at the previous element. So for any element, we have two choices:


Choice 1: Extend the maximum sum subarray ending at the previous element by adding the current element to it. If the maximum subarray sum ending at the previous index is positive, then it is always better to extend the subarray.
Choice 2: Start a new subarray starting from the current element. If the maximum subarray sum ending at the previous index is negative, it is always better to start a new subarray from the current element.
This means that maxEnding at index i = max(maxEnding at index (i – 1) + arr[i], arr[i]) and the maximum value of maxEnding at any index will be our answer. 

"""
arr = [2, 4, 5, -2, 4, 6]
n = len(arr)
max_sum = [0] * n
for i in range(n):
    prev = max_sum[i-1] if i > 0 else 0
    max_sum[i] = max(arr[i]+prev, arr[i])
print(max_sum)
