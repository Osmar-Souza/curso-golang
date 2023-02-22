package main

import (
	"encoding/csv"
	"encoding/json"
	"io"
	"log"
	"net/http"
	"os"
	"strconv"
)

type tpDimensionsProperties struct {
	A   float64 `json:"a"`
	Bf  float64 `json:"bf"`
	Cw  float64 `json:"cw"`
	D   float64 `json:"d"`
	H   float64 `json:"h"`
	Ixx float64 `json:"ixx"`
	Iyy float64 `json:"iyy"`
	J   float64 `json:"j"`
	T   float64 `json:"t"`
	Xcg float64 `json:"xcg"`
	Xs  float64 `json:"xs"`
	Ycg float64 `json:"ycg"`
	Ys  float64 `json:"ys"`
}

type Profile struct {
	Description        string                 `json:"description"`
	DimensionsProperty tpDimensionsProperties `json:"dimensionsProperties"`
	ID                 int64                  `json:"id"`
}

func getProfile(w http.ResponseWriter, r *http.Request) {
	// Abrindo o arquivo CSV
	file, err := os.Open("data/z_properties_final.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Criando um leitor CSV
	reader := csv.NewReader(file)

	var dataList []Profile

	reader.Comma = ';' // define a ponto e vírgula como separador de campo

	// Lendo as linhas do arquivo CSV
	for {
		line, err := reader.Read()
		if err == io.EOF {
			break
		} else if err != nil {
			log.Fatal(err)
		}

		// Convertendo as strings lidas em tipos apropriados
		id, _ := strconv.ParseInt(line[0], 10, 64)
		description := line[1]
		a, _ := strconv.ParseFloat(line[2], 64)
		bf, _ := strconv.ParseFloat(line[3], 64)
		cw, _ := strconv.ParseFloat(line[4], 64)
		d, _ := strconv.ParseFloat(line[5], 64)
		h, _ := strconv.ParseFloat(line[6], 64)
		ixx, _ := strconv.ParseFloat(line[7], 64)
		iyy, _ := strconv.ParseFloat(line[8], 64)
		j, _ := strconv.ParseFloat(line[9], 64)
		t, _ := strconv.ParseFloat(line[10], 64)
		xcg, _ := strconv.ParseFloat(line[11], 64)
		xs, _ := strconv.ParseFloat(line[12], 64)
		ycg, _ := strconv.ParseFloat(line[13], 64)
		ys, _ := strconv.ParseFloat(line[14], 64)

		// Criando um objeto Data
		data := Profile{
			ID:          id,
			Description: description,
			DimensionsProperty: tpDimensionsProperties{
				A:   a,
				Bf:  bf,
				Cw:  cw,
				D:   d,
				H:   h,
				Ixx: ixx,
				Iyy: iyy,
				J:   j,
				T:   t,
				Xcg: xcg,
				Xs:  xs,
				Ycg: ycg,
				Ys:  ys,
			},
		}

		// Adicionando o objeto Data a lista de objetos
		dataList = append(dataList, data)
	}

	// Convertendo a lista de objetos Data em um JSON
	jsonData, err := json.MarshalIndent(dataList, "", "  ")
	if err != nil {
		log.Fatal(err)
	}

	w.Header().Set("Content-Type", "application/json")
	w.Write(jsonData)

}

func main() {
	http.HandleFunc("/getProfile", getProfile)
	log.Println("Executando...")
	http.ListenAndServe(":3000", nil)
}
