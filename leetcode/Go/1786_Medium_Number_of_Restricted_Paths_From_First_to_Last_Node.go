/*
There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.

A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.

The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 + 7.

Example 1:
Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
Output: 3
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The three restricted paths are:
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5

Example 2:
Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
Output: 1
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The only restricted path is 1 --> 3 --> 7.

Constraints:

1 <= n <= 2 * 104
n - 1 <= edges.length <= 4 * 104
edges[i].length == 3
1 <= ui, vi <= n
ui != vi
1 <= weighti <= 105
There is at most one edge between any two nodes.
There is at least one path between any two nodes.
*/
package main

import (
	"container/heap"
	"fmt"
	"math"
	"sort"
)

const MOD = 1_000_000_007

// PriorityQueue implements a min-heap
type PriorityQueue []Node

type Node struct {
	dist int
	id   int
}

func (pq PriorityQueue) Len() int            { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool  { return pq[i].dist < pq[j].dist }
func (pq PriorityQueue) Swap(i, j int)       { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PriorityQueue) Push(x interface{}) { *pq = append(*pq, x.(Node)) }
func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[:n-1]
	return item
}

func countRestrictedPaths(n int, edges [][]int) int {
	// Step 1: Build Graph
	graph := make(map[int][][]int)
	for i := 1; i <= n; i++ {
		graph[i] = [][]int{}
	}
	for _, edge := range edges {
		u, v, weight := edge[0], edge[1], edge[2]
		graph[u] = append(graph[u], []int{weight, v})
		graph[v] = append(graph[v], []int{weight, u})
	}

	// Step 2: Dijkstra's Algorithm to Find Shortest Paths from Node n
	distance := make([]int, n+1)
	for i := range distance {
		distance[i] = math.MaxInt64
	}
	distance[n] = 0

	pq := &PriorityQueue{}
	heap.Init(pq)
	heap.Push(pq, Node{dist: 0, id: n})

	for pq.Len() > 0 {
		curr := heap.Pop(pq).(Node)
		node, weight := curr.id, curr.dist

		if weight > distance[node] {
			continue
		}

		for _, neighbor := range graph[node] {
			nweight, nnode := neighbor[0], neighbor[1]
			newWeight := weight + nweight
			if newWeight < distance[nnode] {
				distance[nnode] = newWeight
				heap.Push(pq, Node{dist: newWeight, id: nnode})
			}
		}
	}

	// Step 3: DP to Count Restricted Paths
	dp := make([]int, n+1)
	dp[n] = 1

	nodes := make([]int, n)
	for i := 1; i <= n; i++ {
		nodes[i-1] = i
	}

	// Sort nodes by increasing distance (ensuring DP is processed in correct order)
	sort.Slice(nodes, func(i, j int) bool {
		return distance[nodes[i]] < distance[nodes[j]]
	})

	for _, node := range nodes {
		if node == n {
			continue
		}
		for _, neighbor := range graph[node] {
			nnode := neighbor[1]
			if distance[node] > distance[nnode] { // Only count valid restricted paths
				dp[node] = (dp[node] + dp[nnode]) % MOD
			}
		}
	}

	return dp[1]
}

func main() {
	n := 5
	edges := [][]int{{1, 2, 3}, {1, 3, 3}, {2, 3, 1}, {1, 4, 2}, {5, 2, 2}, {3, 5, 1}, {5, 4, 10}}
	fmt.Println(countRestrictedPaths(n, edges))
}
