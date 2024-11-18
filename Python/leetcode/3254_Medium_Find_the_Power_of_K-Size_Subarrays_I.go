/*
You are given an array of integers nums of length n and a positive integer k.
The power of an array is defined as:
    Its maximum element if all of its elements are consecutive and sorted in ascending order.
    -1 otherwise.
You need to find the power of all subarrays of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

Example 1:
Input: nums = [1,2,3,4,3,2,5], k = 3
Output: [3,4,-1,-1,-1]
Explanation:
There are 5 subarrays of nums of size 3:
[1, 2, 3] with the maximum element 3.
[2, 3, 4] with the maximum element 4.
[3, 4, 3] whose elements are not consecutive.
[4, 3, 2] whose elements are not sorted.
[3, 2, 5] whose elements are not consecutive.

Example 2:
Input: nums = [2,2,2,2,2], k = 4
Output: [-1,-1]
Example 3:
Input: nums = [3,2,3,2,3,2], k = 2
Output: [-1,3,-1,3,-1]
*/

package main

import "fmt"

func resultsArray(nums []int, k int) []int {
	var n int = len(nums)           // Initialize N as length of nums
	left := 0                       // Initialize left as a pointer marking left boundary of sliding window
	ans := make([]int, (n - k + 1)) // Initialize a slice of size (n-k-1) filled with -1
	var consecutiveASC bool
	for right := k - 1; right < n; right++ { // Iterate through nums, with right being end of sliding window
		consecutiveASC = true                 //Assume the window's items are consecutive and ascending unless otherwise found
		for i := left + 1; i < right+1; i++ { // Iterate through window's items, 2 at a time to check if consecutive and Ascending
			if nums[i]-nums[i-1] != 1 { // Check that the previous item subtracted from the current item is '1'
				consecutiveASC = false //If not, assume window's items are not consecutive and asc
			}
		}
		// set ans[left] to nums[right] (end of subarray, assumed max) if consecutive. Else -1
		if consecutiveASC == true {
			ans[left] = nums[right]
		} else {
			ans[left] = -1
		}

		left++ // Advance left side of sliding window w/right.
	}

	return ans
}

func main() {
	nums := []int{1, 2, 3, 4, 3, 2, 5}
	k := 3
	fmt.Println(resultsArray(nums, k))
}
