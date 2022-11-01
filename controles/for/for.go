package main

import (
	"fmt"
	"time"
)

func main() {

	i := 1
	for i <= 10 {
		fmt.Println(i)
		i++
	}

	for i := 0; i <= 20; i += 2 {
		fmt.Printf("%d", i)
	}

	fmt.Println("Misturando.. ")
	for i := 1; i <= 10; i++ {
		if i%2 == 0 {
			fmt.Printf("%d é Par\n", i)
		} else {
			fmt.Printf("%d é Impar\n", i)
		}
	}

	for {
		// laço infinito
		fmt.Println("Para sempre...")
		time.Sleep(time.Second)
	}
}
