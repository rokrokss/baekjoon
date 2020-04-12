package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	n, m int
	r    []int
	wr   = bufio.NewWriter(os.Stdout)
)

func solve(idx, max int) {
	if idx == m {
		for _, k := range r {
			wr.WriteByte(byte(k) + '0')
			wr.WriteByte(' ')
		}
		wr.WriteByte('\n')
		return
	}
	for j := max + 1; j <= n; j++ {
		r[idx] = j
		solve(idx+1, j)
	}
	return
}

func main() {
	fmt.Scan(&n, &m)
	r = make([]int, m)
	solve(0, 0)
	wr.Flush()
}
