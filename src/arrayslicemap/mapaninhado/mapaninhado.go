package main

import "fmt"

func main() {
	funcsPorLetra := map[string]map[string]float64{
		"G": {
			"Gabriela": 15456.78,
			"Guga":     8456.78,
		},
		"J": {
			"José": 11325.45,
		},
		"P": {
			"Pedro": 1200.0,
		},
	}

	delete(funcsPorLetra, "P")

	for letra, funcs := range funcsPorLetra {
		fmt.Println(letra, funcs)

	}

}
