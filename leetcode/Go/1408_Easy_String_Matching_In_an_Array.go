/*
Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

# A substring is a contiguous sequence of characters within a string

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.
*/
package main

import (
	"fmt"
	"strings"
)

func stringMatching(words []string) []string {
	// Declare answer slice
	answer := []string{}

	// Concatinate words into a string, this makes the compare() function only need to be run against one thing instead of several.
	sentence := strings.Join(words, " ")

	// Iterate through words, checking if the count of word in sentence is > 1 and appending word to answer if so
	for _, word := range words {
		if strings.Count(sentence, word) > 1 {
			answer = append(answer, word)
		}
	}

	return answer

}

func main() {
	words := []string{"leetcode", "et", "code"}
	fmt.Println(stringMatching(words))
}
