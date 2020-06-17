package main

import "fmt"

func main() {
	var t int
	fmt.Scan(&t)
	memo := make([]int, 101)
	memo[1] = 1
	memo[2] = 1
	memo[3] = 1
	memo[4] = 2
	memo[5] = 2
	for i := 6; i <= 100; i++ {
		memo[i] = memo[i-1] + memo[i-5]
	}
	var n int
	for i := 0; i < t; i++ {
		fmt.Scan(&n)
		fmt.Println(memo[n])
	}
}
