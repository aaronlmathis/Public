/*
You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents the minimum time required to be able to visit the cell (row, col), which means you can visit the cell (row, col) only when the time you visit it is greater than or equal to grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent cell in the four directions: up, down, left, and right. Each move you make takes 1 second.

Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the bottom-right cell, then return -1.

Example 1:
Input: grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
Output: 7
Explanation: One of the paths that we can take is the following:
- at t = 0, we are on the cell (0,0).
- at t = 1, we move to the cell (0,1). It is possible because grid[0][1] <= 1.
- at t = 2, we move to the cell (1,1). It is possible because grid[1][1] <= 2.
- at t = 3, we move to the cell (1,2). It is possible because grid[1][2] <= 3.
- at t = 4, we move to the cell (1,1). It is possible because grid[1][1] <= 4.
- at t = 5, we move to the cell (1,2). It is possible because grid[1][2] <= 5.
- at t = 6, we move to the cell (1,3). It is possible because grid[1][3] <= 6.
- at t = 7, we move to the cell (2,3). It is possible because grid[2][3] <= 7.
The final time is 7. It can be shown that it is the minimum time possible.

Example 2:
Input: grid = [[0,2,4],[3,2,1],[1,0,4]]
Output: -1
Explanation: There is no path from the top left to the bottom-right cell.
*/
package main

import (
	"container/heap"
	"fmt"
)

type priorityQueueItem struct {
	time, row, col int
}

type priorityQueue struct {
	items []priorityQueueItem
}

func (pq *priorityQueue) Len() int { return len(pq.items) }

func (pq *priorityQueue) Less(i, j int) bool { return pq.items[i].time < pq.items[j].time }

func (pq *priorityQueue) Swap(i, j int) {
	pq.items[i], pq.items[j] = pq.items[j], pq.items[i]
}

func (pq *priorityQueue) Push(x interface{}) {
	pq.items = append(pq.items, x.(priorityQueueItem))
}

func (pq *priorityQueue) Pop() interface{} {
	last := len(pq.items) - 1
	root := pq.items[last]
	pq.items = pq.items[:last]
	return root
}

func minimumTime(grid [][]int) int {
	R, C := len(grid), len(grid[0])

	// Early check for unsolvable grid
	if (R > 1 && grid[1][0] > 1) && (C > 1 && grid[0][1] > 1) {
		return -1
	}

	// Visited matrix to avoid redundant processing
	visit := make([][]bool, R)
	for i := 0; i < R; i++ {
		visit[i] = make([]bool, C)
	}
	visit[0][0] = true

	// Directions for movement: up, right, down, left
	directions := [][2]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}

	// Priority queue initialization
	pq := &priorityQueue{}
	heap.Init(pq)
	heap.Push(pq, priorityQueueItem{time: 0, row: 0, col: 0})

	for pq.Len() > 0 {
		curr := heap.Pop(pq).(priorityQueueItem)

		// Explore all neighbors
		for _, dir := range directions {
			nrow, ncol := curr.row+dir[0], curr.col+dir[1]

			// Skip invalid or already visited neighbors
			if nrow < 0 || nrow >= R || ncol < 0 || ncol >= C || visit[nrow][ncol] {
				continue
			}

			// Calculate the earliest possible time to reach the neighbor
			newTime := curr.time + 1
			if grid[nrow][ncol] > newTime {
				newTime += (grid[nrow][ncol] - curr.time + 1) / 2 * 2
			}

			// If the neighbor is the bottom-right corner, return the time to reach it
			if nrow == R-1 && ncol == C-1 {
				return newTime
			}

			// Mark the neighbor as visited and push it to the priority queue
			visit[nrow][ncol] = true
			heap.Push(pq, priorityQueueItem{time: newTime, row: nrow, col: ncol})
		}
	}

	// If the bottom-right corner is unreachable, return -1
	return -1
}

func main() {
	var grid = [][]int{
		{0, 1, 3, 2},
		{5, 1, 2, 5},
		{4, 3, 8, 6},
	}
	fmt.Println(minimumTime(grid))
}
