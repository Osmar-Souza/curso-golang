package main

import "fmt"

func main() {
	fmt.Print("Mesma")
	fmt.Print("linha.\n")

	fmt.Println("Nova")
	fmt.Println("linha")

	x := 3.141516

	fmt.Printf("O valor de x é %.2f \n", x)
	fmt.Println("O valor de x é", x)
}
