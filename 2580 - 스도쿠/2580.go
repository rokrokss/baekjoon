package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	wr    = bufio.NewWriter(os.Stdout)
	board [9][9]int
	row   [9][10]bool
	col   [9][10]bool
	inner [9][10]bool
)

func innerIdx(y, x int) int {
	return x/3 + (y/3)*3
}

func printBoard() {
	for _, line := range board {
		for _, v := range line {
			wr.WriteByte(byte(v) + '0')
			wr.WriteByte(' ')
		}
		wr.WriteByte('\n')
	}
	wr.Flush()
	os.Exit(0)
}

func solve(cnt int) {
	if cnt == 81 {
		printBoard()
	}
	y, x := cnt/9, cnt%9
	if board[y][x] != 0 {
		solve(cnt + 1)
	} else {
		for i := 1; i <= 9; i++ {
			if !row[y][i] && !col[x][i] && !inner[innerIdx(y, x)][i] {
				board[y][x] = i
				row[y][i] = true
				col[x][i] = true
				inner[innerIdx(y, x)][i] = true
				solve(cnt + 1)
				board[y][x] = 0
				row[y][i] = false
				col[x][i] = false
				inner[innerIdx(y, x)][i] = false
			}
		}
	}
}

func main() {
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			fmt.Scan(&board[i][j])
			if board[i][j] != 0 {
				row[i][board[i][j]] = true
				col[j][board[i][j]] = true
				inner[innerIdx(i, j)][board[i][j]] = true
			}
		}
	}
	solve(0)
}
