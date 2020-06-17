package main

import "fmt"

var (
	mm = make([][]int, 50)
	dx = []int{1, -1, 0, 0}
	dy = []int{0, 0, 1, -1}
)

func dfs(x, y int) {
	for i := 0; i < 4; i++ {
		xx := x + dx[i]
		yy := y + dy[i]
		if xx < 0 || xx >= 50 || yy < 0 || yy >= 50 {
			continue
		}
		if mm[xx][yy] == 1 {
			mm[xx][yy] = 2
			dfs(xx, yy)
		}
	}
}

func main() {
	var t, m, n, k int
	fmt.Scan(&t)
	for ; t > 0; t-- {
		fmt.Scan(&m, &n, &k)
		for i := 0; i < 50; i++ {
			mm[i] = make([]int, 50)
		}
		for ; k > 0; k-- {
			var x, y int
			fmt.Scan(&x, &y)
			mm[x][y] = 1
		}
		ans := 0
		for i := 0; i < 50; i++ {
			for j := 0; j < 50; j++ {
				if mm[i][j] == 1 {
					ans++
					mm[i][j] = 2
					dfs(i, j)
				}
			}
		}
		fmt.Println(ans)
	}
}
