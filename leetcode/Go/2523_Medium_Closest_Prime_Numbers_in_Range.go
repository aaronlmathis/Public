/*
Given two positive integers left and right, find the two integers num1 and num2 such that:

  - left <= num1 < num2 <= right .
  - Both num1 and num2 are prime numbers.
  - num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.

Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

Example 1:
Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.

Constraints:

1 <= left <= right <= 106
*/

package main

import (
	"fmt"
	"math"
)

func closestPrimes(left int, right int) []int {
	isPrime := func(num int) bool {
		if num == 1 {
			return false
		}

		maxNum := int(math.Sqrt(float64(num)))
		for divisor := 2; divisor <= maxNum; divisor++ {
			if num%divisor == 0 {
				return false
			}
		}
		return true
	}

	primeNumbers := []int{}

	// Find all prime numbers in the given range
	for candidate := left; candidate <= right; candidate++ {
		if candidate%2 == 0 && candidate > 2 {
			continue
		}

		if isPrime(candidate) {
			// If a twin prime (or [2, 3]) is found, return immediately
			if len(primeNumbers) > 0 && candidate <= primeNumbers[len(primeNumbers)-1]+2 {
				return []int{
					primeNumbers[len(primeNumbers)-1],
					candidate,
				}
			}
			primeNumbers = append(primeNumbers, candidate)
		}
	}

	// If fewer than 2 primes exist, return {-1, -1}
	if len(primeNumbers) < 2 {
		return []int{-1, -1}
	}

	// Find the closest prime pair
	closestPair := []int{-1, -1}
	minDifference := math.MaxInt

	for index := 1; index < len(primeNumbers); index++ {
		difference := primeNumbers[index] - primeNumbers[index-1]

		if difference < minDifference {
			minDifference = difference
			closestPair = []int{primeNumbers[index-1], primeNumbers[index]}
		}
	}

	return closestPair
}

func main() {
	left, right := 4, 6
	fmt.Println(closestPrimes(left, right))
}
