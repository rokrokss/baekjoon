package main

import "fmt"

var (
	movex = []int{1, -1, 0, 0}
	movey = []int{0, 0, 1, -1}
)

func main() {
	var N, M, x, y int
	var visited [][][]bool
	fmt.Scan(&N, &M)
	grid := make([]string, N)
	visited = make([][][]bool, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&grid[i])
		visited[i] = make([][]bool, M)
		for j := 0; j < M; j++ {
			visited[i][j] = make([]bool, 64)
			if grid[i][j] == '0' {
				x, y = i, j
			}
		}
	}
	q := [][]int{[]int{x, y, 0, 0}}
	visited[x][y][0] = true
	for len(q) > 0 {
		x, y, key, cnt := q[0][0], q[0][1], q[0][2], q[0][3]
		q = q[1:]
		if grid[x][y] == '1' {
			fmt.Println(cnt)
			return
		}
		cnt++
		for i := 0; i < 4; i++ {
			dx, dy := movex[i], movey[i]
			mx, my := x+dx, y+dy
			if mx >= 0 && mx < N && my >= 0 && my < M && !visited[mx][my][key] {
				if grid[mx][my] == '.' || grid[mx][my] == '1' || grid[mx][my] == '0' {
					q = append(q, []int{mx, my, key, cnt})
					visited[mx][my][key] = true
				} else if 'a' <= grid[mx][my] && grid[mx][my] <= 'f' {
					visited[mx][my][key] = true
					newkey := key | (1 << (grid[mx][my] - 'a'))
					visited[mx][my][newkey] = true
					q = append(q, []int{mx, my, newkey, cnt})
				} else if 'A' <= grid[mx][my] && grid[mx][my] <= 'F' {
					if ((1 << (grid[mx][my] - 'A')) & key) != 0 {
						visited[mx][my][key] = true
						q = append(q, []int{mx, my, key, cnt})
					}
				}
			}
		}
	}
	fmt.Println(-1)
}
