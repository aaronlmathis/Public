/*
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]
*/
package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Constructor function for TreeNode
func NewTreeNode(val int) *TreeNode {
	return &TreeNode{
		Val: val,
	}
}

func largestValues(root *TreeNode) []int {
	// int slice to return the max level values
	levelMaxVals := []int{}

	// Quick exit if root is null
	if root == nil {
		return levelMaxVals
	}

	// Create TreeNode slice (storing pointers) to act as a queu
	queue := []*TreeNode{root}

	// Process queue by iterating while queue has something in it.
	for len(queue) > 0 {
		// Get the current length of queue to see how many nodes need processed
		n := len(queue)

		// Set currLvlMax to the first Val in queue for the level
		currLvlMax := queue[0].Val

		// Since we want to process every node on each level before moving on in the queue, we need to iterate for each node in queue
		for i := 0; i < n; i++ {
			// Pop the first node (FIFO)
			node := queue[0]
			queue = queue[1:]

			// See if node.Val is greater than currLvlMax, if so, set currLvlMax to node.Val
			if node.Val > currLvlMax {
				currLvlMax = node.Val
			}

			// If node has a Left, add it to queue
			if node.Left != nil {
				queue = append(queue, node.Left)
			}

			// If node has a Right, add it to queue
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}

		// Add currLvlMax to levelMaxVal at end of processing level
		levelMaxVals = append(levelMaxVals, currLvlMax)
	}

	// Return the slice of max level vals
	return levelMaxVals
}

func main() {
	/*
		root := NewTreeNode(1)
		root.Left = NewTreeNode(3)
		root.Right = NewTreeNode(5)

		root.Left.Left = NewTreeNode(5)
		root.Left.Right = NewTreeNode(3)

		root.Right.Right = NewTreeNode(9)
	*/

	fmt.Println(largestValues(nil))
}
