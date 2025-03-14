/*
You are given a 0-indexed integer array nums.
The distinct count of a subarray of nums is defined as:
Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.

Example 2:
Input: nums = [1,1]
Output: 3
Explanation: Three possible subarrays are:
[1]: 1 distinct value
[1]: 1 distinct value
[1,1]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
*/
package main

import "fmt"

func sumCounts(nums []int) int {

	// Calculate length of the nums list
	var arrayLength int = len(nums)

	// Initialize a variable to track the sum of the squares of all distinct counts of subarrays
	var squareCountSums int

	// Iterate over each possible starting point of subarrays
	for start := 0; start < arrayLength; start++ {
		// Use a map[int]struct to keep track of unique elements in the current subarray
		uniqueElements := map[int]struct{}{}

		// For each starting point, extend the subarray by moving the `end` pointer
		for end := start; end < arrayLength; end++ {
			// Add the current element to the set of unique elements
			uniqueElements[nums[end]] = struct{}{}

			// Calculate the distinct count by measuring the size of the unique elements set
			var distinctCount int = len(uniqueElements)

			// Square the distinct count and add it to the total sum
			squareCountSums += distinctCount * distinctCount
		}
	}

	// Return the accumulated sum of squares of distinct counts for all subarrays
	return squareCountSums
}

func main() {
	nums := []int{1, 2, 1}
	fmt.Println(sumCounts(nums))
}
