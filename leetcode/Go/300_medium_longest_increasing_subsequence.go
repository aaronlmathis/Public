/*
Given an integer array nums, return the length of the longest strictly increasing
subsequence

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
*/

package main

import "fmt"

func lengthOfLIS(nums []int) int {
	subs := []int{nums[0]}
	binary_search := func(val int) int {
		left, right := 0, len(subs)-1
		for left < right {
			mid := (left + right) / 2
			if subs[mid] < val {
				left = mid + 1
			} else {
				right = mid
			}
		}
		return left
	}

	for i := 1; i < len(nums); i++ {
		if nums[i] > subs[len(subs)-1] {
			subs = append(subs, nums[i])
		} else {
			pos := binary_search(nums[i])
			subs[pos] = nums[i]
		}
	}

	return len(subs)

}

func main() {
	var nums = []int{3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12}
	fmt.Println(lengthOfLIS(nums))
}
