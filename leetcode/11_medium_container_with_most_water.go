package main

import (
	"fmt"
)

func min(value1 int, value2 int) int {
	if value1 > value2 {
		return value2
	} else {
		return value1
	}
}

func max(value1 int, value2 int) int {
	if value1 > value2 {
		return value1
	} else {
		return value2
	}
}

func maxArea(height []int) int {
	// Use a 2-pointer approach to track left and right boundary
	var left, right int = 0, len(height) - 1

	// Track the maximum volume seen
	var maxArea int

	// Iterate while left boundary is still left or at right boundary.
	for left <= right {
		// The width of the water container is the right boundary minus the left
		var width int = right - left

		// Calculate the min height between left and right, to see maximum height of container
		var maxHeight int = min(height[left], height[right])

		// Calculate the volume as width * maxHeight
		var area int = width * maxHeight

		// Track the max volume seen
		maxArea = max(area, maxArea)

		// Move the pointer that is smaller, if left then move right, if right then move left.
		if height[left] > height[right] {
			right -= 1
		} else {
			left += 1
		}
	}
	// return maxvolume
	return maxArea
}

func main() {
	var height = []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	fmt.Println(maxArea(height))
}
