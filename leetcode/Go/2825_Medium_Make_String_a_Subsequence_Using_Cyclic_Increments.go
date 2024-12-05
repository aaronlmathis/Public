/*
"""
You are given two 0-indexed strings str1 and str2.

In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.

Note: A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.

Example 1:
Input: str1 = "abc", str2 = "ad"
Output: true
Explanation: Select index 2 in str1.
Increment str1[2] to become 'd'.
Hence, str1 becomes "abd" and str2 is now a subsequence. Therefore, true is returned.

Example 2:
Input: str1 = "zc", str2 = "ad"
Output: true
Explanation: Select indices 0 and 1 in str1.
Increment str1[0] to become 'a'.
Increment str1[1] to become 'd'.
Hence, str1 becomes "ad" and str2 is now a subsequence. Therefore, true is returned.

Example 3:
Input: str1 = "ab", str2 = "d"
Output: false
Explanation: In this example, it can be shown that it is impossible to make str2 a subsequence of str1 using the operation at most once.
Therefore, false is returned.

	def canMakeSubsequence(self, str1: str, str2: str) -> bool:
*/
package main

import "fmt"

func canMakeSubsequence(str1 string, str2 string) bool {
	i, n := 0, len(str2)
	for _, c := range str1 {
		d := byte('a')
		if c != 'z' {
			d = byte(c + 1)
		}
		if i < n && (str2[i] == byte(c) || str2[i] == d) {
			i++
		}
	}
	return i == n
}

/*
func canMakeSubsequence(str1 string, str2 string) bool {
	// Set s1, s2 to the length of str1, str2
	s1, s2 := len(str1), len(str2)

	// Quick exit: If s2 is longer than s1, then there are not enough characters in s1 to make a subsequence that equals s2.
	if s2 > s1 {
		return false
	}

	// If both s1 and s2 are the same length, we can iterate through using one loop, checking 3 different conditions.
	if s1 == s2 {
		for i := 0; i < s1; i++ {
			// If there is an 'a' in str2 and a 'z' in str1 (since z->a) continue
			if str2[i] == 'a' && str1[i] == 'z' {
				continue
				// If str1[i] is equal to str2[i] (we don't have to make a shift)
			} else if str1[i] == str2[i] {
				continue
				//if the above two aren't true (we didn't continue the loop) then the unicode code of str1 minus the unicode code of str1 must be 1.
				// If it is not, then you can't make a valid subsequence from s1 that equals s2.
			} else if str2[i]-str1[i] != 1 {
				return false
			}
		}
		// If the loop finishes without returning False, then it is possible to make a subsequence, return true
		return true
	}
	// slice to track letters that are in str2 but not str1
	letters := []byte{}

	// Iterate through str2, if a character is not in str1, append it to letters
	for i := 0; i < s2; i++ {
		char := str2[i]
		if !containsByte(str1, char) {
			letters = append(letters, char)
		}
	}
	// c is a counter that tracks valid shift operations, you need c to equal the length of letters
	// Since letters is full of characters that are in str2 but not in str1, you need to have a shiftable char in str1 for every char in letters.
	c := 0

	// Iterate through letters
	for i := 0; i < len(letters); i++ {
		// Is the character thats made from the unicode code of char minus 1 (a shift) found in str1, IF so, this is valid shift, increase counter
		if containsByte(str1, letters[i]-1) {
			c++
		}
		//  Is char an 'a' and 'z' is in str1? A valid shift.. increase counter.
		if letters[i] == 'a' && containsByte(str1, 'z') {
			c++
		}
	}
	//  Return whether a valid shift was found for every letter in letters.
	return c == len(letters)
}

// Helper function to check if a byte exists in a string
func containsByte(s string, b byte) bool {
	for i := 0; i < len(s); i++ {
		if s[i] == b {
			return true
		}
	}
	return false
}
*/
func main() {
	strs := [][]string{
		{"abc", "ad"},
		{"zc", "ad"},
		{"ab", "d"},
	}
	for i := 0; i < len(strs); i++ {
		fmt.Printf("Example: %v\n", i+1)
		fmt.Println(canMakeSubsequence(strs[i][0], strs[i][1]))
		fmt.Println()
	}
}
