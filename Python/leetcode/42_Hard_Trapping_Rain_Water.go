/*
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
*/
package main

import "fmt"

func trap(height []int) int {
	n := len(height)
	if n == 0 {
		return 0
	}

	max := func(val1 int, val2 int) int {
		if val1 > val2 {
			return val1
		} else {
			return val2
		}
	}

	min := func(val1 int, val2 int) int {
		if val1 < val2 {
			return val1
		} else {
			return val2
		}
	}
	// Create slices to store the largest values to the left and right
	maxLeft := make([]int, n)
	maxRight := make([]int, n)

	// Fill left array
	maxLeft[0] = height[0]
	for i := 1; i < n; i++ {
		maxLeft[i] = max(maxLeft[i-1], height[i])
	}
	// Fill Right Array
	maxRight[n-1] = height[n-1]
	for i := n - 2; i >= 0; i-- {
		maxRight[i] = max(maxRight[i+1], height[i])
	}
	minMaxBoundary := 0
	water := 0
	result := 0
	for i := 0; i < n; i++ {
		// Take the minimum maximum of the heights at the left and right boundaries.
		minMaxBoundary = min(maxLeft[i], maxRight[i])

		// Calculate how much water this position will hold.
		// water = min(L, R) - h[i]
		water = minMaxBoundary - height[i]

		// If water is positive (can't have negative water) add it to result.
		if water > 0 {
			result += water
		}
	}

	return result
}

func main() {
	height := []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	fmt.Println(trap(height))
}
