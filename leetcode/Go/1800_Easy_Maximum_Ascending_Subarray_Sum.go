/*
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.

Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

Example 2:
Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

Example 3:
Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
*/
package main

import "fmt"

func maxAscendingSum(nums []int) int {
	n := len(nums)

	rsum, msum := nums[0], nums[0]

	for i := 1; i < n; i++ {
		if nums[i] > nums[i-1] {
			rsum += nums[i]
		} else {
			rsum = nums[i]
		}
		if rsum > msum {
			msum = rsum
		}
	}
	return msum
}

func main() {
	nums := []int{12, 17, 15, 13, 10, 11, 12}
	fmt.Println(maxAscendingSum(nums))
}
