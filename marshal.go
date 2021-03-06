package main

import (
    "encoding/json"
    "fmt"
)

type Data struct {
	Name string `json:"name"`
	Quantity int `json:"quantity"`
}

func main() {
    result := Data{Name: "abc", Quantity: 10}
	byteArray, err := json.Marshal(result)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(string(byteArray))
}
