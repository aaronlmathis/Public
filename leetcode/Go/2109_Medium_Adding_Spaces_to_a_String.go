/*
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added.

Example 1:

Input: s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
Output: "Leetcode Helps Me Learn"
Explanation:
The indices 8, 13, and 15 correspond to the underlined characters in "LeetcodeHelpsMeLearn".
We then place spaces before those characters.
Example 2:

Input: s = "icodeinpython", spaces = [1,5,7,9]
Output: "i code in py thon"
Explanation:
The indices 1, 5, 7, and 9 correspond to the underlined characters in "icodeinpython".
We then place spaces before those characters.
Example 3:

Input: s = "spacing", spaces = [0,1,2,3,4,5,6]
Output: " s p a c i n g"
Explanation:
We are also able to place spaces before the first character of the string.
*/
package main

import (
	"fmt"
)

func addSpaces(s string, spaces []int) string {
    // Preallocate a slice of bytes with the exact length needed:
    // len(s) for the characters in the string + len(spaces) for the spaces to be added.
    answer := make([]byte, len(s)+len(spaces))

    p, n := 0, len(spaces) // `p` is the pointer for `spaces`, `n` is the number of spaces.
    a := 0                 // `a` is the pointer for the `answer` array.

    // Iterate over the input string `s` character by character.
    for i := 0; i < len(s); i++ {
        // Check if the current index `i` matches the next space position in `spaces`.
        if i == spaces[p] {
            answer[a] = ' ' // Add a space at the current position in `answer`.
            if p < n-1 {    // Move to the next space index if there are more spaces left.
                p++
            }
            a++ // Increment the pointer for the `answer` array to account for the space.
        }

        // Add the current character from `s` to the `answer` array.
        answer[a] = s[i]
        a++ // Move the pointer forward in the `answer` array.
    }

    // Convert the `answer` byte slice to a string and return the result.
    return string(answer)
}


	/*
		p, n := 0, len(spaces)
		answer := []byte{}
		for idx, char := range []byte(s) {
			if idx == spaces[p] {
				answer = append(answer, ' ')
				if p < n-1 {
					p++
				}
			}
			answer = append(answer, char)
		}

		return string(answer[:])

			index, answer := 0, []string{}
			for i := 0; i < len(spaces); i++ {
				answer = append(answer, s[index:spaces[i]])
				index = spaces[i]
			}
			answer = append(answer, s[index:])

			return strings.Join(answer, " ")
	*/
}

func main() {
	var s = []string{
		"LeetcodeHelpsMeLearn",
		"icodeinpython",
		"spacing",
	}
	var spaces = [][]int{
		{8, 13, 15},
		{1, 5, 7, 9},
		{0, 1, 2, 3, 4, 5, 6},
	}
	for i := 0; i < len(s); i++ {
		fmt.Printf("Example %v\n", i+1)
		fmt.Printf("%v\n", addSpaces(s[i], spaces[i]))
	}
}
