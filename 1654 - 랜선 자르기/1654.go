package main

import "fmt"

func main() {
	var k, n int
	fmt.Scan(&k, &n)
	arr := make([]int, k)
	for i := 0; i < k; i++ {
		fmt.Scan(&arr[i])
	}
	left := 1
	right := arr[0]
	for i := 0; i < k; i++ {
		if arr[i] > right {
			right = arr[i]
		}
	}
	var mid int
	for left <= right {
		mid = (left + right) / 2
		cnt := 0
		for i := 0; i < k; i++ {
			cnt += arr[i] / mid
		}
		if cnt >= n {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	fmt.Println(right)
}
