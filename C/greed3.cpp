#include<iostream>

void swap(int &a, int &b) {
 int temp;
 temp = a;
 a= b;
 b = temp;
}

int main() {
 int n = 8; //��Ʒ���� 
 int w[8] = {7, 4, 4, 6, 2, 2, 3, 5}; //��Ʒ���� 
 int V[8] = {8, 7, 5, 7, 1, 5, 4, 6}; //��Ʒ��ֵ 
 int Cap = 15; //�������� 
 int result[8][2]; //�������

 //���ݵ�λ��������
 for(int i=0;i<n-1;i++)
 for(int j=0;j<n-1-i;j++)
 if(V[j]/w[j] < V[j+1]/w[ 1]) 
 swap(V[j],V[j+1]),swap(w[j],w[j+1]);
//̰�Ĳ�������������
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

//��ӡ�������
for (int i=0;i<n;i++)
    std::cout << result[i][0];
std::cout << std::endl;
return 0;
}

