/*
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.
*/

package main

import (
	"fmt"
	"sort"
)

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func insertLevelOrder(arr []int, root *TreeNode, i int, n int) *TreeNode {
	if i < n {
		temp := TreeNode{Val: arr[i]}
		root = &temp

		root.Left = insertLevelOrder(arr, root.Left, 2*i+1, n)
		root.Right = insertLevelOrder(arr, root.Right, 2*i+2, n)
	}
	return root
}
func inOrderTraversal(root *TreeNode) {
	if root != nil {
		inOrderTraversal(root.Left)
		fmt.Print(root.Val, " ")
		inOrderTraversal(root.Right)
	}
}

func kthLargestLevelSum(root *TreeNode, k int) int64 {
	if root == nil {
		return -1
	}

	queue := []*TreeNode{root}
	levelSums := []int{}

	for len(queue) > 0 {

		levelSize := len(queue)
		levelSum := 0
		for i := 0; i < levelSize; i++ {

			// Pop the first element in queue
			current := queue[0]
			queue = queue[1:] // deque the front element.

			// Handle the node
			levelSum += current.Val

			if current.Left != nil {
				queue = append(queue, current.Left)
			}

			if current.Right != nil {
				queue = append(queue, current.Right)
			}
		}
		levelSums = append(levelSums, levelSum)
	}
	// Sort level sums in descending order
	sort.Sort(sort.Reverse(sort.IntSlice(levelSums)))

	// Check if k-th largest exists
	if k > len(levelSums) {
		return -1
	}
	return int64(levelSums[k-1])
}

func main() {
	var root *TreeNode
	arr := []int{5, 8, 9, 2, 1, 3, 7}
	k := 2
	n := len(arr)
	root = insertLevelOrder(arr, root, 0, n)

	fmt.Println(kthLargestLevelSum(root, k))
}
