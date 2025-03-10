/*
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

Example 1:
Input: colors = [0,1,0,1,0], k = 3
Output: 3
Explanation:
Alternating groups:

Example 2:
Input: colors = [0,1,0,0,1,0,1], k = 6
Output: 2
Explanation:
Alternating groups:

Example 3:
Input: colors = [1,1,0,1], k = 4
Output: 0
Explanation:

Constraints:
3 <= colors.length <= 105
0 <= colors[i] <= 1
3 <= k <= colors.length
*/
package main

import "fmt"

func numberOfAlternatingGroups(colors []int, k int) int {
	n := len(colors)
	agroups := 0

	left, right := 0, 1

	for colors[left] != colors[right] {
		left++
		right++
		if right == n {
			if n%2 == 0 {
				return n
			} else {
				return n - k + 1
			}
		}

	}

	left = right
	// Now - make one full cycle.
	// Every time double color is encountered:
	//   - if right-left >= k-1, add (right-left+1) - k + 1 to agroups
	//   - slide left to right.
	//   - continue until either a) double color tile b) we have made a full cycle of `n` tiles
	for right = left + 1; right < left+n; right++ {
		fmt.Printf("%v - %v\n", left, right)
		if colors[right%n] == colors[(right-1)%n] {
			fmt.Println("dupe")
			if right-left > k-1 {
				agroups += (right - left) - k + 1
			}
			left = right
			break
		}

	}
	fmt.Printf("%v, %v", right, left)
	if right-left >= k-1 {
		fmt.Println("True")
		agroups += (right - left) - k + 1
	}

	return agroups
}

func main() {
	colors := []int{0, 1, 0, 0, 1, 0, 1}
	k := 6
	colors = []int{1, 1, 0, 1}
	k = 4
	fmt.Println(numberOfAlternatingGroups(colors, k))
}
