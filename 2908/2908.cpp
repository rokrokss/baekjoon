#include <iostream>
#include <string.h>
using namespace std;

int change(int abc){
	return (100*(abc%10)+abc/100+(abc/10)%10*10);
}

int main() {
	int a, b;
	cin >> a >> b;
	int A = change(a);
	int B = change(b);
	if (A>B){
		cout << A;
	}else{
		cout << B;
	}
	return 0;
}