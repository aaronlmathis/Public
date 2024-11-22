/*
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

Example 1:

Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
Example 2:

Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
*/
package main

import "fmt"

func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
	// Step 1: Initialize the grid
	seen := make([][]byte, m)
	for y := 0; y < m; y++ {
		seen[y] = make([]byte, n)
		for x := 0; x < n; x++ {
			seen[y][x] = 'O' // Open cell
		}
	}

	// Step 2: Mark walls and guards
	for _, wall := range walls {
		seen[wall[0]][wall[1]] = 'W' // Wall
	}
	for _, guard := range guards {
		seen[guard[0]][guard[1]] = 'G' // Guard
	}

	// Step 3: Mark visibility from guards
	for _, guard := range guards {
		y, x := guard[0], guard[1]

		// Left
		for left := x - 1; left >= 0 && seen[y][left] != 'W' && seen[y][left] != 'G'; left-- {
			seen[y][left] = 'X'
		}

		// Right
		for right := x + 1; right < n && seen[y][right] != 'W' && seen[y][right] != 'G'; right++ {
			seen[y][right] = 'X'
		}

		// Up
		for up := y - 1; up >= 0 && seen[up][x] != 'W' && seen[up][x] != 'G'; up-- {
			seen[up][x] = 'X'
		}

		// Down
		for down := y + 1; down < m && seen[down][x] != 'W' && seen[down][x] != 'G'; down++ {
			seen[down][x] = 'X'
		}
	}

	// Step 4: Count unguarded cells
	unguardedCount := 0
	for y := 0; y < m; y++ {
		for x := 0; x < n; x++ {
			if seen[y][x] == 'O' { // Cell is still open and unguarded
				unguardedCount++
			}
		}
	}

	return unguardedCount
}

func main() {
	var m int = 4
	var n int = 6
	guards := [][]int{
		{0, 0},
		{1, 1},
		{2, 3},
	}
	walls := [][]int{
		{0, 1},
		{2, 2},
		{1, 4},
	}
	fmt.Println(countUnguarded(m, n, guards, walls))
}
