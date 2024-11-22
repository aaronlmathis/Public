/*
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

Example 1:

Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.

Example 2:
Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.

Example 3:
Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
*/
package main

import "fmt"

func maxEqualRowsAfterFlips(matrix [][]int) int {
	// Initialize a map to track occurances of binary strings
	binaryMap := make(map[string]int)

	// Iterate through rows of matrix, making a []byte for each row
	for _, row := range matrix {
		canonical := make([]byte, len(row))
		// for each column in row, calculate the bitwise XOR and add it to canonical slice for the row
		for i, col := range row {
			canonical[i] = byte(col ^ row[0])
		}
		// Add canonical binary string to binaryMap and increase count by one
		binaryMap[string(canonical)]++

	}
	// Return the maximum count found in the map
	maxCount := 0
	for _, count := range binaryMap {
		if count > maxCount {
			maxCount = count
		}
	}
	return maxCount
}

func main() {
	matrix := [][]int{
		{0, 1},
		{1, 1},
	}
	fmt.Println(maxEqualRowsAfterFlips(matrix))
}
