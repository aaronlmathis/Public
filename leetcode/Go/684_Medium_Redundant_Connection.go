/*
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

Constraints:
n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
*/
package main

import "fmt"

func findRedundantConnection(edges [][]int) []int {
	n := len(edges)
	parent := make([]int, n+1)
	rank := make([]int, n+1)
	for i := range rank {
		rank[i] = 1
	}
	// Initialize the parent array
	for i := range parent {
		parent[i] = i
	}

	// Find function with path compression
	var find func(int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x]) // Path compression
		}
		return parent[x]
	}
	var union func(int, int) bool
	union = func(x int, y int) bool {
		rootX := find(x)
		rootY := find(y)

		if rank[rootX] >= rank[rootY] {
			parent[rootX] = rootY
			rank[rootX] += rank[rootY]
		} else {
			parent[rootY] = rootX
			rank[rootY] += rank[rootX]
		}
		if rootX == rootY {
			return false
		}
		parent[rootX] = rootY
		return true
	}

	for _, edge := range edges {
		if !union(edge[0], edge[1]) {
			return edge
		}
	}
	return []int{}
}

func main() {
	edges := [][]int{{1, 2}, {1, 3}, {2, 3}}
	answer := []int{2, 3}
	fmt.Println(findRedundantConnection(edges))
	fmt.Println(answer)
	edges = [][]int{{1, 2}, {2, 3}, {3, 4}, {1, 4}, {1, 5}}
	answer = []int{1, 4}
	fmt.Println(findRedundantConnection(edges))
	fmt.Println(answer)
}
