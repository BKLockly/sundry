#include<bits/stdc++.h>
using namespace std;
int n;
int a[10000]={1},vis[1000];
int lst[10000]={0,1};
bool p[10000]={0,0,1,1,0,1,0,1,0,0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,0,0};


void dfs(int k){
    
	if(k>n){
		if(p[lst[n]+1]){
			for(int i=1;i<=n;i++){
				if(i==1){
					cout << lst[i];
				}else{
					cout << " " << lst[i];
				}
			}
			cout<<endl;
		}
		return ;
	}
	for(int i=2;i<=n;i++){
		if(!vis[i]){
			if(p[i+lst[k-1]]){
				vis[i]=1;
				lst[k]=i;
				dfs(k+1);
				vis[i]=0;
			}
		}
	}
	return ;
}


int main() {
	
	int ans=0;
    while(cin >> n){
		ans++;
		cout<<"Case"<<" "<< ans <<":" <<endl;
		if(n%2==0){
		dfs(2);
	}
		cout<<endl;
	  }
	  return 0;
}