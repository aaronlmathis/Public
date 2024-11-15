/*
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
*/

package main

import (
	"fmt"
	"strings"
)

func fullJustify(words []string, maxWidth int) []string {
	// Initialize starting variables
	var output []string               // Problem Answer
	counts := make([]int, len(words)) // Create slice of letter counts where counts[i] refers to words[i]
	for i, word := range words {
		counts[i] = len(word)
	}

	var idx int
	n := len(words)

	// Build the current line up to the maxWidth
	for idx < n {
		line := []string{} // Initialize an empty slice for storing words
		lineLength, numWords, numGaps, diff := 0, 0, 0, 0
		endLine := false

		for idx < n && (lineLength+counts[idx]+numWords) <= maxWidth {
			lineLength += counts[idx]
			line = append(line, words[idx])
			idx += 1
			numWords += 1
			if idx == n {
				endLine = true
			}
		}

		// Calculate remaining spaces to fill the line
		diff = maxWidth - lineLength
		if numWords > 1 {
			numGaps = numWords - 1
		} else {
			numGaps = 1
		}
		var justifiedLine string
		if endLine == true {
			// For the last line, left-align with single spaces between words and remaining spaces at the end
			if numWords == 1 {
				// Only one word: add all remaining spaces to the end
				justifiedLine = line[0] + strings.Repeat(" ", diff)
			} else {
				// Multiple words: single space between words, remaining spaces at the end
				justifiedLine = strings.Join(line, " ") + strings.Repeat(" ", diff-(numWords-1))
			}
		} else {
			// For Justified lines
			spacePerGap := diff / numGaps
			extraSpaces := diff % numGaps

			// Build gaps with even distribution, starting extra spaces from the left
			// Initialize the gaps slice with numGaps elements
			gaps := make([]string, numGaps)
			for i := 0; i < numGaps; i++ {
				if i < extraSpaces {
					gaps[i] = strings.Repeat(" ", spacePerGap+1) // Add an extra space for the first `extraSpaces` gaps
				} else {
					gaps[i] = strings.Repeat(" ", spacePerGap) // Standard spacePerGap for the rest
				}
			}
			var justifiedLineBuilder strings.Builder
			for i, word := range line {
				justifiedLineBuilder.WriteString(word)
				if i < len(gaps) { // Append gap if it's not the last word
					justifiedLineBuilder.WriteString(gaps[i])
				}
			}
			justifiedLine = justifiedLineBuilder.String()
		}
		output = append(output, justifiedLine)
	}
	return output
}

func main() {
	words := []string{"This", "is", "an", "example", "of", "text", "justification."}
	maxWidth := 16
	output := fullJustify(words, maxWidth)
	for v := range output {
		fmt.Println(output[v])
	}
}
