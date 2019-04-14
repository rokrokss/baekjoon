#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i=0;i<t;i++){
		int m,n,x,y;
		cin >> m >> n >> x >> y;
		int k = x;
		int tmp = 0;
		bool done = false;
		while ((tmp==0||tmp%n!=0)&&tmp<=m*n){
			if(k%n==y%n){
				cout << k;
				done = true;
				break;
			}
			else{
				k=k+m;
				tmp=tmp+m;
			}
		}
		if(!done){
			cout << -1;
		}
		if(i!=t-1){
			cout << "\n";
		}
	}
	return 0;
}