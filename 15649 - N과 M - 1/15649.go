package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	n, m  int
	r     []int
	check []bool
	wr    = bufio.NewWriter(os.Stdout)
)

func dfs(i int) {
	if i == m {
		for _, k := range r {
			wr.WriteByte(byte(k) + '0')
			wr.WriteByte(' ')
		}
		wr.WriteByte('\n')
		return
	}
	for j := 1; j <= n; j++ {
		if check[j] {
			continue
		}
		r[i] = j
		check[j] = true
		dfs(i + 1)
		check[j] = false
	}
}

func main() {
	fmt.Scan(&n, &m)
	r = make([]int, m)
	check = make([]bool, n+1)
	dfs(0)
	wr.Flush()
}
