package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	i := n
	for i > 1 {
		fmt.Printf(strings.Repeat(" ", n-i))
		fmt.Println(strings.Repeat("*", i*2-1))
		i--
	}
	for i <= n {
		fmt.Printf(strings.Repeat(" ", n-i))
		fmt.Println(strings.Repeat("*", i*2-1))
		i++
	}
}
