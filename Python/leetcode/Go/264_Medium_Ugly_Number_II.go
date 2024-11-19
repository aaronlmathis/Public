/*
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
*/

package main

import "fmt"

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func nthUglyNumber(n int) int {
	var dp []int = make([]int, n)
	dp[0] = 1
	i2, i3, i5 := 0, 0, 0
	for i := 1; i < n; i++ {
		n2 := dp[i2] * 2
		n3 := dp[i3] * 3
		n5 := dp[i5] * 5

		dp[i] = min(n2, min(n3, n5))

		if dp[i] == n2 {
			i2++
		}
		if dp[i] == n3 {
			i3++
		}
		if dp[i] == n5 {
			i5++
		}
	}
	return dp[n-1]
}

func main() {
	var n int = 10
	fmt.Println(nthUglyNumber(n))
}
