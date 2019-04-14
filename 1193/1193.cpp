#include <iostream>
#include <math.h>
using namespace std;


int main() {
	double n;
	cin >> n;
	double formula = 1+(sqrt(8*n-7)-1)/2;
	int k = (int)formula;
	int cnt = (int)n - (k*k-k)/2;

	if(k%2==0){
		cout << cnt << "/" << k-cnt+1;
	}else{
		cout << k-cnt+1 << "/" << cnt;
	}
	return 0;
}