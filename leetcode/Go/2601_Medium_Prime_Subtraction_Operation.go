/*
You are given a 0-indexed integer array nums of length n.
You can perform the following operation as many times as you want:

	Pick an index i that you haven’t picked before, and pick a prime p strictly less than nums[i], then subtract p from nums[i].

Return true if you can make nums a strictly increasing array using the above operation and false otherwise.
A strictly increasing array is an array whose each element is strictly greater than its preceding element.

Example 1:
Input: nums = [4,9,6,10]
Output: true
Explanation: In the first operation: Pick i = 0 and p = 3, and then subtract 3 from nums[0], so that nums becomes [1,9,6,10].
In the second operation: i = 1, p = 7, subtract 7 from nums[1], so nums becomes equal to [1,2,6,10].
After the second operation, nums is sorted in strictly increasing order, so the answer is true.

Example 2:
Input: nums = [6,8,11,12]
Output: true
Explanation: Initially nums is sorted in strictly increasing order, so we don't need to make any operations.

Example 3:
Input: nums = [5,8,3]
Output: false
Explanation: It can be proven that there is no way to perform operations to make nums sorted in strictly increasing order, so the answer is false.
*/
package main

import (
	"fmt"
	"math"
)

func maxInt(nums []int) int {
	if len(nums) == 0 {
		panic("Slice is Empty")
	}

	max := nums[0]
	for _, num := range nums[1:] {
		if num > max {
			max = num
		}
	}
	return max
}
func primeSubOperation(nums []int) bool {
	limit := maxInt(nums)

	sieve := make([]bool, limit+1)
	for i := 0; i < len(sieve); i++ {
		sieve[i] = true
	}

	sieve[0], sieve[1] = false, false

	for start := 2; start < int(math.Sqrt(float64(limit+1)))+1; start++ {
		if sieve[start] == true {
			for multiple := start * start; multiple < limit+1; multiple += start {
				sieve[multiple] = false
			}
		}
	}

	currValue := 1
	i := 0
	for i < len(nums) {
		difference := nums[i] - currValue

		if difference < 0 {
			return false
		}

		if sieve[difference] == true || difference == 0 {
			i += 1
			currValue += 1
		} else {
			currValue += 1
		}
	}

	return true
}
func main() {
	nums := []int{4, 9, 6, 10}
	fmt.Println(primeSubOperation(nums))
}
