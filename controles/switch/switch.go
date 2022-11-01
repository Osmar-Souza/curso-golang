package main

import "fmt"

func notaParaConceito(n float64) string {
	var nota = int(n)
	switch nota {
	case 10:
		fallthrough
	case 9:
		return "A"
	case 8, 7:
		return "B"
	case 6, 5:
		return "C"
	case 4, 3:
		return "D"
	case 2, 1, 0:
		return "E"
	default:
		return "Nota invalida"
	}
}

func main() {
	nota1 := notaParaConceito(5)
	nota2 := notaParaConceito(11)
	nota3 := notaParaConceito(8)
	nota4 := notaParaConceito(1)
	fmt.Println(nota1)
	fmt.Println(nota2)
	fmt.Println(nota3)
	fmt.Println(nota4)
}
