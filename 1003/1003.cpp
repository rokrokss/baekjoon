#include <iostream>
using namespace std;

void fibbb(int n){
	if (n==0) {
		cout << 1 << " " << 0 << endl;
	}
	else if (n==1){
		cout << 0 << " " << 1 << endl;
	}
	else{
		int* before = new int[2];
		before[0]=1;
		before[1]=0;
		int* cur= new int [2];
		cur[0]=0;
		cur[1]=1;
		int* temp = new int [2];
		for (int i = 1; i < n; i++){
			temp[0] = cur[0];
			temp[1] = cur[1];
			cur[0]=cur[0]+before[0];
			cur[1]=cur[1]+before[1];
			before[0] = temp[0];
			before[1] = temp[1];
		}
		cout << cur[0] << " " << cur[1] << endl;
	}
}

int main() {
	int n;
	cin>>n;
	for (int i=0;i<n;i++){
		int a;
		cin>>a;
		fibbb(a);
	}
	return 0;
}