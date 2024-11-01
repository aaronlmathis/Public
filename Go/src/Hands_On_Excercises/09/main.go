package main

import "fmt"

var age int = 32

const pi float32 = 3.14

func main() {
	name := "Aaron"

	fmt.Printf("Hi, my name is %v. I am %d years old and I'm obsessed with %v", name, age, pi)
	for i := 0; i < 21; i++ {
		if i%2 != 0 {
			continue
		}
		fmt.Println(i)
	}

	xi := []int{42, 24, 35, 65}

	for v := range xi {
		fmt.Println("ranging over a slice", v)
	}

	m := map[string]int{
		"Aaron": 42,
		"Kassi": 25,
	}

	for k, v := range m {
		fmt.Println("Ranging over map", k, v)
	}
}
