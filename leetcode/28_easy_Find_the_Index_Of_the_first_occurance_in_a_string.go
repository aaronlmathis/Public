/*
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

Constraints:
*/
package main

import (
	"fmt"
	"strings"
)

func strStr(haystack string, needle string) int {
	/*
	   Without Strings Package:

	   	h, n := len(haystack), len(needle)

	   	if n > h {
	   		return -1
	   	}

	   	for i := 0; i <= h-n; i++ {
	   		if haystack[i] == needle[0] {
	   			slice := haystack[i : i+n]
	   			if slice == needle {
	   				return i
	   			}
	   		}
	   	}

	   	return -1
	*/
	if len(needle) == 0 {
		return 0
	}

	return strings.Index(haystack, needle)
}

func main() {
	needle := "sad"
	haystack := "svdbutsad"

	fmt.Println(strStr(haystack, needle))
}
