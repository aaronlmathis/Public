/*
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:
    - 0 represents an empty cell,
    - 1 represents an obstacle that may be removed.

You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.

Example 2:
Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
*/

package main

import (
	"fmt"
	"math"
)

type priorityQueueItem struct {
	cost, row, col int
}

type priorityQueue struct {
	items []priorityQueueItem
}

func (pq *priorityQueue) push(item priorityQueueItem) {
	pq.items = append(pq.items, item)
	pq.bubbleUp(len(pq.items) - 1)
}

func (pq *priorityQueue) bubbleUp(index int) {
	for index > 0 {
		parent := (index - 1) / 2
		if pq.items[index].cost >= pq.items[parent].cost {
			break
		} else {
			pq.items[index], pq.items[parent] = pq.items[parent], pq.items[index]
			index = parent
		}
	}
}

func (pq *priorityQueue) bubbleDown(index int) {
	lastIndex := len(pq.items) - 1
	for {
		left := 2*index + 1
		right := 2*index + 2
		smallest := index

		if left <= lastIndex && pq.items[left].cost < pq.items[smallest].cost {
			smallest = left
		}
		if right <= lastIndex && pq.items[right].cost < pq.items[smallest].cost {
			smallest = right
		}
		if smallest == index {
			break
		}
		pq.items[index], pq.items[smallest] = pq.items[smallest], pq.items[index]
		index = smallest
	}
}
func (pq *priorityQueue) pop() priorityQueueItem {
	if len(pq.items) == 0 {
		panic("Priority Queue is empty")
	}
	root := pq.items[0]
	lastIndex := len(pq.items) - 1
	pq.items[0] = pq.items[lastIndex]
	pq.items = pq.items[:lastIndex]
	pq.bubbleDown(0)

	return root
}

func minimumObstacles(grid [][]int) int {
	m, n := len(grid), len(grid[0])

	// Array to track cost to reach last cell cost[row][col] = cost
	cost := make([][]float64, m)
	for i := 0; i < m; i++ {
		cost[i] = make([]float64, n)
	}
	for row := 0; row < m; row++ {
		for col := 0; col < n; col++ {
			cost[row][col] = math.Inf(1)
		}
	}
	// Directions for possible moves - right, up, left, down
	var directions = [4][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

	// Initialize priorityQueue and add first cell with a cost of zero
	pq := &priorityQueue{}
	pq.push(priorityQueueItem{0, 0, 0}) // Starting cell (0 cost, row 0, col 0)

	// Process priority queue items

	for len(pq.items) > 0 {
		current := pq.pop()

		if current.row == m-1 && current.col == n-1 {
			return current.cost
		}
		for _, dir := range directions {
			dr, dc := dir[0], dir[1]
			nrow, ncol := current.row+dr, current.col+dc
			if nrow >= 0 && nrow < m && ncol >= 0 && ncol < n {
				ncost := current.cost + grid[nrow][ncol]
				if float64(ncost) < cost[nrow][ncol] {
					cost[nrow][ncol] = float64(ncost)
					pq.push(priorityQueueItem{ncost, nrow, ncol})
				}
			}

		}
	}
	return int(cost[m-1][n-1])

}

func main() {
	var grid = [][]int{
		{0, 1, 1},
		{1, 1, 0},
		{1, 1, 0},
	}
	fmt.Println(minimumObstacles(grid))
}
