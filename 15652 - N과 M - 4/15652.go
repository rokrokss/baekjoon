package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	wr   = bufio.NewWriter(os.Stdout)
	n, m int
	r    []int
)

func solve(i, min int) {
	if i == m {
		for _, k := range r {
			wr.WriteByte(byte(k) + '0')
			wr.WriteByte(' ')
		}
		wr.WriteByte('\n')
		return
	}
	for j := min; j <= n; j++ {
		r[i] = j
		solve(i+1, j)
	}
}

func main() {
	fmt.Scan(&n, &m)
	r = make([]int, m)
	solve(0, 1)
	wr.Flush()
}
