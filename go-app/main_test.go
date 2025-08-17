package main

import "testing"

func TestGreet(t *testing.T) {
	got := greet("Go")
	want := "Hello, Go!"
	if got != want {
		t.Errorf("greet() = %q; want %q", got, want)
	}
}
