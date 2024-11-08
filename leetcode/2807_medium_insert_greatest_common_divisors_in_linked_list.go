/*
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
*/
package main

import "fmt"

//Definition for singly-linked list.

type ListNode struct {
	Val  int
	Next *ListNode
}

func insertGreatestCommonDivisors(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}

	current := head

	for current != nil && current.Next != nil {
		newNode := ListNode{Val: gcd(current.Val, current.Next.Val)}
		newNode.Next = current.Next
		current.Next = &newNode
		current = newNode.Next
	}
	return head
}

func buildLinkedList(nums []int) *ListNode {
	if len(nums) == 0 {
		return nil
	}

	head := &ListNode{Val: nums[0]}
	current := head

	for _, num := range nums[1:] {
		current.Next = &ListNode{Val: num}
		current = current.Next
	}

	return head
}

func main() {
	nums := []int{18, 6, 10, 3}
	head := buildLinkedList(nums)

	// Print the linked list to verify
	current := head
	for current != nil {
		fmt.Printf("%d -> ", current.Val)
		current = current.Next
	}
	fmt.Println("nil")
	insertGreatestCommonDivisors(head)
	after := head
	for after != nil {
		fmt.Printf("%d -> ", after.Val)
		after = after.Next
	}
	fmt.Println("nil")
}
