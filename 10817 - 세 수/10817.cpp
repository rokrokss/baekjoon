#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	int A, B, C;
	cin >> A >> B >> C;
	if (A > B){
		if (C > A){
			cout << A;
		}else if (B > C){
			cout << B;
		}else{
			cout << C;
		}
	}else{
		if (C > B){
			cout << B;
		}else if (C > A){
			cout << C;
		}else{
			cout << A;
		}
	}
	return 0;
}