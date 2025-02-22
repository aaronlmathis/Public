package main

import "fmt"

// Define the struct with two int fields
type MyStruct struct {
	A int
	B int
}

func main() {
	// Initialize a slice of MyStruct using make
	stack := make([]MyStruct, 0)

	// Example list of integers
	numbers := []int{1, 2, 3, 4, 5, 6}

	// Populate the slice by grouping numbers into struct instances
	for i := 0; i < len(numbers)-1; i += 2 {
		stack = append(stack, MyStruct{A: numbers[i], B: numbers[i+1]})
	}

	// Print the stack
	for i, v := range stack {
		fmt.Printf("stack[%d]: A = %d, B = %d\n", i, v.A, v.B)
	}
}
