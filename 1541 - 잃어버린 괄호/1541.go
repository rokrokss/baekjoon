package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var str string
	fmt.Scanln(&str)
	arr := strings.Split(str, "-")
	ans := 0
	for i, str2 := range arr {
		if i == 0 {
			arr2 := strings.Split(str2, "+")
			for _, str3 := range arr2 {
				a, _ := strconv.Atoi(str3)
				ans += a
			}
		} else {
			arr2 := strings.Split(str2, "+")
			for _, str3 := range arr2 {
				a, _ := strconv.Atoi(str3)
				ans -= a
			}
		}
	}
	fmt.Println(ans)
}
