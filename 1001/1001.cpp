#include <iostream>
using namespace std;

int main() {
	string a;
	string b;
	cin >> a;
	cin >> b;
	int A = std::stoi(a);
	int B = std::stoi(b);
	cout << A-B;
	return 0;
}