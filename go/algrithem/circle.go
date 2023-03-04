package main

import (
	"fmt"
)

// 判断一个数是否为素数
func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	var n int       // 圆圈数
	var caseNum int // 测试用例编号
	for {
		nCou, err := fmt.Scan(&n)
		if nCou == 0 || err != nil { // 当没有输入或输入错误时退出循环
			break
		}
		if caseNum > 0 { // 输出测试编号
			fmt.Println()
		}
		caseNum++
		fmt.Printf("Case %d:\n", caseNum)
		nums := make([]int, n)
		for i := 0; i < n; i++ {
			nums[i] = i + 1
		}
		// 首位数字为1， 其他数字放在圆环上
		perms := permutation(nums[1:])
		for _, perm := range perms {
			circle := append([]int{1}, perm...)
			if isPrime(circle[0] + circle[len(circle)-1]) { // 判断首尾数字之和是否素数
				flag := true
				for i := 1; i < len(circle); i++ {
					if !isPrime(circle[i-1] + circle[i]) {
						flag = false // 如果相邻两个数字之和不是素数，将flag置为false
						break
					}
				}
				if flag { // 如果所有相邻数字之和都是素数，打印出此排列方案
					for _, num := range circle {
						fmt.Print(num, " ")
					}
					fmt.Println()
				}
			}
		}
	}
}

// 排列函数，返回一个slice中元素的全排列
func permutation(nums []int) [][]int {
	if len(nums) == 1 { // 终止条件：如果slice只有一个元素，返回他本身
		return [][]int{{nums[0]}}
	}
	var res [][]int
	for i, num := range nums {
		subNums := append(append([]int{}, nums[:i]...), nums[i+1:]...) // 子slice为其他元素
		subPerms := permutation(subNums)                               // 获取所有子slice的全排列
		for _, subPerm := range subPerms {
			res = append(res, append([]int{num}, subPerm...)) // 将当前元素与子排列进行组合并加入最后返回值的slice中
		}
	}
	return res
}
