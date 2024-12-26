/*
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1
*/

package main

import "fmt"

func findTargetSumWays(nums []int, target int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}

	if target > sum || target < -sum {
		return 0
	}

	n := len(nums)
	sumRange := 2*sum + 1

	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, sumRange)
	}

	offset := sum
	dp[0][offset] = 1

	for i := 1; i <= n; i++ {
		for j := 0; j < sumRange; j++ {
			// Add the current number
			if j-nums[i-1] >= 0 {
				dp[i][j] += dp[i-1][j-nums[i-1]]
			}
			// Subtract the current number
			if j+nums[i-1] < sumRange {
				dp[i][j] += dp[i-1][j+nums[i-1]]
			}
		}
	}
	return dp[n][target+offset]
}

func main() {
	nums := []int{1, 1, 1, 1, 1}
	target := 3
	fmt.Println(findTargetSumWays(nums, target))
}
