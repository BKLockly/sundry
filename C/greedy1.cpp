#include <stdio.h> 
// C 语言代码
int main() 
{ 
 int n,m; 
 printf("Input the number of elements: \n");
 scanf("%d", &n);
 int w[n],v[n]; // w 是表示重量, v 表示价值
 for (int i = 0; i< n; i++) 
 { 
 printf("Please input weight and value:");
 scanf("%d %d", &w[i], &v[i]); 
 } 
 // 按重量排序
for(int i=0;i<n;i++){
 for(int j=0;j< n-1-i;j++){
 if(w[j]>w[j+1]){
 int temp = w[j];
 w[j] = w[j+1];
 w[j+1] = temp;
 
 temp = v[j];
 v[j] = v[j+1];
 v[j+1] = temp;
        }
    }
}
 
//输出结果
printf("The result is:\n");
for(int i=0;i<n;i++){
 printf("%d %d\n",w[i],v[i]);
}
 
 return 0; 
}
 
