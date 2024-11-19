/*
A fancy string is a string where no three consecutive characters are equal.
Given a string s, delete the minimum possible number of characters from s to make it fancy.
Return the final string after the deletion. It can be shown that the answer will always be unique.

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
*/
package main

import "fmt"

func makeFancyString(s string) string {

	// Initialize variable to count character length of string
	var strLength int = len(s)

	// Check to see if string length is less than 3.
	if strLength < 3 {
		return s
	}

	var resultStr []rune // Initialize rune slice for answer
	var currentChar rune // Initialilze a rune for current char.
	var charCount int    // Initialize an int for the char count

	// Iterate through characters in the string
	for _, char := range s {
		// If char equals current char, check if char count is 2. If so, continue loop and do nothing
		if char == currentChar {
			if charCount == 2 {
				continue
			}
			charCount += 1 // Char count wasn't 2, so increase it by one.
		} else {
			// The char doesn't equal current char, so set current char to char and increase count.
			currentChar = char
			charCount = 1
		}

		// Append char to answer rune slice
		resultStr = append(resultStr, char)
	}
	
	// Return answer as String
	return string(resultStr)
}

func main() {
	var s string = "aaaabbaaaa"
	fmt.Println(makeFancyString(s))
}
