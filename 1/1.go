package main

func main() {
	res := 0
	for i := 1; i < 1000; i++ {
		if i%3 == 0 || i%5 == 0 {
			res += i
		}
	}
	println(res)
}
