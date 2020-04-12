package main

import (
	"fmt"
)

var (
	n, ans int
	col    []int
)

func solve(i int) {
	if i == n {
		ans++
		return
	}
	for j := 0; j < n; j++ {
		var k int
		for ; k < i; k++ {
			if col[k] == j || col[k]-j == i-k || j-col[k] == i-k {
				break
			}
		}
		if k == i {
			col[i] = j
			solve(i + 1)
		}
	}
}

func main() {
	fmt.Scan(&n)
	col = make([]int, n)
	solve(0)
	fmt.Println(ans)
}
