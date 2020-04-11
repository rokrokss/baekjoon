package main

import "fmt"

func main() {
	var a, b, c, d, e int
	fmt.Scan(&a, &b, &c, &d, &e)
	if a > b {
		a = b
	}
	if a > c {
		a = c
	}
	if d > e {
		d = e
	}
	fmt.Println(a + d - 50)
}
