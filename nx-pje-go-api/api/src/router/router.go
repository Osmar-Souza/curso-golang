package router

import "github.com/gorilla/mux"

// vai retonrar um router com as rotas configuradas
func Gerar() *mux.Router {
	return mux.NewRouter()
}
