package utils

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func BuildBinaryTree(nodes []int) *TreeNode {
	if len(nodes) < 1 {
		return nil
	}
	idx := 1
	root := &TreeNode{Val: nodes[0]}
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]

		if idx < len(nodes) && nodes[idx] != -1 {
			node.Left = &TreeNode{Val: nodes[idx]}
			queue = append(queue, node.Left)
		}
		idx++
		if idx < len(nodes) && nodes[idx] != -1 {
			node.Right = &TreeNode{Val: nodes[idx]}
			queue = append(queue, node.Right)
		}
		idx++
	}
	return root

}

// PrintLevelOrder prints the tree in level order (for testing)
func PrintLevelOrder(root *TreeNode) {
	if root == nil {
		return
	}
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		if node != nil {
			fmt.Print(node.Val, " ")
			queue = append(queue, node.Left, node.Right)
		} else {
			fmt.Print("nil ")
		}
	}
	fmt.Println()
}
