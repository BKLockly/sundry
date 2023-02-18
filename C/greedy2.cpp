

#include<iostream>
using namespace std;

int main()
{
    int w[] = {7, 4, 4, 6,2,2,3,5}; //数组w，用来存储原始数字
    int v[] = {8, 7,5,7,1,5,4,6}; //数组v，用来存储处理后的数组中每个元素出现的次数
    
    for(int i = 0; i < 8; i++)
    {
        int count = 1;
        for(int j=i+1; j<8; j++)
        {
            if(w[j] == w[i])
            {
                v[i] += count;
                count++;
            }
        }
    }

//输出处理后的数字，每行一组
for(int i=0; i<8; i++)
{ 
    cout << w[i] << " " << v[i] << endl;
}
cout << endl;

return 0;
}


