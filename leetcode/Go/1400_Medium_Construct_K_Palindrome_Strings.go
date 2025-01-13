/*
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.



Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
*/

package main

import (
	"fmt"
)

func canConstruct(s string, k int) bool {
	n := len(s)
	if n < k {
		return false
	}
	if n == k {
		return true
	}
	letterCounts := make([]int, 26)
	for _, char := range s {
		letterCounts[char-'a']++
	}
	oddCount := 0
	for _, count := range letterCounts {
		if count%2 != 0 {
			oddCount++
		}
	}
	if oddCount > k {
		return false
	}

	return true
}

func main() {
	s := "annabelle"
	k := 2
	fmt.Println(canConstruct(s, k))
}
