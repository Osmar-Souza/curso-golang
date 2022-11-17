package main

import "fmt"

func main() {
	i := 1

	// Go não tem aritmérica de ponteiros

	var p *int = nil

	p = &i // pegando o endereço da variavel i
	*p++   // desreferenciando (pegando o valor)
	i++
	fmt.Println(p, *p, i, &i)

}
