/*
You are given a sorted array nums of n non-negative integers and an integer maximumBit. You want to perform the following query n times:
Find a non-negative integer k < 2maximumBit such that nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
Remove the last element from the current array nums.
Return an array answer, where answer[i] is the answer to the ith query.

Example 1:
Input: nums = [0,1,1,3], maximumBit = 2
Output: [0,3,2,3]
Explanation: The queries are answered as follows:
1st query: nums = [0,1,1,3], k = 0 since 0 XOR 1 XOR 1 XOR 3 XOR 0 = 3.
2nd query: nums = [0,1,1], k = 3 since 0 XOR 1 XOR 1 XOR 3 = 3.
3rd query: nums = [0,1], k = 2 since 0 XOR 1 XOR 2 = 3.
4th query: nums = [0], k = 3 since 0 XOR 3 = 3.

Example 2:
Input: nums = [2,3,4,7], maximumBit = 3
Output: [5,2,6,5]
Explanation: The queries are answered as follows:
1st query: nums = [2,3,4,7], k = 5 since 2 XOR 3 XOR 4 XOR 7 XOR 5 = 7.
2nd query: nums = [2,3,4], k = 2 since 2 XOR 3 XOR 4 XOR 2 = 7.
3rd query: nums = [2,3], k = 6 since 2 XOR 3 XOR 6 = 7.
4th query: nums = [2], k = 5 since 2 XOR 5 = 7.

Example 3:
Input: nums = [0,1,2,2,5,7], maximumBit = 3
Output: [4,3,6,4,6,7]
*/
package main

import "fmt"

func getMaximumXor(nums []int, maximumBit int) []int {
	// Helper function to take an integer, flip the bits up to MaximumBit, and return integer
	flipBits := func(num int) int {
		//Create mask based on maxium bits
		var mask int = ((1 << maximumBit) - 1)
		return mask ^ num
	}

	// We will need to perform this operation 'n' times which is equal to length of nums.
	n := len(nums)

	// Declare an answer int slice to return the answer
	answer := make([]int, n)

	// Calculate the xorTotal of nums once
	xorTotal := nums[0]
	for i := 1; i < n; i++ {
		xorTotal ^= nums[i]
	}
	//A ppend that total to the answer
	answer[0] = flipBits(xorTotal)

	// Iterate through list, calculating the new xorTotal after removing last number of nums
	// To do this, we xor the xorTotal by the last number of the previous iteration (to cancel that operation out)
	for i := n - 1; i > 0; i-- {
		xorTotal ^= nums[i]
		answer[n-i] = flipBits(xorTotal)
	}

	return answer
}

func main() {
	var nums = []int{0, 1, 2, 2, 5, 7}
	var maximumBit int = 3
	fmt.Println(getMaximumXor(nums, maximumBit))
}