package main

import "fmt"

func main() {
	var n, a, b int
	fmt.Scanln(&n)
	for ; n > 0; n-- {
		fmt.Scanln(&a, &b)
		a %= 10
		p := a
		b = (b - 1) % 4
		for ; b > 0; b-- {
			p = (p * a) % 10
		}
		if p == 0 {
			p = 10
		}
		fmt.Println(p)
	}
}
