package main

import (
	"fmt"
)

func main() {
	var n, k, ans int
	fmt.Scan(&n, &k)
	left := 1
	right := k
	for left <= right {
		cnt := 0
		mid := (left + right) / 2
		for i := 1; i <= n; i++ {
			div := mid / i
			if div > n {
				cnt += n
			} else {
				cnt += div
			}
		}
		if cnt < k {
			left = mid + 1
		} else {
			right = mid - 1
			ans = mid
		}
	}
	fmt.Println(ans)
}
