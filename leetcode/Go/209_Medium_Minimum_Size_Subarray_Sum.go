/*
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
*/
package main

import "fmt"

func minSubArrayLen(target int, nums []int) int {
	// Initialize:
	//   n as length of nums
	//   start as left boundary of window (zero)
	//   subTotal sum of subarray as zero
	//   minLength as n + 1 (at end, if minLength > n, we know that zero should be returned because list items don't total target)
	var n int = len(nums)
	var start int
	var subTotal int
	var minLength int = n + 1

	// Iterate through nums dynamically, using sliding window
	for end := 0; end < n; end++ {
		// Calculate sum total of subarray by adding nums[end] to subTotal
		subTotal += nums[end]
		// While subTotal >= target number, calculate length of subarray
		// set minLength to length if length < minLength
		// Shrink window by increasing start after reducing subTotal by nums[start]
		for subTotal >= target {
			if end-start+1 < minLength {
				minLength = end - start + 1
			}
			subTotal -= nums[start]
			start += 1
		}
	}

	// Return 0 if minLength > n (meaning we never found a subarray whose sum > target)
	// Otherwise return minLength
	if minLength > n {
		return 0
	}
	return minLength
}

func main() {
	var nums = []int{1, 2, 3, 4, 5}
	var target int = 15
	fmt.Println(minSubArrayLen(target, nums))
}
