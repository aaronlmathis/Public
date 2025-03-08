/*
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

Example 1:
Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW".
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.

Example 2:
Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.

Constraints:

n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n
*/
package main

import "fmt"

func minimumRecolors(blocks string, k int) int {

	// wCount initially starts at 0
	wCount := 0

	// Count the white blocks in the initial window of size `k`
	for i := 0; i < k; i++ {
		if blocks[i] == 'W' {
			wCount++
		}
	}

	// If  the initial `wCount` was zero, then 0 operations are needed.
	if wCount == 0 {
		return 0
	}

	// Initialize minOps as `wCount` before seeing if we can do better.
	minOps := wCount

	// `left` is the left side of the window, `right` is the right.
	// Advance the window across `blocks`, updating `wCount` and noting `minOps`
	left := 0
	for right := k; right < len(blocks); right++ {
		// if the left block of the previous window was white, remove 1 from `wCount`
		if blocks[left] == 'W' {
			wCount--
		}
		// Shrink window
		left++

		// Increase `wCount` if we encountered another white block when growing window
		if blocks[right] == 'W' {
			wCount++
		}

		// Exit early if `wCount` is zero because operations would be zero.
		if wCount == 0 {
			return 0
		}

		// Update `minOps` if `wCount` is smaller than any before.
		minOps = min(minOps, wCount)

	}
	// Return minOps.
	return minOps
}

// Helper function min()

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}
func main() {
	blocks := "WBWBBBW"
	k := 2
	fmt.Println(minimumRecolors(blocks, k))
}
