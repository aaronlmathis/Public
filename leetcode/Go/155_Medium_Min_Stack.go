/*
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
*/
package main

type MinStack struct {
	items    []int
	minStack []int
}

func Constructor() MinStack {
	return MinStack{
		items:    []int{},
		minStack: []int{},
	}
}

func (this *MinStack) Push(val int) {
	this.items = append(this.items, val)
	if len(this.minStack) == 0 || val <= this.minStack[len(this.minStack)-1] {
		this.minStack = append(this.minStack, val)
	}
}

func (this *MinStack) Pop() {
	if len(this.items) == 0 {
		return
	}
	if this.items[len(this.items)-1] == this.minStack[len(this.minStack)-1] {
		this.minStack = this.minStack[:len(this.minStack)-1]
	}
	this.items = this.items[:len(this.items)-1]
}

func (this *MinStack) Top() int {
	if len(this.items) == 0 {
		panic("stack is empty")
	}
	return this.items[len(this.items)-1]
}

func (this *MinStack) GetMin() int {
	if len(this.minStack) == 0 {
		panic("minStack is empty")
	}
	return this.minStack[len(this.minStack)-1]
}
