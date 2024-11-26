/*
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
*/
package main

import "fmt"

func spiralOrder(matrix [][]int) []int {
	// Get the dimensions of the matrix
	var m int = len(matrix)    // Number of rows
	var n int = len(matrix[0]) // Number of columns

	// Initialize the result slice to store the spiral order
	var result = []int{}

	// Initialize boundaries:
	// - top: The topmost unvisited row
	// - bottom: The bottommost unvisited row
	// - left: The leftmost unvisited column
	// - right: The rightmost unvisited column
	top, bottom := 0, m-1
	left, right := 0, n-1

	// Continue looping while the boundaries are valid
	for top <= bottom && left <= right {
		// Traverse from left to right along the top boundary
		for col := left; col < right+1; col++ {
			result = append(result, matrix[top][col]) // Append elements in the top row
		}
		top++ // Move the top boundary down

		// Traverse from top to bottom along the right boundary
		for row := top; row < bottom+1; row++ {
			result = append(result, matrix[row][right]) // Append elements in the rightmost column
		}
		right-- // Move the right boundary left

		// Traverse from right to left along the bottom boundary, if still valid
		if top <= bottom {
			for col := right; col > left-1; col-- {
				result = append(result, matrix[bottom][col]) // Append elements in the bottom row
			}
			bottom-- // Move the bottom boundary up
		}

		// Traverse from bottom to top along the left boundary, if still valid
		if left <= right {
			for row := bottom; row > top-1; row-- {
				result = append(result, matrix[row][left]) // Append elements in the leftmost column
			}
			left++ // Move the left boundary right
		}
	}

	// Return the result slice containing the matrix elements in spiral order
	return result
}

func main() {
	var matrix = [][]int{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}}
	fmt.Println(spiralOrder(matrix))
	fmt.Println("[1 2 3 4 8 12 11 10 9 5 6 7]")
}
