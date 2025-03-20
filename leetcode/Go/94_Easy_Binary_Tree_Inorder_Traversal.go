/*
Given the root of a binary tree, return the inorder traversal of its nodes' values.



Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]
Explanation:

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]
Explanation:

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
*/
/**
 * Definition for a binary tree node.*/
package main

import (
	"Go/utils"
	"fmt"
)

func inorderTraversal(root *utils.TreeNode) []int {
	var results []int
	return inorderTraversalHelper(results, root)
}

func inorderTraversalHelper(results []int, root *utils.TreeNode) []int {
	if root != nil {
		results = inorderTraversalHelper(results, root.Left)
		results = append(results, root.Val)
		results = inorderTraversalHelper(results, root.Right)
	}
	return results
}

func main() {
	nodes := []int{1, 2, 3, 4, 5, -1, 8, -1, -1, 6, 7, 9}
	root := utils.BuildBinaryTree(nodes)
	fmt.Println(inorderTraversal(root))
}
