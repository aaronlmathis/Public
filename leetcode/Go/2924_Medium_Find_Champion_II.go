/*
There are n teams numbered from 0 to n - 1 in a tournament; each team is also a node in a DAG.

You are given the integer n and a 0-indexed 2D integer array edges of length m representing the DAG, where edges[i] = [ui, vi] indicates that there is a directed edge from team ui to team vi in the graph.

A directed edge from a to b in the graph means that team a is stronger than team b and team b is weaker than team a.

Team a will be the champion of the tournament if there is no team b that is stronger than team a.

Return the team that will be the champion of the tournament if there is a unique champion, otherwise, return -1.

# Notes

A cycle is a series of nodes a1, a2, ..., an, an+1 such that node a1 is the same node as node an+1, the nodes a1, a2, ..., an are distinct, and there is a directed edge from the node ai to node ai+1 for every i in the range [1, n].
A DAG is a directed graph that does not have any cycle.
*/
package main

import "fmt"

func findChampion(n int, edges [][]int) int {
	// Create an boolean array where i represents each team and teams[i] represents whether team i can be the champion.
	// All teams start with the ability to be the champion (True)
	teams := make([]bool, n)
	for i := 0; i < n; i++ {
		teams[i] = true
	}
	// Iterate through the edges, since each edge [u, v] means team u is better than team v, we know that teams[v] becomes False
	// They cannot be the champion if someone is better than them.
	for _, edge := range edges {
		teams[edge[1]] = false
	}
	// Set the intial champion to -1
	champion := -1

	// Set the champCount to 0 as there are no champions yet
	champCount := 0

	// Iterate through teams looking for any team that is still able to be the champion
	// If found, set teh champion to the id of that team and increase the champCount by one
	// IF and only if champCount is 1, return the champion. Otherwise return -1
	for id, team := range teams {
		if team == true {
			champCount++
			champion = id

		}
	}
	if champCount == 1 {
		return champion
	} else {
		return -1
	}
}
func main() {
	var n int = 3
	var edges = [][]int{
		{0, 1},
		{1, 2},
	}
	fmt.Println(findChampion(n, edges))
}
