/*
You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
- Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.

Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.

Example 2:
Input: s = "cb34"
Output: ""
Explanation:
First, we apply the operation on s[2], and s becomes "c4".
Then we apply the operation on s[1], and s becomes "".

Constraints:
1 <= s.length <= 100
s consists only of lowercase English letters and digits.
The input is generated such that it is possible to delete all digits.
*/
package main

import (
	"fmt"
	"unicode"
)

func clearDigits(s string) string {
	// Initialize an empty slice of runes for the stack
	stack := make([]rune, 0)

	// Iterate over `s` checking if each character is a number.
	for _, char := range s {
		// If it is, pop the top of the stack (the item to the left)
		if unicode.IsDigit(char) {
			stack = stack[:len(stack)-1]
			// If it isn't, append the char to the stack
		} else {
			stack = append(stack, char)
		}
	}
	// Return the stack as a string
	return string(stack)
}

func main() {
	s := "cb34"
	fmt.Println(clearDigits(s))
}
