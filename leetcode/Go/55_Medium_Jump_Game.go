/*
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
*/
package main

import "fmt"

func canJump(nums []int) bool {
	// Let n be equal to the length of nums
	n := len(nums)
	// Create an array of length n to store boolean values, initially set to False
	// dp[i] is set True or False reflecting whether the end can be reached by dp[i]
	dp := make([]bool, n)
	// Set last value of dp array to True as we assume the last item can always reach the end.
	dp[n-1] = true

	// Set farthestReachable to the index of the last True item (n-1)
	farthestReachable := n - 1

	// Iterate over nums, starting from the second to last (n-2) value and ending at index 0
	for i := n - 2; i >= 0; i-- {
		// see if i + nums[i] (the amount of places you can jump) is >= the index of the last position where dp is True
		if i+nums[i] >= farthestReachable {
			// Set dp[i] to True because you can reach end from this position i
			dp[i] = true
			//  Set farthestReachable to i as it is now the closest position that can reach the end.
			farthestReachable = i
		}
	}
	// If after iterating, dp[0] is set to True, it means you can successfully traverse the jump game, so return dp[0] (true or false)
	return dp[0]

}

func main() {
	var nums = []int{2, 3, 1, 1, 4}
	fmt.Println(canJump(nums))
}
