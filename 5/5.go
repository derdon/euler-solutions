package main

import "math"

// gcd computes the greatest common divisor using the Euclidean algorithm.
// It follows the pseudo-code, copied from
// http://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations
// function gcd(a, b)
//    while b ≠ 0
//       t := b
//       b := a mod b
//       a := t
//    return a
func gcd(a, b int) int {
	var t float64
	x := float64(a)
	y := float64(b)
	for y != 0 {
		t = y
		y = math.Mod(x, y)
		x = t
	}
	return int(x)
}

// lcm returns the lowest common multiple by using the formula
// lcm(a, b) = a * b / gcd(a, b)
func lcm(a, b int) int {
	x := math.Abs(float64(a))
	y := math.Abs(float64(b))
	return int(x*y) / gcd(a, b)
}

func main() {
	res := 1
	for i := 1; i <= 20; i++ {
		res = lcm(res, i)
	}
	println("res =", res)
}
