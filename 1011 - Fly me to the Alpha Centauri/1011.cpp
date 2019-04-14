#include <iostream>
#include <math.h>
using namespace std;



int main() {
	int t;
	cin >> t;
	for (int i=0;i<t;i++){
		int x, y;
		cin >> x >> y;
		int d = abs(x-y);
		int n = (int)sqrt((double)d);
		int r = d - n*n;
		int rest = r/n;
		int answer;
		if (r%n==0) {
			answer = 2 * n - 1 + rest;
		}
		else {
			answer = 2 * n - 1 + rest + 1;
		}
		cout << answer << endl;
	}
	return 0;
}