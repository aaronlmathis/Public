/*
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
*/
package main

import "fmt"

// Backtrack function that has 2 options, add an open or add a closed parenthesis

func generateParentheses(n int) []string {
	result := []string{}

	// Define the backtracking function as an inner function
	var backtrack func(current string, open, close int)
	backtrack = func(current string, open, close int) {
		// Base case: if the current combination has the correct length
		if len(current) == 2*n {
			result = append(result, current)
			return
		}

		// Option 1: Add an opening parenthesis if we haven't reached the limit
		if open < n {
			backtrack(current+"(", open+1, close)
		}

		// Option 2: Add a closing parenthesis if it forms a valid sequence
		if close < open {
			backtrack(current+")", open, close+1)
		}
	}

	// Initial call to the backtracking function
	backtrack("", 0, 0)
	return result
}

func main() {
	n := 3
	fmt.Println(generateParentheses(n))
}
