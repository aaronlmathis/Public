/*
You are given an integer n and a 2D integer array queries.
There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.
queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.
Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.

Example 1:
Input: n = 5, queries = [[2,4],[0,2],[0,4]]
Output: [3,2,1]
Explanation:

Example 2:
Input: n = 4, queries = [[0,3],[0,2]]
Output: [1,1]
Explanation:
*/
package main

import (
	"fmt"
)

type PriorityQueueItem struct {
	node, distance int
}

type PriorityQueue struct {
	items []PriorityQueueItem
}

func (pq *PriorityQueue) Push(item PriorityQueueItem) {
	pq.items = append(pq.items, item)
	pq.bubbleUp(len(pq.items) - 1)
}

func (pq *PriorityQueue) bubbleUp(index int) {
	for index > 0 {
		parent := (index - 1) / 2
		if pq.items[index].distance >= pq.items[parent].distance {
			break
		}
		pq.items[index], pq.items[parent] = pq.items[parent], pq.items[index]
		index = parent
	}
}

func (pq *PriorityQueue) bubbleDown(index int) {
	lastIndex := len(pq.items) - 1
	for {
		left := 2*index + 1
		right := 2*index + 2
		smallest := index

		if left <= lastIndex && pq.items[left].distance < pq.items[smallest].distance {
			smallest = left
		}
		if right <= lastIndex && pq.items[right].distance < pq.items[smallest].distance {
			smallest = right
		}
		if smallest == index {
			break
		}
		pq.items[index], pq.items[smallest] = pq.items[smallest], pq.items[index]
		index = smallest
	}
}

func shortestDistanceAfterQueries(n int, queries [][]int) []int {
	extraEdges := make([][]int, n)
	dist := make([]int, n)
	pq := &PriorityQueue{}
	results := make([]int, len(queries))

	for i := 0; i < n; i++ {
		dist[i] = i
	}

	for i, q := range queries {
		u, v := q[0], q[1]
		extraEdges[u] = append(extraEdges[u], v)

		if len(pq.items) > 0 {
			pq.items = pq.items[:0]
		}

		pq.Push(PriorityQueueItem{u, dist[u]})

		for len(pq.items) > 0 {
			current := pq.items[0]
			last := pq.items[len(pq.items)-1]
			pq.items = pq.items[:len(pq.items)-1]
			if len(pq.items) > 0 {
				pq.items[0] = last
				pq.bubbleDown(0)
			}

			if current.distance > dist[current.node] {
				continue
			}

			if current.node == n-1 {
				dist[n-1] = current.distance
				break
			}

			if current.node < n-1 {
				neighbor := current.node + 1
				newDist := current.distance + 1
				if newDist < dist[neighbor] {
					dist[neighbor] = newDist
					pq.items = append(pq.items, PriorityQueueItem{neighbor, newDist})
					pq.bubbleUp(len(pq.items) - 1)
				}
			}

			for _, neighbor := range extraEdges[current.node] {
				newDist := current.distance + 1
				if newDist < dist[neighbor] {
					dist[neighbor] = newDist
					pq.items = append(pq.items, PriorityQueueItem{neighbor, newDist})
					pq.bubbleUp(len(pq.items) - 1)
				}
			}
		}

		results[i] = dist[n-1]
	}

	return results
}

func main() {
	var n int = 5
	var queries = [][]int{
		{2, 4},
		{0, 2},
		{0, 4},
	}
	fmt.Println(shortestDistanceAfterQueries(n, queries))
}
