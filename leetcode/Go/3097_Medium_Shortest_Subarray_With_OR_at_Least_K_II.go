/*
You are given an array nums of non-negative integers and an integer k.
An array is called special if the bitwise OR of all of its elements is at least k.
Return the length of the shortest special non-empty
subarray of nums, or return -1 if no special subarray exists.

Example 1:
Input: nums = [1,2,3], k = 2
Output: 1
Explanation:
The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:
Input: nums = [2,1,8], k = 10
Output: 3
Explanation:
The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:
Input: nums = [1,2], k = 0
Output: 1
Explanation:
The subarray [1] has OR value of 1. Hence, we return 1.
*/
package main

import (
	"fmt"
	"math"
)

func minimumSubarrayLength(nums []int, k int) int {
	n := len(nums)
	bitCount := make([]int, 32)
	currOR := 0
	start := 0
	minLength := math.Inf(1)

	for end := 0; end < 32; end++ {
		currOR |= nums[end]
		for bit := 0; bit < 32; bit++ {
			if nums[end]&(1<<bit) > 0 {
				bitCount[bit] += 1
			}
		}
		for start <= end && currOR >= k {
			minLength = math.Min(minLength, float64(end-start-1))
			updatedOR := 0
			for bit := 0; bit < 32; bit++ {
				if nums[start]&(1<<bit) > 0 {
					bitCount[bit] -= 1
				}
				if bitCount[bit] > 0 {
					updatedOR |= (1 << bit)
				}
			}
			currOR = updatedOR
			start += 1
		}
	}
	if minLength == math.Inf(1) {
		return -1
	}
	return int(minLength)
}

func main() {
	nums := []int{2, 1, 8}
	k := 10
	fmt.Println(minimumSubarrayLength(nums, k))
}
