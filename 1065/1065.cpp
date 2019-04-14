#include <iostream>
#include <algorithm>
using namespace std;

bool hansoo(int n){
	int a = n/100;
	int b = (n/10)%10;
	int c = n%10;
	if (a-b==b-c){
		return true;
	}
	else{
		return false;
	}
}

int main() {
	int x;
	cin >> x;
	if (x<100){
		cout << x;
	}else{
		int n = 99;
		for(int i=110;i<=x;i++) {
			if (hansoo(i)){
				n++;
			}
		}
		cout << n;
	}
	return 0;
}