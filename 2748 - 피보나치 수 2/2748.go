package main

import (
	"fmt"
)

var (
	memo []int
	n    int
)

func fibo(i int) int {
	if i == 0 || memo[i] != 0 {
		return memo[i]
	}
	memo[i] = fibo(i-1) + fibo(i-2)
	return memo[i]
}

func main() {
	fmt.Scan(&n)
	memo = make([]int, 91)
	memo[0] = 0
	memo[1] = 1
	fmt.Println(fibo(n))
}
