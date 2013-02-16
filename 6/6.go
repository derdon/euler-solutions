package main

import "math"

func sumOfSquares(n float64) float64 {
	return n * (n + 1) * (2*n + 1) / 6
}

func squareOfSums(n float64) float64 {
	return math.Pow(n * (n + 1) / 2, 2)
}

func main() {
	x := 100.0
	println(int(squareOfSums(x) - sumOfSquares(x)))
}
