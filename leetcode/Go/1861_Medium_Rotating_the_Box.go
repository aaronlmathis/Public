/*
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

Input: box = [["#",".","#"]]
Output: [["."],

	["#"],
	["#"]]

Example 2:

Input: box = [["#",".","*","."],

	["#","#","*","."]]

Output: [["#","."],

	["#","#"],
	["*","*"],
	[".","."]]

Example 3:

Input: box = [["#","#","*",".","*","."],

	["#","#","#","*",".","."],
	["#","#","#",".","#","."]]

Output: [[".","#","#"],

	[".","#","#"],
	["#","#","*"],
	["#","*","."],
	["#",".","*"],
	["#",".","."]]
*/
package main

import (
	"fmt"
)

func rotateTheBox(box [][]byte) [][]byte {
	rows := len(box)
	cols := len(box[0])

	// Step 1: Simulate sliding rocks ('#') downwards within each row
	for r := 0; r < rows; r++ { // Traverse the row in reverse order
		i := cols - 1
		for c := cols - 1; c >= 0; c-- {
			// If we find a rock, swap it with the position at 'i'
			if box[r][c] == '#' {
				temp := box[r][c]
				box[r][c] = box[r][i]
				box[r][i] = temp
				i-- // Update the next available position for the rock
			} else if box[r][c] == '*' {
				// If we find an obstacle, reset 'i' to just before the obstacle
				i = c - 1
			}
		}
	}

	// Step 2: Rotate the box 90 degrees clockwise
	var newBox = [][]byte{}
	for c := 0; c < cols; c++ { // Iterate through each column of the original box
		col := []byte{}
		for r := rows - 1; r >= 0; r-- { // Traverse the rows in reverse for rotation
			col = append(col, box[r][c]) // Add elements to the new column
		}
		newBox = append(newBox, col) // Append the rotated column to the new box
	}
	return newBox
}

func main() {
	var box = [][]byte{
		{'#', '.', '*', '.'},
		{'#', '#', '*', '.'},
	}
	fmt.Println(rotateTheBox(box))
}
