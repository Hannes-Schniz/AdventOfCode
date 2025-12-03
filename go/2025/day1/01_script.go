package main

import (
	"fmt"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	fmt.Println("###################### Test ######################")
	fmt.Println(part1("01_test.txt"))
	fmt.Println(part2("01_test.txt"))
	fmt.Println("###################### Input ######################")
	fmt.Println(part1("01_input.txt"))
	fmt.Println(part2("01_input.txt"))
}

func part1(filename string) int {
	dat, err := os.ReadFile(filename)
	check(err)
	//fmt.Println(string(dat))
	for index, element := range dat {
		println("Step " + strconv.Itoa(index) + ": ")
		first := rune(element)
		fmt.Println(first)
	}
	fmt.Println("<----------> Part1 <---------->")
	return -1
}
func part2(filename string) int {
	fmt.Println("<----------> Part2 <---------->")
	return -1
}
