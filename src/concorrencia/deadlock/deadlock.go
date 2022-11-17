package main

import (
	"fmt"
	"time"
)

func rotina(c chan int) {
	time.Sleep(time.Second)
	c <- 1 // operação bloqueante
	fmt.Println("Só depois que foi lido")
}

func main() {
	c := make(chan int) // canal sem buffer
	go rotina(c)

	fmt.Println(<-c)
	fmt.Println("foi lido")
	fmt.Println(<-c)
}
