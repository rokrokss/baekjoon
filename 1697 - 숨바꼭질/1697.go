package main

import "fmt"

func main() {
	max := 100000
	var n, k, ans int
	fmt.Scan(&n, &k)
	q := []int{n}
	visited := make([]bool, max+1)
	visited[n] = true
	seg := 1
	for len(q) > 0 {
		cnt := 0
		moved := false
		for i := 0; i < seg; i++ {
			v := q[0]
			q = q[1:]
			visited[v] = true
			if v == k {
				fmt.Println(ans)
				return
			}
			if v > 0 && !visited[v-1] {
				q = append(q, v-1)
				moved = true
				cnt++
			}
			if v+1 <= max && !visited[v+1] {
				q = append(q, v+1)
				moved = true
				cnt++
			}
			if 2*v <= max && !visited[2*v] {
				q = append(q, 2*v)
				moved = true
				cnt++
			}
		}
		seg = cnt
		if moved {
			ans++
		}
	}
}
