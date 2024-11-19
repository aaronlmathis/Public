/*
The bitwise AND of an array nums is the bitwise AND of all integers in nums.
For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
Also, for nums = [7], the bitwise AND is 7.
You are given an array of positive integers candidates.
Evaluate the bitwise AND of every combination of numbers of candidates.
Each number in candidates may only be used once in each combination.
Return the size of the largest combination of candidates with a bitwise AND greater than 0.

Example 1:
Input: candidates = [16,17,71,62,12,24,14]
Output: 4
Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
The size of the combination is 4.
It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
Note that more than one combination may have the largest size.
For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.

Example 2:
Input: candidates = [8,8]
Output: 2
Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
The size of the combination is 2, so we return 2.
*/
package main

import "fmt"

// Helper function to return max int in an array
func maxCount(positionCount [24]int) int {
	var maxCount int = positionCount[0]
	for i := 1; i < 24; i++ {
		if positionCount[i] > maxCount {
			maxCount = positionCount[i]
		}
	}
	return maxCount
}

func largestCombination(candidates []int) int {
	// Determine the maximum number of bits required based on the largest candidate
	maxBits := 0
	for _, candidate := range candidates {
		bits := 0
		temp := candidate
		for temp > 0 {
			temp >>= 1
			bits++
		}
		if bits > maxBits {
			maxBits = bits
		}
	}

	// Initialize position count for only the required bits
	positionCount := make([]int, maxBits)

	// Count occurrences of '1's in each bit position
	for _, candidate := range candidates {
		for idx := 0; idx < maxBits; idx++ {
			if candidate&(1<<idx) != 0 {
				positionCount[idx]++
			}
		}
	}

	// Find the maximum count in the relevant bit positions
	maxCount := 0
	for _, count := range positionCount {
		if count > maxCount {
			maxCount = count
		}
	}

	return maxCount
}

func main() {
	var candidates = []int{16, 17, 71, 62, 12, 24, 14}
	fmt.Println(largestCombination(candidates))
}
