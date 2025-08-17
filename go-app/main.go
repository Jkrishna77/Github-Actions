package main

import "fmt"

func greet(name string) string {
	return "Hello, " + name + "!" + "Testing CI"
}

func main() {
	fmt.Println(greet("GitHub Actions"))
}
