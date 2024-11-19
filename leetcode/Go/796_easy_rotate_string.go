/*
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
*/
package main

func rotateString(s string, goal string) bool {
    // Check if lengths are equal
    if len(s) != len(goal) {
        return false
    }
    
    // Concatenate s with itself and use strings.Contains to check if goal is a substring
    return strings.Contains(s+s, goal)
}
func main(){

	s := "abcde"
	goal := "cdeab" 
	fmt.Println(rotateString((s, goal)))
}