#include<iostream>
using namespace std;

int main()
{
    int w[] = {7, 4, 4, 6,2,2,3,5}; 
    int v[] = {8, 7,5,7,1,5,4,6}; 
    
    for(int i = 0; i < 8; i++) {
        int count = 1;
        for(int j=i+1; j<8; j++) {
            if(w[j] == w[i]) {
                v[i] += count;
                count++;
            }
        }
    }
    cout << "w" << " " << "v" << endl;
for(int i=0; i<8; i++) { 
    cout << w[i] << " " << v[i] << endl;
}
cout << endl;
return 0;
}

