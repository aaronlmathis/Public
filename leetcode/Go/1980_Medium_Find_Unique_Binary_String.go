/*
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

Constraints:
n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
*/
package main

import "fmt"

func findDifferentBinaryString(nums []string) string {
	// Initialize your stack with an empty string.
	stack := []string{""}

	// For efficient lookups against `nums`, make a map[string]struct to reference binary strings in nums.
	lookup := make(map[string]struct{}, len(nums))
	for _, str := range nums {
		lookup[str] = struct{}{}
	}

	// Helper function to see if a string exists in `lookup` map
	contains := func(target string) bool {
		_, exists := lookup[target]
		return exists
	}

	n := len(nums[0])

	// Process the stack, adding 0s or 1s until a solution is found.
	for len(stack) > 0 {
		state := stack[0]
		stack = stack[1:]
		if len(state) == n {
			if !contains(state) {
				return state
			} else {
				continue
			}
		}

		stack = append(stack, state+"1")
		stack = append(stack, state+"0")
	}
	return ""
}

func main() {
	nums := []string{"111", "011", "001"}
	fmt.Println(findDifferentBinaryString(nums))
}
