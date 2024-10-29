package main

import "fmt"

func main() {
	a, b, c := "hello", 12, 25.5

	fmt.Printf("%v is of %T type\n", a, a)
	fmt.Printf("%v is of %T type\n", b, b)
	fmt.Printf("%v is of %T type\n", c, c)
}
