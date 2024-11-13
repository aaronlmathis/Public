/*
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
A pair (i, j) is fair if:

	0 <= i < j < n, and
	lower <= nums[i] + nums[j] <= upper

Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).
*/
package main

import (
	"fmt"
	"sort"
)

func bisectLeft(nums []int, target int, start int) int {
	return sort.Search(len(nums)-start, func(i int) bool {
		return nums[start+i] >= target
	}) + start
}

func bisectRight(nums []int, target int, start int) int {
	return sort.Search(len(nums)-start, func(i int) bool {
		return nums[start+i] > target
	}) + start
}

func countFairPairs(nums []int, lower int, upper int) int {
	sort.Ints(nums) // sort nums in asc
	count := 0
	for left := 0; left < len(nums); left++ {
		minRequired := lower - nums[left]
		maxRequired := upper - nums[left]
		rightMin := bisectLeft(nums, minRequired, left+1)
		rightMax := bisectRight(nums, maxRequired, left+1)
		count += rightMax - rightMin
	}
	fmt.Println(nums)
	return count
}
func main() {
	nums := []int{0, 1, 7, 4, 4, 5}
	lower, upper := 3, 6
	fmt.Println(countFairPairs(nums, lower, upper))
}
