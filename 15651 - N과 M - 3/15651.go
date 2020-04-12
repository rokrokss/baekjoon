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

func solve(i int) {
	if i == m {
		for _, k := range r {
			wr.WriteByte(byte(k) + '0')
			wr.WriteByte(' ')
		}
		wr.WriteByte('\n')
		return
	}
	for j := 1; j <= n; j++ {
		r[i] = j
		solve(i + 1)
	}
}

func main() {
	fmt.Scan(&n, &m)
	r = make([]int, m)
	solve(0)
	wr.Flush()
}
