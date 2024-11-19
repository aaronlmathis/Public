/*
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
*/
package main

import "fmt"

func maximumSubarraySum(nums []int, k int) int64 {
	// Set integer n to length of nums
	var n int = len(nums)

	// Early exit if k is > array length
	if k > n {
		return int64(0)
	}

	// Initialize variable to hold answer
	var answer int

	// int subTotal to track subarray total
	var subTotal int

	// map with empty struct values to efficiently track digit frequency
	seen := make(map[int]struct{})

	// start pointer to indicate start of window
	var start int

	// Iterate through nums, dynamically resizing window and calculating totals
	for end := 0; end < n; end++ {
		// Handle duplicates by shrinking window from left until duplicate is gone.
		// While shrinking, reduce total by each number and remove number from seen map
		for _, exists := seen[nums[end]]; exists; _, exists = seen[nums[end]] {
			subTotal -= nums[start]
			delete(seen, nums[start])
			start++
		}
		// If not a duplicate anymore, add it to seen map and increase total
		subTotal += nums[end]
		seen[nums[end]] = struct{}{}

		// If window size is larger than k, shrink it from left
		// Remove each number from total and map while shrinking.
		if end-start+1 > k {
			subTotal -= nums[start]
			delete(seen, nums[start])
			start += 1
		}

		// If window is of size k, its a valid subarray.
		// Check if total is > answer, if so, set answer to total
		if end-start+1 == k {
			if subTotal > answer {
				answer = subTotal
			}
		}
	}

	// Return the max total sum of a subarray of length k with no duplicates
	return int64(answer)
}

func main() {
	var nums = []int{1, 5, 4, 2, 9, 9, 9}
	var k int = 3
	fmt.Println(maximumSubarraySum(nums, k))
}
