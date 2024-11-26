/*
You are given an n x n integer matrix. You can do the following operation any number of times:

	Choose any two adjacent elements of matrix and multiply each of them by -1.
	Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

Example 1:
Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.

Example 2:
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
*/
package main

import (
	"fmt"
	"math"
)

func maxMatrixSum(matrix [][]int) int64 {
	// Initialize variables:
	// - negCount: Tracks the count of negative numbers in the matrix.
	// - absSum: Accumulates the sum of the absolute values of all elements.
	// - minAbs: Stores the minimum absolute value in the matrix, initialized to positive infinity.
	negCount, absSum, minAbs := 0, 0, math.Inf(1)

	// Iterate through each row of the matrix.
	for _, row := range matrix {
		// Iterate through each number in the current row.
		for _, num := range row {
			// If the number is negative, increment the negCount.
			if num < 0 {
				negCount++
			}
			// Calculate the absolute value of the current number.
			absVal := math.Abs(float64(num))

			// Update the minimum absolute value encountered so far.
			minAbs = math.Min(minAbs, absVal)

			// Add the absolute value of the current number to the total sum.
			absSum += int(absVal)
		}
	}

	// Determine the result:
	// - If there is an even number of negative numbers or a zero in the matrix,
	//   the largest sum is the sum of absolute values (negatives cancel out).
	if negCount%2 == 0 || minAbs == 0 {
		return int64(absSum)
	} else {
		// If there is an odd number of negatives and no zeros,
		//   the smallest absolute value must remain negative.
		//   Subtract twice the smallest absolute value to account for this.
		return int64(absSum - 2*int(minAbs))
	}
}

func main() {
	var matrix = [][]int{
		{2, 9, 3},
		{5, 4, -4},
		{1, 7, 1},
	}
	fmt.Println(maxMatrixSum(matrix))
}
