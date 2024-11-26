/*
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Example 1:
Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

Example 2:
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.

Example 3:
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
*/
package main

import (
	"container/list"
	"fmt"
	"strings"
)

// Helper function to stringify a state
func stringifyState(state []int) string {
	return strings.Trim(strings.Join(strings.Fields(fmt.Sprint(state)), ""), "[]")
}

func slidingPuzzle(board [][]int) int {
	var solvedState = []int{1, 2, 3, 4, 5, 0}
	var state []int
	for _, row := range board {
		for _, num := range row {
			state = append(state, num)
		}
	}
	// Define the State struct to track the board and move count
	type State struct {
		Board     []int
		MoveCount int
	}
	// Initialize the queue using container/list
	queue := list.New()
	queue.PushBack(State{Board: state, MoveCount: 0})

	// Flatten the board into a string to use as a key
	initialState := stringifyState(state)

	// Define the visited set as a map
	visited := make(map[string]bool)
	visited[initialState] = true

	// Define the map for available moves
	availableMoves := map[int][]int{
		0: {1, 3},    // Top-left
		1: {0, 2, 4}, // Top-middle
		2: {1, 5},    // Top-right
		3: {0, 4},    // Bottom-left
		4: {1, 3, 5}, // Bottom-middle
		5: {2, 4},    // Bottom-right
	}

	for queue.Len() > 0 {
		// Dequeue the first element
		element := queue.Front()
		current := element.Value.(State)
		queue.Remove(element)

		// Check if the current board matches the solved state
		isSolved := true

		for i := range current.Board {
			if current.Board[i] != solvedState[i] {
				isSolved = false
				break
			}
		}
		if isSolved {
			return current.MoveCount // Return the move count if solved
		}
		zeroIndex := -1
		for i := 0; i < len(current.Board); i++ {
			if current.Board[i] == 0 {
				zeroIndex = i
				break
			}
		}
		// Process all moves for the empty space
		for _, swap := range availableMoves[zeroIndex] {
			// Swap in place
			current.Board[zeroIndex], current.Board[swap] = current.Board[swap], current.Board[zeroIndex]

			// Serialize and check if visited
			stringifiedState := stringifyState(current.Board)
			if !visited[stringifiedState] {
				// Mark the new state as visited
				visited[stringifiedState] = true
				// Add the new state to the queue
				newBoard := append([]int{}, current.Board...) // Copy the board
				queue.PushBack(State{Board: newBoard, MoveCount: current.MoveCount + 1})
			}

			// Revert the swap
			current.Board[zeroIndex], current.Board[swap] = current.Board[swap], current.Board[zeroIndex]
		}
	}
	// Return -1 if no solution is found
	return -1
}

func main() {
	var board = [][]int{
		{4, 1, 2},
		{5, 0, 3},
	}
	fmt.Println(slidingPuzzle(board))
}
