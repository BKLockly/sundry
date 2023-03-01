package main

import (
	"fmt"
	"log"
	"os/exec"
)

func main() {
	cmd := exec.Command("powershell", "-File", "music.ps1")
	stdout, err := cmd.Output()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(stdout))
}
