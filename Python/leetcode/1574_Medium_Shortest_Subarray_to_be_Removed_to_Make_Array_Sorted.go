/*
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.
Return the length of the shortest subarray to remove.
A subarray is a contiguous subsequence of the array.

Example 1:
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

Example 2:
Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example 3:
Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
*/

package main

import "fmt"

func findLengthOfShortestSubarray(arr []int) int {
	// Helper function to return the minimum of two integers
	min := func(value1 int, value2 int) int {
		if value1 > value2 {
			return value2
		} else {
			return value1
		}
	}

	// Initialize n as length of arr
	n := len(arr)

	// Initialize left and right pointers at the beginning and end of the array
	left, right := 0, n-1

	// Increase left pointer while next number is greater than or equal to
	for left < n-1 && arr[left] <= arr[left+1] {
		left++
	}

	// If the entire array is sorted, return 0
	if left == n-1 {
		return 0
	}
	// Decrease right pointer while next number is less than or equal to
	for right > 0 && arr[right] >= arr[right-1] {
		right--
	}

	// Calculate the minimum array length between removing all but prefix, or all but suffix
	minToRemove := min(n-left-1, right)

	// Iterate from 0 to end of prefix (including end)
	newRight := right
	for newLeft := 0; newLeft <= left; newLeft++ {
		// While beginning of suffix is < arr[newleft], increase newRight pointer
		for newRight < n && arr[newRight] < arr[newLeft] {
			newRight += 1
		}
		// Calculate minimum between previous minToRemove and newRight - newLeft - 1
		minToRemove = min(minToRemove, newRight-newLeft-1)
	}

	// Return the answer
	return minToRemove
}

func main() {
	arrs := [][]int{{1},
		{2, 2, 2, 1, 1, 1},
		{1, 2, 3, 10, 0, 7, 8, 9},
		{1, 2, 3, 10, 0, 2, 7, 8, 9},
		{16, 10, 0, 3, 22, 1, 14, 7, 1, 12, 15},
		{13, 0, 14, 7, 18, 18, 18, 16, 8, 15, 20}}
	for _, arr := range arrs {
		fmt.Println(findLengthOfShortestSubarray(arr))
	}
}
