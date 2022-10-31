package main

import (
	"fmt"
	"math"
)

func main() {
	a := 3
	b := 2

	fmt.Println("soma =>", a+b)
	fmt.Println("subtração =>", a-b)
	fmt.Println("divisão =>", a/b)
	fmt.Println("multiplicação =>", a*b)
	fmt.Println("módulo =>", a%b)

	// bitwise
	fmt.Println("E =>", a&b)
	fmt.Println("Ou =>", a|b)
	fmt.Println("Xor =>", a^b)

	c := 3.0
	d := 2.0

	// outras operações usando math
	fmt.Println("Maior =>", math.Max(float64(a), float64(b)))
	fmt.Println("Menor =>", math.Min(c, d))
	fmt.Println("Exponenciação =>", math.Pow(c, d))
}
