/*
Given an array arr of integers, check if there exist two indices i and j such that :

	i != j
	0 <= i, j < arr.length
	arr[i] == 2 * arr[j]

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
*/
package main

import (
	"fmt"
)

func checkIfExist(arr []int) bool {
	n := len(arr)

	// Create a map to store each number as a key and its index as the value.
	// This helps us efficiently check for the existence of numbers.
	seen := make(map[int]int, n)

	// Populate the map with all numbers in the array.
	for i, num := range arr {
		seen[num] = i
	}

	// Iterate through the array to check if the double of the current number exists.
	for i, num := range arr {
		double := num * 2 // Calculate the double of the current number.

		// Check if the double exists in the map.
		// Additionally, ensure the indices are not the same to avoid false positives.
		if idx, exists := seen[double]; exists && idx != i {
			return true // Return true if a valid pair is found.
		}
	}

	// Return false if no such pair exists.
	return false
}

/*
func checkIfExist(arr []int) bool {

		n := len(arr)
		binarySearch := func(num int) (bool, int) {
			left, right := 0, n-1

			for left <= right {
				mid := left + (right-left)/2

				if arr[mid] == num {
					return true, mid
				} else if arr[mid] > num {
					right = mid - 1
				} else {
					left = mid + 1
				}
			}

			return false, -1
		}
		sort.Ints(arr)
		fmt.Println(arr)
		for i := 0; i < n; i++ {
			val := arr[i] * 2
			fmt.Printf("i = %v: %v - searching for %v\n", i, arr[i], val)
			found, idx := binarySearch(val)
			if found && idx != i {
				return true
			}
		}

		return false
	}
*/
func main() {
	var arr = []int{10, 2, 5, 3}
	fmt.Println(checkIfExist((arr)))
}
