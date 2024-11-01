package main

import (
	"fmt"
	"math/rand"
	"sort"
)

func init() {
	fmt.Println("This is where initialization for my program occurs")
}

func binarySearch(targetNum int, dataset []int) bool {
	left, right := 0, len(dataset)-1

	for left <= right {
		mid := (left + right) / 2
		if dataset[mid] > targetNum {
			right = mid - 1
		} else if dataset[mid] < targetNum {
			left = mid + 1
		} else {
			return true
		}

	}
	return false
}
func main() {
	var targetNum int = 2
	var candidates []int

	for i := 0; i < 100; i++ {
		candidates = append(candidates, rand.Intn(100))
	}
	sort.Ints(candidates)
	fmt.Println(candidates)
	fmt.Println(targetNum)
	fmt.Println(binarySearch(targetNum, candidates))

}
