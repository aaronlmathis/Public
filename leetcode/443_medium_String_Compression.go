package main

import (
	"fmt"
	"strconv"
)

func compress(chars []byte) int {
	read, write := 0, 0
	for read < len(chars) {
		char := chars[read]
		count := 0

		for read < len(chars) && chars[read] == char {
			read += 1
			count += 1
		}
		chars[write] = char
		write += 1

		if count > 1 {
			for _, digit := range strconv.Itoa(count) {
				chars[write] = byte(digit)
				write += 1
			}
		}
	}
	return write
}

func main() {
	chars := []byte{'a', 'a', 'b', 'b', 'c', 'c', 'c'}
	fmt.Println(compress(chars))

}
