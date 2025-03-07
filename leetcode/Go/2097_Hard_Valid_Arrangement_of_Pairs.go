/*
You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.

Return any valid arrangement of pairs.

Note: The inputs will be generated such that there exists a valid arrangement of pairs.

Example 1:

Input: pairs = [[5,1],[4,5],[11,9],[9,4]]
Output: [[11,9],[9,4],[4,5],[5,1]]
Explanation:
This is a valid arrangement since endi-1 always equals starti.
end0 = 9 == 9 = start1
end1 = 4 == 4 = start2
end2 = 5 == 5 = start3
Example 2:

Input: pairs = [[1,3],[3,2],[2,1]]
Output: [[1,3],[3,2],[2,1]]
Explanation:
This is a valid arrangement since endi-1 always equals starti.
end0 = 3 == 3 = start1
end1 = 2 == 2 = start2
The arrangements [[2,1],[1,3],[3,2]] and [[3,2],[2,1],[1,3]] are also valid.
Example 3:

Input: pairs = [[1,2],[1,3],[2,1]]
Output: [[1,2],[2,1],[1,3]]
Explanation:
This is a valid arrangement since endi-1 always equals starti.
end0 = 2 == 2 = start1
end1 = 1 == 1 = start2
*/
package main

import "fmt"

func validArrangement(pairs [][]int) [][]int {
	// Create adjacency list and degree tracker
	graph := make(map[int][]int)
	degree := make(map[int]int)

	// Build the graph and calculate degrees
	for _, pair := range pairs {
		u, v := pair[0], pair[1]
		graph[u] = append(graph[u], v)
		degree[u]++
		degree[v]--
	}

	// Determine the starting node
	startNode := pairs[0][0]
	for node, val := range degree {
		if val == 1 {
			startNode = node
			break
		}
	}

	// Use slice as stack for path
	path := []int{}
	nodeStack := []int{startNode}

	for len(nodeStack) > 0 {
		lastIdx := len(nodeStack) - 1
		curr := nodeStack[lastIdx]
		neighbors := graph[curr]

		if len(neighbors) == 0 {
			path = append(path, curr)
			nodeStack = nodeStack[:lastIdx]
		} else {
			nextNode := neighbors[len(neighbors)-1]
			nodeStack = append(nodeStack, nextNode)
			graph[curr] = neighbors[:len(neighbors)-1]
		}
	}

	// Build final arrangement
	arrangement := make([][]int, 0, len(path)-1)
	for i := len(path) - 1; i > 0; i-- {
		arrangement = append(arrangement, []int{path[i], path[i-1]})
	}

	return arrangement
}

func main() {
	// Example input
	var pairs = [][]int{
		{5, 1}, {4, 5}, {11, 9}, {9, 4},
	}
	fmt.Println(validArrangement(pairs))
}
