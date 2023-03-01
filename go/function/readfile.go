package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"strings"
)

func readToLine(f string) string {
	file, err := os.Open(f)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var text string
	for scanner.Scan() {
		line := scanner.Text()
		text = text + " " + strings.TrimSpace(line)
	}
	return text
}

func main() {
	flags1 := readToLine("sysinfo.ps1")
	fmt.Print(flags1)
	command := exec.Command("powershell", "/c", flags1)
	buf, _ := command.Output()
	output := string(buf)
	fmt.Print(output)
}
