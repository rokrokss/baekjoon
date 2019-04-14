#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	int n;
	cin >> n;
	int a = 0;
	int c = getchar();
	for (int i = 0; i < n; i++) {
		int b = (int) getchar() - 48;
		a = a + b;
	}

	cout << a;
	return 0;
}