#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;


int main() {
	int t;
	cin >> t;
	for (int a=0; a<t; a++){
		int n;
		cin >> n;
		string s;
		cin >> s;
		int length = s.size();
		for(int i=0;i<length;i++){
			for(int j=0;j<n;j++) {
				printf("%c", s[i]);
			}
		}
		printf("\n");
	}
	return 0;
}