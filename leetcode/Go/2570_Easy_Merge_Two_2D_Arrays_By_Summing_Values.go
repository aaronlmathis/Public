/*
You are given two 2D integer arrays nums1 and nums2.

nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.

Example 1:
Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]
Explanation: The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.

Example 2:
Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
Explanation: There are no common ids, so we just include each id with its value in the resulting list.

Constraints:
1 <= nums1.length, nums2.length <= 200
nums1[i].length == nums2[j].length == 2
1 <= idi, vali <= 1000
Both arrays contain unique ids.
Both arrays are in strictly ascending order by id.
*/
package main

import (
	"fmt"
	"sort"
)

func mergeArrays(nums1 [][]int, nums2 [][]int) [][]int {
	// Create hash map to track id: val
	valMap := make(map[int]int)
	// Iterate over nums1, adding each id:val
	for _, pair := range nums1 {
		valMap[pair[0]] = pair[1]
	}
	// Iterate over nums2,  sum the vals. If not, add the id:val
	for _, pair := range nums2 {
		valMap[pair[0]] += pair[1]
	}
	// Build array of id's so we can sort them. (maps don't guarantee order)
	ids := make([]int, 0, len(valMap))
	for id := range valMap {
		ids = append(ids, id)
	}
	sort.Ints(ids) // sort em'

	// Build answer array by iterating over id's and adding corresonding val from valMap.
	answer := make([][]int, 0)
	for _, id := range ids {
		answer = append(answer, []int{id, valMap[id]})
	}

	return answer
}

func main() {
	nums1 := [][]int{{1, 2}, {2, 3}, {4, 5}}
	nums2 := [][]int{{1, 4}, {3, 2}, {4, 1}}
	fmt.Println(mergeArrays(nums1, nums2))
}
