package main

func sum(a []int) int {
	var r int
	for _, num := range a {
		r += num
	}
	return r
}
