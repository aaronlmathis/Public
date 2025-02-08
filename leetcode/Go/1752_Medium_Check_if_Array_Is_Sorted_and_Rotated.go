/*
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

Example 1:
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].

Example 2:
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.

Example 3:
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
*/
package main

import "fmt"

func check(nums []int) bool {
	n := len(nums)
	nums = append(nums, nums...)
	nn := len(nums)

	asc_count := 0

	for i := 0; i < nn-1; i++ {
		if nums[i+1] > nums[i] {
			asc_count++
		} else {
			asc_count = 1
		}
		if asc_count == n {
			return true
		}
	}
	return false
}

func main() {
	nums := []int{3, 4, 5, 1, 2}
	fmt.Println(check(nums))
	nums = []int{2, 1, 3, 4}
	fmt.Println(check(nums))
}
