package main

import (
	"bytes"
	"fmt"
)

var r [][]byte

func draw(x, y int) byte {
	if x == 0 {
		return '*'
	} else if x%3 == 1 && y%3 == 1 {
		return ' '
	} else {
		return draw(x/3, y/3)
	}
}

func main() {
	var n int
	fmt.Scan(&n)
	r = make([][]byte, n)
	for i := range r {
		r[i] = bytes.Repeat([]byte{' '}, n)
	}
	for y := 0; y < n; y++ {
		for x := 0; x < n; x++ {
			r[x][y] = draw(x, y)
		}
	}
	for _, l := range r {
		fmt.Printf("%s\n", l)
	}
}
