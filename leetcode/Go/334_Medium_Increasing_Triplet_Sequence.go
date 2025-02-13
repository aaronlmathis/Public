/*
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
*/
package main

import (
	"fmt"
	"math"
)

func increasingTriplet(nums []int) bool {
	// Set fm and sm be set to the input constraint 2^32
	fm, sm := int(math.Pow(2, 32)), int(math.Pow(2, 32))
	// Iterate through nums, tracking first smallest, and second smallest.
	// Return true if num is > second smallest > first smallest.
	for _, num := range nums {
		if num < fm {
			fm = num
		} else if num < sm && num > fm {
			sm = num
		} else if num > sm {
			return true
		}
	}
	return false
}
func main() {
	nums := []int{1, 1, -2, 6}
	fmt.Println(increasingTriplet(nums))
}
