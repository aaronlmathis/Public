package main

import "fmt"

// sumCounts calculates the sum of the squares of distinct counts of all subarrays.
func sumCounts(nums []int) int {
	n := len(nums)
	totalSum := 0

	// Iterate over each possible starting index of subarrays
	for i := 0; i < n; i++ {
		// Use a map to track the frequency of elements in the current subarray
		freqMap := make(map[int]int)
		distinctCount := 0

		// Extend the subarray to include elements up to the end of the array
		for j := i; j < n; j++ {
			// If the element is new to the subarray, increase the distinct count
			if freqMap[nums[j]] == 0 {
				distinctCount++
			}
			// Update the frequency map
			freqMap[nums[j]]++

			// Add the square of the distinct count to the total sum
			totalSum += distinctCount * distinctCount
		}
	}

	return totalSum
}

func main() {
	// Example usage
	nums := []int{1, 2, 1}
	result := sumCounts(nums)
	fmt.Println("Result:", result) // Output: 15
}
