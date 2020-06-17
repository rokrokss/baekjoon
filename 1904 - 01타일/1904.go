package main

import "fmt"

var (
	n int
)

func main() {
	fmt.Scan(&n)
	memo := make([]int, 1000001)
	memo[0] = 0
	memo[1] = 1
	memo[2] = 2
	for i := 3; i <= n; i++ {
		memo[i] = (memo[i-1] + memo[i-2]) % 15746
	}
	fmt.Println(memo[n])
}
