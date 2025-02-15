/*
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.



Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
*/

package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func CreateBinaryTreeTestCase(nodes []int) *TreeNode {
	n := len(nodes)
	if len(nodes) == 0 {
		return nil
	}
	idx := 1
	root := &TreeNode{Val: nodes[0]}
	stack := []*TreeNode{root}
	for len(stack) > 0 {
		node := stack[0]
		stack = stack[1:]

		if idx < n && nodes[idx] != math.MinInt {
			node.Left = &TreeNode{Val: nodes[idx]}
			stack = append(stack, node.Left)
		}
		idx++

		if idx < n && nodes[idx] != math.MinInt {
			node.Right = &TreeNode{Val: nodes[idx]}
			stack = append(stack, node.Right)
		}
		idx++
	}
	return root

}
func CountNodes(node *TreeNode, count *int, maxVal int) {
	if node == nil {
		return
	}

	if node.Val >= maxVal {
		*count++
		maxVal = node.Val
	}

	CountNodes(node.Left, count, maxVal)
	CountNodes(node.Right, count, maxVal)
}
func goodNodes(root *TreeNode) int {

	var GoodNodes int

	CountNodes(root, &GoodNodes, root.Val)

	return GoodNodes
	/*
		type NodeWithMax struct {
			Node    *TreeNode
			PathMax int
		}

		stack := make([]NodeWithMax, 0, 1000) // Preallocate some memory
		stack = append(stack, NodeWithMax{Node: root, PathMax: root.Val})
		goodNodesCount := 0
		for len(stack) > 0 {
			n := len(stack) - 1
			item := stack[n]
			stack = stack[:n]
			node, pathMax := item.Node, item.PathMax

			//fmt.Println(node.Val)
			if node.Val >= pathMax {
				goodNodesCount++
				pathMax = node.Val
			}

			if node.Left != nil {
				stack = append(stack, NodeWithMax{Node: node.Left, PathMax: pathMax})
			}
			if node.Right != nil {
				stack = append(stack, NodeWithMax{Node: node.Right, PathMax: pathMax})
			}

		}
		return goodNodesCount
	*/
}

func main() {
	nodes := []int{3, 1, 4, 3, math.MinInt, 1, 5}
	root := CreateBinaryTreeTestCase(nodes)
	fmt.Println(goodNodes(root))
}
