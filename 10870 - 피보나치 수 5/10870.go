package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	a, b := 0, 1
	for i := 0; i < n; i++ {
		a, b = b, a+b
	}
	fmt.Println(a)
}
