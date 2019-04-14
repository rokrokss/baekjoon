#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n;
	int a, b, c, d;
	a = n/10;
	b = n%10;
	c = (a + b)%10;
	a = b;
	b = c;
	c = (a + b)%10;
	int i = 1;
	while (a!=n/10||b!=n%10){
		a = b;
		b = c;
		c = (a+b)%10;
		i++;
	}
	cout << i;

	return 0;
}