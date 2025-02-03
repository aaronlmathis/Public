/*
You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

Example 1:
Input: nums = [1,4,3,3,2]
Output: 2
Explanation:
The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].
The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].
Hence, we return 2.

Example 2:
Input: nums = [3,3,3,3]
Output: 1
Explanation:
The strictly increasing subarrays of nums are [3], [3], [3], and [3].
The strictly decreasing subarrays of nums are [3], [3], [3], and [3].
Hence, we return 1.

Example 3:
Input: nums = [3,2,1]
Output: 3
Explanation:
The strictly increasing subarrays of nums are [3], [2], and [1].
The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].
Hence, we return 3.

Constraints:
1 <= nums.length <= 50
1 <= nums[i] <= 50
*/
package main

import "fmt"

func longestMonotonicSubarray(nums []int) int {

	n := len(nums)

	ilen, dlen, mlen := 1, 1, 1

	var max = func(a int, b int) int {
		if a >= b {
			return a
		} else {
			return b
		}
	}
	for i := 1; i < n; i++ {
		if nums[i] > nums[i-1] {
			ilen++
			dlen = 1
		} else if nums[i] < nums[i-1] {
			dlen++
			ilen = 1
		} else {
			ilen, dlen = 1, 1
		}
		mlen = max(mlen, max(ilen, dlen))
	}

	return mlen
}

func main() {
	nums := []int{1, 4, 3, 3, 2}
	fmt.Println(longestMonotonicSubarray(nums))
}
