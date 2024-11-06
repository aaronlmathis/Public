/*
There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.

The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.

All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.

At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.

Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.

# Note that

All robots move at the same speed.
If two robots move in the same direction, they will never collide.
If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
If the robot moved from a position x to a position y, the distance it moved is |y - x|.
*/
package main

import (
	"fmt"
	"math"
	"sort"
)

// MinInt function to return the minimum of two integers
func MinInt(a, b int) int {
    if a < b {
        return a
    }
    return b
}

// Abs function to return the absolute value of an integer
func Abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func minimumTotalDistance(robot []int, factory [][]int) int64 {

	// Sort the factories and robots
	sort.Slice(factory, func(i, j int) bool {
		return factory[i][0] < factory[j][0]
	})
	sort.Ints(robot)

	// Unpack the factory slice
	// Initialize an empty slice to store expanded factory positions
	var factories []int

	// Loop over each factory, unpacking each by its capacity
	for _, f := range factory {
		position := f[0]
		capacity := f[1]

		// Append the position `capacity` times
		for i := 0; i < capacity; i++ {
			factories = append(factories, position)
		}
	}

	n := len(robot)
	m := len(factories)

	// Initialize DP Table where dp[i][j] = Let dp[i][j] represent the minimum distance for the first i robots visiting the first j factories.

	dp := make([][]float64, n+1)

	for i := 0; i <= n; i++ {
		row := make([]float64, m+1)
		for j := 0; j <= m; j++ {
			row[j] = math.Inf(1) // Set each element to positive infinity
		}
		dp[i] = row // Append the row to dp
	}

	for i := 0; i <= m; i++ {
		dp[0][i] = 0
	}
	// Fil DP table
	for i:= 1; i<= n; i++ {
		for j := 1; j <= m {
			dp[i][j] = MinInt(dp[i][j-1], dp[i-1][j-1] + Abs(robot[i-1] - factories[j-1]))
		}
	}

	// Return distance for all robots / all factories.

	return dp[n][m]
}

func main() {
	factory := [][]int{
		{2, 2},
		{6, 2},
	}
	robot := []int{0, 4, 6}
	fmt.Println(minimumTotalDistance(robot, factory))
}
