package main

import (
	"fmt"
	"io/ioutil"
	"time"
)

const (
	width         = 470
	height        = 120
	pageLimit     = 1479
	numCharacters = height * width
)

func main() {
	// cmd := exec.Command("powershell", "-File", "music.ps1")
	// stdout, err := cmd.Output()
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// fmt.Println(string(stdout))
	// time.After(2 * time.Second)
	for i := 1; i <= pageLimit; i++ {
		name := fmt.Sprintf("ASCII-cxk_%06d.txt", i)
		//打开文本
		time.Sleep(24 * time.Millisecond)
		b, err := ioutil.ReadFile(name)
		if err != nil {
			fmt.Println("Error reading file:", err)
			continue
		}

		//读取文本
		strBytes := b[:numCharacters]
		str := string(strBytes)
		fmt.Print(str)

		//清屏
		fmt.Print("\033[H\033[2J")
	}
}
