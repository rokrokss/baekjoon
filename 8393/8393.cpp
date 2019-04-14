#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	int n;
	cin >> n;
	int a = 0;
	for (int i=1;i<=n;i++) {
		a=a+i;
	}
	cout << a;
	return 0;
}