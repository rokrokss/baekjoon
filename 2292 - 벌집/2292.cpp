#include <iostream>
#include <math.h>
#include <string.h>
using namespace std;

int main() {
	double k;
	cin >> k;
	int n = ((int)(sqrt(12*(k-1)-3)-3))/6+2;
	if (k==1){
		cout << 1;
	}
	else {
		cout << n;
	}
	return 0;
}