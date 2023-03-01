package main

import (
	"fmt"
	"image"
	"os"
	"os/exec"
	"time"

	"gocv.io/x/gocv"
)

// video_addr 为视频的路径(建议绝对路径)
// img gocv.Mat的数组类型 即将要保存的每一帧图片的集合
// point 为image.Point类型 我们在对图片进行resize的时候需要用到(将size减小来缩短程序运行时间)
func video2imgs(video_addr string, imgs *([]gocv.Mat), point image.Point) {
	// 读取视频并返回VideoCapture
	ocp, _ := gocv.OpenVideoCapture(video_addr)
	img := gocv.NewMat()
	//通过for循环读取视频每一帧
	for {
		//如果VideoCapture还能读取到img
		if ocp.Read(&img) {
			img2 := gocv.NewMat()
			// 将彩色视频帧转成灰度图
			gocv.CvtColor(img, &img2, gocv.ColorBGRToGray)
			// resize图片
			gocv.Resize(img2, &img2, point, 0, 0, gocv.InterpolationLinear)
			// 将图片加入图片集
			*imgs = append(*imgs, img2)
		} else {
			break
		}
	}
	defer ocp.Close()
	return
}

// 传入图片 返回二维数组用于展示
func img2char(img gocv.Mat) [][]string {
	// 用于展示的字符 从不明显到明显
	pixels := ` .,-'` + `:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$`
	// 图片归一化(归pixels的长度tvt)
	img.DivideFloat(255 / float32(len(pixels)-1))
	cols, rows := img.Cols(), img.Rows()
	img_string := make([][]string, 0)
	for i := 0; i < rows; i++ {
		row_string := make([]string, 0)
		for j := 0; j < cols; j++ {
			// 将图片的每一个point转化成字符
			row_string = append(row_string, string(pixels[img.GetSCharAt(i, j)]))
		}
		img_string = append(img_string, row_string)
	}
	return img_string
}

// 对图片的每一帧显示加一个间隔 并调用terminal的清屏函数"clear"
// 如果是别的终端可以参考https://studygolang.com/articles/15848
func SleepAndClear() {
	// 延时
	time.Sleep(20 * time.Millisecond)
	// 清屏
	c := exec.Command("bash", "-c", "clear")
	c.Stdout = os.Stdout
	c.Run()
}

func main() {
	point := image.Point{X: 120, Y: 60}
	imgs := make([]gocv.Mat, 0)
	video2imgs("./cxk.mp4", &imgs, point)
	vedio2string := make([][][]string, 0)
	for _, v := range imgs {
		vedio2string = append(vedio2string, img2char(v))
	}
	for z := 0; z < len(vedio2string); z++ {
		for i := 0; i < point.Y; i++ {
			for j := 0; j < point.X; j++ {
				fmt.Print(vedio2string[z][i][j])
			}
			fmt.Println()
		}
		SleepAndClear()
	}
}
