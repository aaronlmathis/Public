/*
There is an undirected weighted graph with n vertices labeled from 0 to n - 1.

You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.

A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.

The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the bitwise AND operator.

You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending at vertex ti. If there exists no such walk, the answer is -1.

Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.

Example 1:
Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]
Output: [1,-1]
Explanation:
To achieve the cost of 1 in the first query, we need to move on the following edges: 0->1 (weight 7), 1->2 (weight 1), 2->1 (weight 1), 1->3 (weight 7).
In the second query, there is no walk between nodes 3 and 4, so the answer is -1.

Example 2:
Input: n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]
Output: [0]
Explanation:
To achieve the cost of 0 in the first query, we need to move on the following edges: 1->2 (weight 1), 2->1 (weight 6), 1->2 (weight 1).

Constraints:
2 <= n <= 105
0 <= edges.length <= 105
edges[i].length == 3
0 <= ui, vi <= n - 1
ui != vi
0 <= wi <= 105
1 <= query.length <= 105
query[i].length == 2
0 <= si, ti <= n - 1
si != ti
*/
package main

import "fmt"

var parent []int
var minimumWeight []int
var rank []int

// DSU Find with path compression
func find(x int) int {
	p := parent[x]
	for x != p {
		parent[x], x, p = parent[parent[x]], parent[x], parent[parent[x]]
	}
	return p
}

// DSU Join with Ranking + calculating min weight
func join(x, y, w int) {
	rootX, rootY := find(x), find(y)

	// Determine minimum result of & operation of *all* the weights for edges between these two nodes.
	minimumWeight[rootX] &= w & minimumWeight[rootY]
	minimumWeight[rootY] = minimumWeight[rootX]

	if rootX == rootY {
		return
	}

	if rank[rootX] >= rank[rootY] {
		parent[rootY] = rootX
		rank[rootX] += rank[rootY]
	} else {
		parent[rootX] = rootY
		rank[rootY] += rank[rootX]
	}
}

func minimumCost(n int, edges [][]int, query [][]int) []int {
	parent = make([]int, n)
	rank = make([]int, n)
	minimumWeight = make([]int, n)

	// Initialize parent, rank, and minimumWeight Slice's
	for i := 0; i < n; i++ {
		parent[i] = i
		rank[i] = 1
		minimumWeight[i] = 131071
	}

	answer := make([]int, len(query))

	// Join all connected node - while calculating minimum weights
	for _, edge := range edges {
		join(edge[0], edge[1], edge[2])
	}

	// Process Queries
	for i, q := range query {
		// Find parent of start and end node. We can assume:
		//   1. If they aren't the same, there ain't a path
		//   2. Any node that shares a parent (After compression of course) is in that path.
		parentStart, parentEnd := find(q[0]), find(q[1])
		if parentStart == parentEnd && minimumWeight[parentStart] != 131071 {
			answer[i] = minimumWeight[parentStart]
		} else {
			answer[i] = -1
		}

	}
	return answer
}

func main() {
	n := 5
	edges := [][]int{{0, 1, 7}, {1, 3, 7}, {1, 2, 1}}
	query := [][]int{{0, 3}, {3, 4}}
	fmt.Println(minimumCost(n, edges, query))
}
