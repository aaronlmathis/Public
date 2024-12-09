/*
Given a string s, find the length of the longest
substring

	without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
*/
package main

import "fmt"

func lengthOfLongestSubstring(s string) int {
	var n int = len(s)

	// Quick exit if s is empty.
	if n == 0 {
		return 0
	}
	// Left pointer, start of window and maxLength of string
	var start, maxLength int

	// map byte to empty struct for frequency checks
	seen := make(map[byte]int)

	// Iterate through s, byte by byte
	for end := 0; end < n; end++ {
		// if character already exists in seen, set start to the byte after where it was seen before
		if lastIndex, exists := seen[s[end]]; exists && lastIndex >= start {
			start = lastIndex + 1
		}

		// map current byte
		seen[s[end]] = end

		// if current window length is greater than maxlength, set maxlength to it
		if end-start+1 > maxLength {
			maxLength = end - start + 1
		}

	}
	//return maxLength
	return maxLength
}

func main() {
	var s string = "bbbbbb"
	fmt.Println(lengthOfLongestSubstring((s)))
}
