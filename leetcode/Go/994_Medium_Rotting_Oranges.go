/*
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
*/
package main

import "fmt"

func orangesRotting(grid [][]int) int {
	R := len(grid)
	C := len(grid[0])

	var freshOranges int
	minutes := 0

	direction := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	type rottenOrange struct {
		Row int
		Col int
	}

	queue := make([]rottenOrange, 0)

	for row := 0; row < R; row++ {
		for col := 0; col < C; col++ {
			if grid[row][col] == 2 {
				queue = append(queue, rottenOrange{Row: row, Col: col})
			} else if grid[row][col] == 1 {
				freshOranges++
			}
		}
	}

	if freshOranges == 0 {
		return 0
	}

	for len(queue) > 0 {
		continueProcessing := false
		levelSize := len(queue)
		for i := 0; i < levelSize; i++ {
			currentRottenOrange := queue[0]
			queue = queue[1:]
			for _, adjacent := range direction {
				adjRow, adjCol := adjacent[0]+currentRottenOrange.Row, adjacent[1]+currentRottenOrange.Col
				if adjRow >= 0 && adjRow < R && adjCol >= 0 && adjCol < C && grid[adjRow][adjCol] == 1 {
					queue = append(queue, rottenOrange{Row: adjRow, Col: adjCol})
					freshOranges -= 1
					grid[adjRow][adjCol] = 2
					continueProcessing = true
				}
			}
		}
		if continueProcessing {
			minutes += 1
		}
	}
	if freshOranges == 0 {
		return minutes
	} else {
		return -1
	}

}

func main() {
	grid := [][]int{{2, 1, 1}, {1, 1, 0}, {0, 1, 1}}
	fmt.Println(orangesRotting(grid))
}
