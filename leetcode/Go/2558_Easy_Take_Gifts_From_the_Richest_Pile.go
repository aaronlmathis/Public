/*
You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

Choose the pile with the maximum number of gifts.
If there is more than one pile with the maximum number of gifts, choose any.
Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
Return the number of gifts remaining after k seconds.

Example 1:
Input: gifts = [25,64,9,4,100], k = 4
Output: 29
Explanation:
The gifts are taken in the following way:
- In the first second, the last pile is chosen and 10 gifts are left behind.
- Then the second pile is chosen and 8 gifts are left behind.
- After that the first pile is chosen and 5 gifts are left behind.
- Finally, the last pile is chosen again and 3 gifts are left behind.
The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.

Example 2:
Input: gifts = [1,1,1,1], k = 4
Output: 4
Explanation:
In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile.
That is, you can't take any pile with you.
So, the total gifts remaining are 4.
*/
package main

import (
	"fmt"
	"math"
)

// maxHeap represents a max-heap structure that maintains the heap property
// where the largest element is at the root.
type maxHeap struct {
	items []maxHeapItem // Slice to store heap elements
}

// maxHeapItem represents an item in the heap, which contains the number of gifts in a pile.
type maxHeapItem struct {
	gifts int // Number of gifts in this item
}

// push adds a new item to the heap and restores the max-heap property.
func (mh *maxHeap) push(gifts int) {
	// Append the new item to the end of the heap
	mh.items = append(mh.items, maxHeapItem{gifts: gifts})
	// Restore the heap property by bubbling up the new item
	mh.bubbleUp(len(mh.items) - 1)
}

// pop removes and returns the root (maximum element) of the heap.
// It replaces the root with the last element, removes the last element,
// and restores the max-heap property by bubbling down.
func (mh *maxHeap) pop() int {
	// Get the value of the root (maximum element)
	root := mh.items[0].gifts
	// Replace the root with the last element
	mh.items[0] = mh.items[len(mh.items)-1]
	// Remove the last element
	mh.items = mh.items[:len(mh.items)-1]
	// Restore the heap property by bubbling down from the root
	mh.bubbleDown(0)
	// Return the original root value
	return root
}

// bubbleUp moves an element at the given index up the heap until the max-heap
// property is restored. This happens if the current element is larger than its parent.
func (mh *maxHeap) bubbleUp(index int) {
	for index > 0 {
		// Calculate the parent index
		parent := (index - 1) / 2
		// If the parent is larger than or equal to the current element, stop
		if mh.items[parent].gifts >= mh.items[index].gifts {
			break
		}
		// Swap the current element with its parent
		mh.items[parent], mh.items[index] = mh.items[index], mh.items[parent]
		// Move up to the parent's index
		index = parent
	}
}

// bubbleDown moves an element at the given index down the heap until the max-heap
// property is restored. This happens by swapping it with the larger of its two children.
func (mh *maxHeap) bubbleDown(index int) {
	for {
		// Calculate the indices of the left and right children
		left := 2*index + 1
		right := 2*index + 2
		largest := index // Assume the current index is the largest

		// Check if the left child exists and is larger than the current element
		if left < len(mh.items) && mh.items[left].gifts > mh.items[largest].gifts {
			largest = left
		}

		// Check if the right child exists and is larger than the current largest
		if right < len(mh.items) && mh.items[right].gifts > mh.items[largest].gifts {
			largest = right
		}

		// If the largest is still the current index, the heap property is satisfied
		if largest == index {
			break
		}

		// Swap the current element with the larger child
		mh.items[index], mh.items[largest] = mh.items[largest], mh.items[index]

		// Move down to the larger child's index
		index = largest
	}
}

// newMaxHeap creates a new max-heap and populates it with the given items.
func newMaxHeap(items []int) *maxHeap {
	mh := &maxHeap{
		items: make([]maxHeapItem, 0),
	}
	// Add each item to the heap, maintaining the max-heap property
	for _, gift := range items {
		mh.push(gift)
	}
	return mh
}

// sumSlice calculates the sum of the `gifts` field for all items in the slice.
func sumSlice(sl []maxHeapItem) int {
	sum := 0
	for _, num := range sl {
		sum += num.gifts
	}
	return sum
}

// pickGifts simulates the process of taking gifts from piles for `k` seconds.
// It returns the total number of gifts remaining in the piles after the process.
func pickGifts(gifts []int, k int) int64 {
	// Create a max-heap from the given gifts
	pq := newMaxHeap(gifts)
	// Perform the operation `k` times
	for k > 0 {
		// Remove the largest pile of gifts
		g := pq.pop()
		// Add back the floor of the square root of the removed pile
		pq.push(int(math.Floor(math.Sqrt(float64(g)))))
		k--
	}
	// Calculate the total number of gifts remaining in the heap
	return int64(sumSlice(pq.items))
}

func main() {
	gifts := []int{25, 64, 9, 4, 100}
	k := 4
	fmt.Printf("Example 1: %v\n", pickGifts(gifts, k))
}
