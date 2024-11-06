/*
Given a string word, compress it using the following algorithm:

Begin with an empty string comp. While word is not empty, use the following operation:
Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
Append the length of the prefix followed by c to comp.
Return the string comp.

Example 1:
Input: word = "abcde"
Output: "1a1b1c1d1e"
Explanation:
Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.
For each prefix, append "1" followed by the character to comp.

Example 2:
Input: word = "aaaaaaaaaaaaaabb"
Output: "9a5a2b"
Explanation:
Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.
For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
For prefix "aaaaa", append "5" followed by "a" to comp.
For prefix "bb", append "2" followed by "b" to comp.
*/

package main

import (
	"fmt"
	"strings"
)

func compressedString(word string) string {

	// If word is null, return empty string
	if len(word) == 0 {
		return ""
	}

	// Declar currentChar (set to first char in word)
	// Declare charCount, starting at 0
	// Declare comp value for return string using string builder

	var currentChar byte = word[0]
	var charCount int
	var comp strings.Builder

	// Iterate through the word

	for i := 0; i < len(word); i++ {
		// If word[i] == currentChar, increase count. If count = 9, add count+char to compressed string
		if word[i] == currentChar {
			charCount++

			if charCount == 9 {
				comp.WriteString(fmt.Sprintf("%d%c", charCount, currentChar))
				charCount = 0
			}
		} else {
			// word[i] != current char
			//if char count > 0, add count and char to compressed string
			if charCount > 0 {
				comp.WriteString(fmt.Sprintf("%d%c", charCount, currentChar))
			}
			//Set currentChar to word[i] and set count to 1
			currentChar = word[i]
			charCount = 1
		}
	}

	// Ad the Final character's segment
	if charCount > 0 {
		comp.WriteString(fmt.Sprintf("%d%c", charCount, currentChar))
	}

	return comp.String()
}

func main() {
	var word string = "aaaaaaaaaaaaaabb"
	fmt.Println(compressedString(word))
}
