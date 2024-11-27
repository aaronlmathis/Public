/*
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
*/
package main

import "fmt"

func canConstruct(ransomNote string, magazine string) bool {
	charCount := make(map[rune]int)
	for _, char := range magazine {
		charCount[char]++
	}

	for _, char := range ransomNote {
		if charCount[char] > 0 {
			charCount[char]--
		} else {
			return false
		}
	}
	return true
}
func main() {
	var ransomNote string = "aab"
	var magazine string = "baa"
	fmt.Println(canConstruct(ransomNote, magazine))
}
