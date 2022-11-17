package main

import (
	"fmt"
	"time"
)

func fale(pessoa, texto string, qtde int) {
	for i := 0; i < qtde; i++ {
		time.Sleep(time.Second)
		fmt.Printf("%s: %s (iteração %d)\n", pessoa, texto, i+1)
	}
}

func main() {
	// fale("Maria", "pq vc não fala comigo", 3)-
	// fale("João", "só posso falar dps", 1)

	// go fale("Maria", "Ei...", 4)
	// go fale("João", "Opa...", 1)

	go fale("Maria", "Entendi...", 10)
	fale("João", "Opa...", 5)
}
