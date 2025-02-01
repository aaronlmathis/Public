/*
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

Example 1:
Input: nums = [1]
Output: true
Explanation:
There is only one element. So the answer is true.

Example 2:
Input: nums = [2,1,4]
Output: true
Explanation:
There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

Example 3:
Input: nums = [4,3,1,6]
Output: false
Explanation:
nums[1] and nums[2] are both odd. So the answer is false.
*/

package main

import "fmt"

func isArraySpecial(nums []int) bool {
	n := len(nums)

	// Quick exit if nums has 1 item.
	if n == 1 {
		return true
	}
	// Iterate over nums, 2 at a time, checking to ensure both numbers have differing parity
	for index := 1; index < n; index++ {
		if nums[index]&1 == nums[index-1]&1 {
			return false
		}
	}
	return true
}
func main() {
	nums := []int{4, 3, 1, 6}
	fmt.Println(isArraySpecial(nums))
}
