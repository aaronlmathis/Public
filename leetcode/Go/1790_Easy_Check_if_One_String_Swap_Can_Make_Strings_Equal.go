/*
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
*/
package main

import "fmt"

func areAlmostEqual(s1 string, s2 string) bool {
	if s1 == s2 {
		return true
	}
	n := len(s1)

	type Pair[a, b any] struct {
		A a
		B b
	}
	diffs := []Pair[byte, byte]{}

	for i := 0; i < n; i++ {
		if s1[i] != s2[i] {
			pair := Pair[byte, byte]{s1[i], s2[i]}
			diffs = append(diffs, pair)
		}
		if len(diffs) > 2 {
			return false
		}
	}

	if len(diffs) == 1 {
		return false
	}
	if diffs[0].A == diffs[1].B && diffs[0].B == diffs[1].A {
		return true
	}

	return false
}

func main() {
	s1 := "bank"
	s2 := "kanb"
	fmt.Println(areAlmostEqual(s1, s2))
}
