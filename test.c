#include<stdio.h> 

void swap(int &a,int &b){
 int temp;
 temp = a;
 a= b;
 b = temp;
}

int main(){
    int n = 8; //物品数量 
    int w[8] = {7, 4, 4, 6, 2, 2, 3, 5}; //物品重量 
    int V[8] = {8, 7, 5, 7, 1, 5, 4, 6}; //物品价值 
    int Cap = 15; //背包容量 
    int result[8][2]; //最优组合

    //依据单位重量排序
    for(int i=0;i<n-1;i++)
        for(int j=0;j<n-1-i;j++)
            if(V[j]/w[j] < V[j+1]/w[ 1]) 
                swap(V[j],V[j+1]),swap(w[j],w[j+1]);
    //贪心策略求解最优组合
    int c=0,v=0;
    while(Cap>=0){
        if(Cap>=w[c]){
            result[c][0]=1;
            Cap-=w[c];
            v+=V[c];
        }
        else
            result[c][0]=0;
        result[c][1]=v;
        c++;
    }

    //打印最优组合
    for (int i=0;i<n;i++)
        printf("%d",result[i][0]);
	printf("\n");
    return 0;
}
