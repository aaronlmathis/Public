/*
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

Example 1:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]

Constraints:
1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
*/
package main

import "fmt"

func wordSubsets(words1 []string, words2 []string) []string {
	// Create a map to store the maximum frequency of each character in words2
	charFreq := make(map[rune]int)
	for _, word := range words2 {
		charCount := make(map[rune]int)
		for _, char := range word {
			charCount[char]++
		}
		for char, count := range charCount {
			if charFreq[char] < count {
				charFreq[char] = count
			}
		}
	}

	// Filter words1 to keep only those that contain all characters with the required frequency
	result := []string{}
	for _, word := range words1 {
		charCount := make(map[rune]int)
		for _, char := range word {
			charCount[char]++
		}
		isValid := true
		for char, freq := range charFreq {
			if charCount[char] < freq {
				isValid = false
				break
			}
		}
		if isValid {
			result = append(result, word)
		}
	}

	return result
}
func main() {
	words1 := []string{"amazon", "apple", "facebook", "google", "leetcode"}
	words2 := []string{"e", "o"}
	fmt.Println(wordSubsets(words1, words2))
}
