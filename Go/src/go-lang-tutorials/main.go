package main

import (
	"fmt"
	"strings"
)

func main() {

	greeting := "Hello there friends!"

	fmt.Println(strings.Contains(greeting, "Hello"))

	// Slices (size can change)
	// var scores = []int{100, 50, 60}
	// scores[2] = 25
	// scores = append(scores, 85)

	// fmt.Println(scores, len(scores))

	// // Slice Ranges
	// rangeOne := scores[1:3]
	// rangeTwo := scores[2:]
	// rangeThree := scores[:3]
	// fmt.Println(rangeOne, rangeTwo, rangeThree)

	// Arrays (size can't change)
	// var ages [3]int = [3]int{20, 25, 30}
	// var ages = [3]int{20, 25, 30}

	// names := [4]string{"yoshi", "mario", "peach", "bowser"}

	// fmt.Println(ages, len(ages))
	// fmt.Println(names, len(names))

	// age := 35
	// name := "Aaron"

	// fmt.Println("my age is", age, "and my name is", name)

	// // formatted string - Printf ( formatted string)
	// fmt.Printf("my age is %v and my name is %v \n", age, name)
	// fmt.Printf("my age is %q and my name is %q \n", age, name)
	// fmt.Printf("age is of type %T \n", age)
	// fmt.Printf("you scored %0.1f points \n", 225.55)

	// // Springf(save formatted strings)
	// var str = fmt.Sprintf("my age is %v and my name is %v \n", age, name)
	// fmt.Println(str)

	//Strings

	// var nameOne string = "Mario"
	// var nameTwo = "Luigi"
	// var nameThree string

	// fmt.Println(nameOne, nameTwo, nameThree)

	// nameOne = "peach"
	// nameThree = "bowser"

	// fmt.Println(nameOne, nameTwo, nameThree)

	// nameFour := "yoshi"

	// fmt.Println(nameFour)

	// ints
	// var ageOne int = 20
	// var ageTwo = 30
	// ageThree := 40

	// fmt.Println(ageOne, ageTwo, ageThree)

	// // bits and memory
	// var numOne int8 = 25
	// var numTwo int8 = -128
	// var numThree uint8 = 255

	// var scoreOne float32 = 25.98
	// var scoreTwo float64 = 12312311251262713572375547345654.5
	// scoreThree := 1.5

}
