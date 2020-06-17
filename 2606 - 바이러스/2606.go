package main

import "fmt"

var (
	ans     = -1
	visited = make([]bool, 101)
)

func dfs(x int, m [][]int) {
	ans++
	visited[x] = true
	for _, y := range m[x] {
		if !visited[y] {
			dfs(y, m)
		}
	}
}

func main() {
	var n, t int
	fmt.Scan(&n)
	fmt.Scan(&t)
	arr := make([][]int, n+1)
	for i := 0; i < t; i++ {
		var a, b int
		fmt.Scan(&a, &b)
		arr[a] = append(arr[a], b)
		arr[b] = append(arr[b], a)
	}
	dfs(1, arr)
	fmt.Println(ans)
}
