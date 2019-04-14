#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	int N;
	cin >> N;
	int a=0;
	int b=0;
	int c=N;
	while (c%5!=0){
		c=c-3;
		a++;
	}
	if (c<0){
		cout << -1;
	}
	else{
		b=c/5;
		cout << b+a;
	}
	return 0;
}