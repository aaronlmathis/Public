/*
You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].

Example 2:
Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation: Every string satisfies the conditions, so we return [3,2,1].
*/
package main

import "fmt"

func isVowel(c byte) bool {
	switch c {
	case 'a', 'e', 'i', 'o', 'u',
		'A', 'E', 'I', 'O', 'U':
		return true
	}
	return false
}

func vowelStrings(words []string, queries [][]int) []int {
	ans := make([]int, len(queries))
	n := len(words)
	pf := make([]int, n+1)

	for i := 0; i < n; i++ {
		word := words[i]
		if len(word) > 0 {
			if isVowel(word[0]) && isVowel(word[len(word)-1]) {
				pf[i+1] = pf[i] + 1
				continue
			}
		}
		pf[i+1] = pf[i]
	}

	for i, q := range queries {
		left, right := q[0], q[1]
		ans[i] = pf[right+1] - pf[left]
	}

	return ans
}

func main() {
	words := []string{"aba", "bcb", "ece", "aa", "e"}
	queries := [][]int{{0, 2}, {1, 4}, {1, 1}}
	fmt.Println(vowelStrings(words, queries))
}
