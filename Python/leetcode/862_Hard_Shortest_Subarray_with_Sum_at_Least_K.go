/*
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1], k = 1
Output: 1

Example 2:
Input: nums = [1,2], k = 4
Output: -1

Example 3:
Input: nums = [2,-1,2], k = 3
Output: 3
*/
package main

import (
	"container/list"
	"fmt"
)

func shortestSubarray(nums []int, k int) int {
	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	n := len(nums)

	// Edge Case: Single item >= k
	if n == 1 && nums[0] >= k {
		return 1
	}

	result := n + 1 // Use n + 1 to represent "infinity" for integers

	// Calculate prefix sums
	prefixSums := make([]int, n+1) // Include a 0 at the start for easier calculations
	for i := 0; i < n; i++ {
		prefixSums[i+1] = prefixSums[i] + nums[i]
	}

	// Edge case: Any single prefix sum >= k
	for idx, sum := range prefixSums {
		if sum >= k {
			result = min(result, idx)
		}
	}

	queue := list.New()

	// Process prefix sums
	for i := 0; i <= n; i++ {
		// Maintain condition: prefixSums[i] - prefixSums[queue.Front()] >= k
		for queue.Len() > 0 && prefixSums[i]-prefixSums[queue.Front().Value.(int)] >= k {
			result = min(result, i-queue.Remove(queue.Front()).(int))
		}

		// Maintain monotonicity of the deque
		for queue.Len() > 0 && prefixSums[i] <= prefixSums[queue.Back().Value.(int)] {
			queue.Remove(queue.Back())
		}

		// Push current index to the deque
		queue.PushBack(i)
	}

	// If result wasn't updated, no valid subarray exists
	if result == n+1 {
		return -1
	}
	return result
}

func main() {
	nums := [][]int{
		{1},
		{1, 2},
		{2, -1, 2},
	}
	k := []int{1, 4, 3}
	for i := 0; i < len(nums); i++ {
		fmt.Println(shortestSubarray(nums[i], k[i]))
	}
}
