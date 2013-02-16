package main

func main() {
	res := 0
	a, b := 0, 1
	for {
		a, b = b, a+b
		if a%2 == 0 {
			res += a
		} else if a > 4e6 {
			break
		}
	}
	println(res)
}
