package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	i := 1
	for i < n {
		fmt.Println(strings.Repeat("*", i))
		i++
	}
	for i > 0 {
		fmt.Println(strings.Repeat("*", i))
		i--
	}
}
