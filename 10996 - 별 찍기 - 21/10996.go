package main

import (
	"fmt"
	"strings"
)

func main() {
	var n int
	var l1, l2 string
	fmt.Scan(&n)
	if n == 1 {
		fmt.Println("*")
		return
	}
	l1 = strings.Repeat("* ", n/2)
	l2 = strings.Repeat(" *", n/2)
	if n%2 == 1 {
		l1 += "*"
	}
	for ; n > 0; n-- {
		fmt.Println(l1)
		fmt.Println(l2)
	}
}
